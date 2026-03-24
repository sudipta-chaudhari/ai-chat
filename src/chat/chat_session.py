# ChatSession manages conversation message history


class ChatSession:
    """
    Manages the conversation message history for a chat session.
    Stores and provides access to all messages exchanged in the conversation.
    """

    def __init__(self):
        """Initialize an empty message history."""
        self.messages = []

    def add(self, role: str, content: str):
        """
        Adds a new message to the conversation history.

        Args:
            role (str): The speaker's role ('user', 'assistant', or 'system').
            content (str): The actual text content of the message.
        """
        message = {"role": role, "content": content}
        self.messages.append(message)

    def get_all(self) -> list:
        """
        Retrieves the complete message history.

        Returns:
            list: All messages in the conversation.
        """
        return self.messages

    def clear(self):
        """Clears the entire conversation history."""
        self.messages = []
