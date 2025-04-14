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

    name_pattern = re.compile(r'(name is|call me)\s+(\w+)', re.I)
    if name_pattern.search(user_input):
        g = name_pattern.search(user_input).group(2).strip()
    # if re.search(r"(my name is|call me)\s+([a-zA-Z ]+?)(\s+and|,|\.|$)", user_input, re.IGNORECASE):
    #     g = re.search(r"(my name is|call me)\s+([a-zA-Z ]+?)(\s+and|,|\.|$)", user_input, re.IGNORECASE).group(2).strip()
        saves["user_name"] = g
        return f"Hello, {saves['user_name']}."
    elif "your name" in user_input:
        return f"q v a b b y t e | Version: {version}"
    elif re.search(r"^what .*my .*name|.*my .*name|what is my name|what's my name", user_input):
        if saves.get("user_name") is not None:
            return f"Your name is {saves['user_name']}"
        return f'I never caught you saying your name.'
    return ""
def handle_mood_check(user_input,saves,previous_input,moodLevels):
    if re.search(r"how are you", previous_input):
        if re.search(r"good|fantastic|nice", user_input):
            saves['user_feel'] = "good"
            moodLevels['happy'] += 1
            return f"Nice to hear, how can I assist you?"
        elif re.search(r"bad|depressed|sad", user_input):
            saves['user_feel'] = "bad"
            moodLevels['sad'] += 1

            return f"That's bad, why?"
    elif "how are you" in user_input:
        return f"I feel Pythonic. How about you?"
    return ""
def handle_help_request(user_input,saves):
    if re.search(r"^help .*me|assist .*me|\bhelp", user_input):
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
    #old ([0-9\+\-\*/\(\)\s]+)
    if re.search(r"\b(\d+[\s\d\.\+\-\*\/\(\)]+)\b",user_input):
        match = re.search(r"\b(\d+[\s\d\.\+\-\*\/\(\)]+)\b", user_input)
        if match:
            math_problem = match.group(1)  # Extract the matched math expression
            if math_problem != "" and math_problem != " ":
                try:
                    # Safely evaluate the math expression
                    result = eval(math_problem)
                    return f"The answer to {math_problem} is {result}"
                except Exception as e:
                    return f"Sorry, I couldn't solve that. Error: {str(e)}"
    return ""

# def handle_user_understanding(user_input,saves):

def process_input(user_input, saves,previous_input,moodLevels):
    user_input = re.sub(r"\bwhat(?:'s| is|s)?\b", "what", user_input)
    user_input = user_input.lower().strip()
    output = ""
    # Process different topics separately
    action = ""

    output += handle_greeting_check(user_input, saves)
    output_greeting = handle_greeting_check(user_input, saves)
    if output != "":
        output += " "

    output += handle_name_request(user_input, saves)
    output_name = handle_name_request(user_input, saves)
    if output != "":
        output += " "

    output += handle_help_request(user_input, saves)
    output_help = handle_help_request(user_input, saves)
    if output != "":
        output += " "

    output += handle_mood_check(user_input,saves,previous_input,moodLevels)
    output_mood = handle_mood_check(user_input,saves,previous_input,moodLevels)

    if output != "":
        output += " "

    output += handle_math_problems(user_input,saves)
    output_math = handle_math_problems(user_input,saves)

    if output_greeting !="":
        action += "greeted,"
    if output_name !="":
        action += "name_related,"
    if output_math !="":
        action += "math_related"
    if output_help !="":
        action += "help_related,"
    if output_mood !="":
        action += "mood_check,"
    saves['last_action'] = action

    return output
def qvabbyte():
    global qvabbyteVersionNameString, version
    chatbot = qvabbyteVersionNameString
    print("-------------- q v a b b y t e --------------")
    print("(Type 'bye' to exit)")
    print(f"{get_random_greeting()}")
    moodLevels = {
        'sad':0,
        'happy':0,
        'angry':0,
        'confused':0
    }
    saves = {
        'user_name': None,
        'topics': [],
        'mood_history': [],
        'last_action': None,
        'last_action_bot_unknown': False,
        'bot_unknown_streak':0,
        'user_input_history':[]
    }
    last_input =""
    previous_input = ""
    saved_inputs = []
    while True:
        # User Input
        user_input = input("You: ").lower().strip()
        #save every input.
        saved_inputs.append(user_input)

        saves['user_input_history'].append(user_input)

        # Store the last and previous input
        if saves['bot_unknown_streak'] == 0:
            previous_input = last_input
        else:
            previous_input = saves['user_input_history'][ (len(saves['user_input_history']) - saves["bot_unknown_streak"] - 2 )]
        last_input = user_input
        # Exit Code
        if user_input == "bye":
            print(f"{chatbot}: {get_random_bye()}")
            break
        # if saves["last_action_bot_unknown"]:
        #     user_input = saves['user_input_history']
        output = process_input(user_input,saves,previous_input,moodLevels)
        if output != "" and output != " ":
            print(f"{chatbot}: {output}")
            saves["last_action_bot_unknown"] = False
            saves["bot_unknown_streak"] = 0
        else:
            print(f"{chatbot}: {handle_unknown()}")
            saves["last_action_bot_unknown"] = True
            saves["bot_unknown_streak"] += 1

if __name__ == "__main__":
    qvabbyte()