# # Adding Basic Conversation logic
# responses = {
#     "hello":"Hi there!, How can I help you?",
#     "how are you?":"I'm just a bot, but I'm doing great! How about you?",
#     "what's your name?":"I'm Chatbot, your friendly assistant.",
#     "bye":"Goodbye! Take care!"
# }

def get_responses(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I assist you?"
    elif "how are you?" in user_input:
        return "I'm doing great! How can I help you today?"
    elif "your name" in user_input:
        return "I'm Chatbot, your virtual assistant"
    elif "bye" in user_input:
        return "Goodbye! Have a wonderful day!"
    else:
        return "I'm not sure how to respond to that"

# Basic structure of this chatbot

def chatbot():
    print("Hello! I'm Chatbot. Type 'exit' to end the chat.!")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        # elif user_input in responses:
        #     print(f"Chatbot: {responses[user_input]}")
        # else: 
        #     print("Chatbot: I'm not sure how to respond to that.")
        response = get_responses(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()