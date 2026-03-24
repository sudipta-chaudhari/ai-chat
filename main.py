# Import the chat classes and settings
from src.chat import ChatClient, ChatSession
from src.settings import settings


def main():
    """
    Runs a continuous terminal-based chat loop that maintains conversation 
    context by storing history in a local ChatSession instance.
    """
    
    # Initialize the chat client and session
    client = ChatClient(settings)
    session = ChatSession()

    print(f"🤖 Chat initialized with model: {settings.model}")
    print("Type 'exit' to quit, 'clear' to clear conversation history")
    print("-" * 50)

    # Start an infinite loop to allow for back-and-forth dialogue
    while True:
        try:
            # Capture user input from the terminal and remove extra whitespace
            user_query = input("\nYou: ").strip()

            # Handle special commands
            if user_query.lower() == "exit":
                print("Goodbye!")
                break
            elif user_query.lower() == "clear":
                session.clear()
                print("Conversation history cleared.")
                continue
            elif not user_query:
                continue

            # 1. Store the user's prompt in the session history.
            # This tells the LLM: "The human just said this."
            session.add("user", user_query)

            # 2. Package the entire history and send it to the model.
            # The model processes the context and generates a response.
            print("Assistant: ", end="", flush=True)
            answer = client.send(session.get_all())

            # Display the model's reply to the user
            print(answer)

            # 3. CRITICAL STEP: Store the AI's answer back into history.
            # Without this, the AI will "forget" what it just said in the next turn.
            session.add("assistant", answer)

        except KeyboardInterrupt:
            print("\n\nInterrupted. Type 'exit' to quit or continue chatting.")
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")


# Standard Python entry point: only run main() if this file is executed directly
if __name__ == "__main__":
    main()