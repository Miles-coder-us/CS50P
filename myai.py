def respond(message):
    message = message.lower().strip()

    if "hello" in message or "hi" in message:
        return "Hey! How can I help you?"
    elif "how are you" in message:
        return "I'm just a program but I'm doing great!"
    elif "your name" in message:
        return "I'm a simple chatbot built in Python."
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! See you later."
    elif "help" in message:
        return "I can respond to hello, how are you, your name, and bye."
    else:
        return "I don't understand that yet. Try saying hello!"

def main():
    print("Chatbot started! Type 'bye' to exit.")
    while True:
        message = input("You: ")
        reply = respond(message)
        print(f"Bot: {reply}")
        if "bye" in message.lower():
            break

main()