# Import the custom chat functions
from src.chat.localchat import add_message, chat

def main():
    """
    Runs a continuous terminal-based chat loop that maintains conversation 
    context by storing history in a local list.
    """
    # This list acts as the "short-term memory" for the session.
    # It stores every exchange so the AI can remember previous questions.
    messages = []

    # Start an infinite loop to allow for back-and-forth dialogue
    while True:
        # Capture user input from the terminal and remove extra whitespace
        user_query = input("\nAsk a question (or 'exit' to quit): ").strip()
        
        # Provide a clean way for the user to close the application
        if user_query.lower() == 'exit':
            break

        # 1. Store the user's prompt in the history list. 
        # This tells the LLM: "The human just said this."
        add_message(messages, "user", user_query)
        
         # 2. Package the entire history and send it to the model.
        # The model processes the context and generates a response.
        answer = chat(messages)

        # Display the model's reply to the user        
        print(f"Answer: {answer}")

        # 3. CRITICAL STEP: Store the AI's answer back into history.
        # Without this, the AI will "forget" what it just said in the next turn.
        add_message(messages, "assistant", answer)

# Standard Python entry point: only run main() if this file is executed directly
if __name__ == "__main__":
    main()