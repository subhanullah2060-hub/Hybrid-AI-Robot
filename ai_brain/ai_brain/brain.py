
def think(user_input):
    if "hello" in user_input.lower():
        return "Hello human 👋"

    elif "your name" in user_input.lower():
        return "I am a Hybrid AI Robot"

    elif "move" in user_input.lower():
        return "COMMAND:MOVE"

    elif "stop" in user_input.lower():
        return "COMMAND:STOP"

    else:
        return "I am learning..."
