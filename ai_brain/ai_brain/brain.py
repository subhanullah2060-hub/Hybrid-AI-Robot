def think(user_input):
    text = user_input.lower()

    if "hello" in text:
        return "Hello human 👋"

    if "your name" in text:
        return "I am a Hybrid AI Robot"

    if "move" in text:
        return "COMMAND:MOVE"

    if "stop" in text:
        return "COMMAND:STOP"

    return "I am learning..."
