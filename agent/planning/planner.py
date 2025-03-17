from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY

def generate_plan(query, history):
    """Generates a plan using the LLM."""
    llm = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY, model="gemini-2.0-flash")
    prompt = f"""
    Given the user query: "{query}" and conversation history: "{history}", generate a step-by-step plan.
    Plan:
    """
    plan = llm.invoke(prompt)
    return plan.content