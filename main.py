from src.chat.localchat import add_message, chat

def main():
    messages = []

    while True:
        # Get user input
        user_query = input("\nAsk a question (or 'exit' to quit): ").strip()
        
        # Check for exit command
        if user_query.lower() == 'exit':
            break

        # 1. Add User's question to history
        add_message(messages, "user", user_query)
        
        # 2. Get the answer from LLM
        answer = chat(messages)
        print(f"Answer: {answer}")

        # 3. Add the Assistant's actual ANSWER to history 
        add_message(messages, "assistant", answer)

if __name__ == "__main__":
    main()