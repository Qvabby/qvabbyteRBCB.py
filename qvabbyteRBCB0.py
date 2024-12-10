# qvabbyteRBCB0 - qvabbyte Rule-based Chatbot v0
import random as r
import re

qvabbyteVersionNameString = "qvabbyteRBCB0"
version = "RBCB0"

def get_random_greeting():
    greeting_phrases = [
        "Hello, what's on your mind today?",
        "How can I help?",
        "Sup, what's going on?"
    ]
    return r.choice(greeting_phrases)

def get_random_bye():
    bye_phrases = ["Arrivederci.", "Bye-bye.", "See ya!"]
    return r.choice(bye_phrases)

def handle_unknown():
    return "I am yet rule-based and can't really understand what you mean."

def qvabbyte():
    global qvabbyteVersionNameString, version
    chatbot = qvabbyteVersionNameString

    print("-------------- q v a b b y t e --------------")
    print("(Type 'bye' to exit)")
    print(f"{get_random_greeting()}")

    user_want = ""
    saves = { }
    while True:
        # User Input
        user_input = input("You: ").lower().strip()
        # Exit Code
        if user_input == "bye":
            print(f"{chatbot}: {get_random_bye()}")
            break
        # Hardcoded Responses
        if re.search(r"\bhi\b|\bhello\b",user_input):
            print(f"{chatbot}: Hello. How can I assist you today?")
        elif "how are you" in user_input:
            print(f"{chatbot}: I feel Pythonic. How about you?")
        elif "your name" in user_input:
            print(f"{chatbot}: q v a b b y t e | Version: {version}")
        #using re module (python regular expression)
        elif re.search(r"help .*me|assist .*me|\bhelp",user_input):
            print("what do you need help with?")
            user_want = "help"
        elif re.search(r"what .*i.*want",user_input):
            if user_want == "help":
                print("you need help with something...")
        elif re.search(r"my name is (.+)",user_input):
            saves["user_name"] = re.search(r"my name is (.+)", user_input).group(1)
        #handle unknown.
        else:
            print(f"{chatbot}: {handle_unknown()}")

if __name__ == "__main__":
    qvabbyte()