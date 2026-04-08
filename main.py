import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ai(question):
    response = requests.post(OLLAMA_URL, json={
        "model": "phi3",
        "prompt": f"You are a helpful assistant.\nUser: {question}",
        "keep_alive": -1,
        "stream": False
    })
    return response.json()["response"]

print("🤖 AI Assistant Ready (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    answer = ask_ai(user_input)
    print("AI:", answer, "\n")
