from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY
from agent.memory.memory import Memory
from agent.tools.search_tool import search_google
from agent.planning.planner import generate_plan
from utils.helper import format_markdown, clean_text

class Agent:
    def __init__(self, system_prompt_path="agent/prompts/system_prompt.txt"):
        self.llm = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY, model="gemini-2.0-flash")
        self.memory = Memory()
        with open(system_prompt_path, "r") as f:
            self.system_prompt = f.read()

    def respond(self, query):
        history = self.memory.get_history()
        plan = generate_plan(query, history)

        self.memory.add({"user": query, "plan": plan}) # store plan in memory.

        messages = [{"role": "system", "content": self.system_prompt},  # System instruction
                    {"role": "user", "content": query}]  # User query
        
        if "search" in plan.lower(): # Basic plan recognition. Refinement Needed.
            search_results = search_google(query)
            messages.append({"role": "assistant", "content": f"Search Results: {search_results}"})

        response = self.llm.invoke(messages) # invoke llm

        formatted_response = format_markdown(clean_text(response.content)) #markdown response

        self.memory.add({"user": query, "response": formatted_response}) # save to memory
        
        return formatted_response