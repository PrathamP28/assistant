import requests
import json
import os

OLLAMA_URL = "http://localhost:11434/api/generate"
MEMORY_FILE = "memory.json"

# Load memory
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        history = json.load(f)
else:
    history = []

def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def build_prompt(user_input):
    prompt = "You are a helpful AI assistant.\n\n"

    # Use last 10 messages for context
    for msg in history[-10:]:
        prompt += f"{msg['role']}: {msg['content']}\n"

    prompt += f"User: {user_input}\nAI:"
    return prompt

def ask_ai(user_input):
    prompt = build_prompt(user_input)

    response = requests.post(OLLAMA_URL, json={
        "model": "phi3",
        "prompt": prompt,
        "keep_alive": -1,
        "stream": False
    })

    return response.json()["response"]

print("🤖 AI Assistant with Memory")
print("Type 'exit' to quit | 'clear' to reset memory\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    if user_input.lower() == "clear":
        history.clear()
        save_memory()
        print("🧹 Memory cleared\n")
        continue

    answer = ask_ai(user_input)

    print("AI:", answer, "\n")

    # Save chat
    history.append({"role": "User", "content": user_input})
    history.append({"role": "AI", "content": answer})

    save_memory()
