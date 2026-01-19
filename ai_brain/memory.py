def save_to_memory(text):
    with open("ai_brain/memory.txt", "a") as file:
        file.write(text + "\n")
