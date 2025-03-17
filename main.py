from agent.agent import Agent

def main():
    agent = Agent()
    while True:
        query = input("User: ")
        if query.lower() == "exit":
            break
        response = agent.respond(query)
        print("Agent:", response)

if __name__ == "__main__":
    main()