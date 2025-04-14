# qvabbyteRBCB0 - qvabbyte Rule-based Chatbot v0.1
import random as r
import re
qvabbyteVersionNameString = "qvabbyteRBCB0.1"
version = "RBCB0.1"
chatbot = "qvabbyte"
def get_random_greeting():
    greeting_phrases = [
        "Hello, what's on your mind today?",
        "How can I help?",
        "Sup, what's going on?",
        "Hola Amigo, que espanol?",
        "Bonjour",
        "Hello you look sexy tonight"
    ]
    return r.choice(greeting_phrases)
def get_random_bye():
    bye_phrases = ["Arrivederci.", "Bye-bye.", "See ya!"]
    return r.choice(bye_phrases)
def handle_unknown():
    fallback_phrases = [
        f"I'm not sure I got that. Could you rephrase?",
        f"I'm still learning! Can you try saying it differently?",
        f"Hmm, I don't understand that yet. Help me learn by asking something else!",
        f"bro im not even a 150 line of a code, i don't understand that much sorry.",
        f"idk that bro",
        f"GIVE ME CLEARER INPUT",
        f"I AM    R O B O T    I can't Understand T H A T."
    ]
    return r.choice(fallback_phrases)
def handle_name_request(user_input,saves):
    if re.search(r"(my name is|call me)\s+([a-zA-Z ]+?)(\s+and|,|\.|$)", user_input, re.IGNORECASE):
        g = re.search(r"(my name is|call me)\s+([a-zA-Z ]+?)(\s+and|,|\.|$)", user_input, re.IGNORECASE).group(2).strip()
        saves["user_name"] = g
        return f"Hello, {saves['user_name']}."
    elif "your name" in user_input:
        return f"q v a b b y t e | Version: {version}"
    elif re.search(r"what .*my .*name|.*my .*name|what is my name|what's my name", user_input):
        if saves.get("user_name") is not None:
            return f"Your name is {saves['user_name']}"
        return f'I never caught you saying your name.'
    return ""
def handle_mood_check(user_input,saves,previous_input):
    if re.search(r"how are you", previous_input):
        if re.search(r"good|fantastic|nice", user_input):
            saves['user_feel'] = "good"
            return f"Nice to hear, how can I assist you?"
        elif re.search(r"bad|depressed|sad", user_input):
            saves['user_feel'] = "bad"
            return f"That's bad, why?"
    elif "how are you" in user_input:
        return f"I feel Pythonic. How about you?"
    return ""
def handle_help_request(user_input,saves):
    if re.search(r"help .*me|assist .*me|\bhelp", user_input):
        saves["user_want"] = "help"
        match = re.search(r"with (.+)", user_input)
        if match:
            x = match.groups()
            y = x[0].translate(str.maketrans({',': ' ', ';': ' ', ' ': ''}))
            y = y.replace('and', ' ')
            ts = y.split(" ")

            if saves.get('user_topic') is None:
                saves['user_topic'] = []  # Initialize user_topic if it doesn't exist

            # Add the new topics to user_topic if not already present
            for topic in ts:
                if topic not in saves['user_topic']:
                    saves['user_topic'].append(topic)

            return f"What specifically about {', '.join(saves['user_topic'])} do you need help with?"
        else:
            return f"What do you need help with?"
    elif re.search(r"what i want|what i need|do you understand.*want", user_input):
        if saves.get("user_want") == "help":
            if saves.get("user_topic") is not None:
                if saves.get("user_topic"):
                    return f"You need help with {', '.join(saves['user_topic'])}."
                else:
                    return "You need help with something, but I don't remember you saying what."
            else:
                return "I don't know what you want. Can you clarify?"
    return ""
def handle_greeting_check(user_input,saves):
    if re.search(r"\bhi\b|\bhello\b", user_input):
        return f"Hello. How can I assist you today?"
    return ""
def handle_math_problems(user_input,saves):
    if re.search(r"([0-9\+\-\*/\(\)\s]+)",user_input):
        match = re.search(r"([0-9\+\-\*/\(\)\s]+)", user_input)
        if match:
            math_problem = match.group(1)  # Extract the matched math expression
            if math_problem != "" and math_problem != " ":
                try:
                    # Safely evaluate the math expression
                    result = eval(math_problem)
                    return f"The answer to{math_problem} is {result}"
                except Exception as e:
                    return f"Sorry, I couldn't solve that. Error: {str(e)}"
    return ""
def process_input(user_input, saves,previous_input):
    user_input = re.sub(r"\bwhat(?:'s| is|s)?\b", "what", user_input)
    user_input = user_input.lower().strip()
    output = ""
    # Process different topics separately
    output += handle_greeting_check(user_input, saves)
    if output != "":
        output += " "
    output += handle_name_request(user_input, saves)
    if output != "":
        output += " "
    output += handle_help_request(user_input, saves)
    if output != "":
        output += " "
    output += handle_mood_check(user_input,saves,previous_input)
    if output != "":
        output += " "
    output += handle_math_problems(user_input,saves)
    return output
def qvabbyte():
    global qvabbyteVersionNameString, version
    chatbot = qvabbyteVersionNameString
    print("-------------- q v a b b y t e --------------")
    print("(Type 'bye' to exit)")
    print(f"{get_random_greeting()}")
    saves = { }
    last_input =""
    previous_input = ""
    while True:
        # User Input
        user_input = input("You: ").lower().strip()
        # Store the last and previous input
        previous_input = last_input
        last_input = user_input
        # Exit Code
        if user_input == "bye":
            print(f"{chatbot}: {get_random_bye()}")
            break
        output = process_input(user_input,saves,previous_input)
        if output != "" and output != " ":
            print(f"{chatbot}: {output}")
        else:
            print(f"{chatbot}: {handle_unknown()}")
if __name__ == "__main__":
    qvabbyte()