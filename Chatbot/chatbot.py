import random

# simple rule-based chatbot logic
def bot_reply(user_input: str) -> str:
    user_input = user_input.lower()
    if "hi" in user_input or "hello" in user_input:
        return "Hello! How are you today?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "how are you" in user_input:
        return "I'm just code, but I'm vibing 😎"
    else:
        responses = [
            "Interesting... tell me more!",
            "Oh really?",
            "That sounds cool!",
            "Hmm, I'm not sure about that."
        ]
        return random.choice(responses)
