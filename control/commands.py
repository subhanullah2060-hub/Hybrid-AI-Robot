def execute(command):
    if command == "COMMAND:MOVE":
        return "🟢 Robot moving forward"

    elif command == "COMMAND:STOP":
        return "🔴 Robot stopped"

    else:
        return None
