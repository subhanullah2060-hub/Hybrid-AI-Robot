print("🤖 Hybrid AI Robot Online")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("AI Robot: Shutting down")
        break

    elif "hello" in user.lower():
        print("AI Robot: Hello human 👋")

    elif "move" in user.lower():
        print("AI Robot: Command received → MOVE")

    else:
        print("AI Robot: I am learning...")
