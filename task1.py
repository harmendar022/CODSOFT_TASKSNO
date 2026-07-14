import re

def get_response(user_input):
    # Convert input to lowercase to ensure case insensitivity
    user_input = user_input.lower().strip()
    
    # Predefined rules and response mappings
    rules = {
        r"hello|hi|hey|greetings": "Hello! How can I help you with your AI internship today?",
        r"how are you": "I'm just a computer program, but I'm functioning perfectly! How are you?",
        r"your name|who are you": "I am a simple rule-based AI assistant built for Task 1.",
        r"codsoft": "CodSoft is an innovative tech education platform helping developers grow!",
        r"what is ai|artificial intelligence": "Artificial Intelligence is the simulation of human intelligence by machines.",
        r"help|support": "Sure! Tell me what you need, and I'll do my best to assist you.",
        r"bye|goodbye|exit": "Goodbye! Have a great day and happy coding!"
    }
    
    # Iterate through rules and match
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
            
    return "I'm sorry, I didn't quite understand that. Can you rephrase? (Type 'bye' to exit)"

def start_chatbot():
    print("=========================================")
    print("    CODSOFT CHATBOT (Task 1 Started)     ")
    print("=========================================")
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chatbot()
