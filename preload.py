import requests
import time

OLLAMA_URL = "http://localhost:11434/api/generate"

def wait_for_ollama():
    print("⏳ Waiting for Ollama...")
    while True:
        try:
            requests.get("http://localhost:11434")
            break
        except:
            time.sleep(1)

def preload():
    print("🔄 Preloading AI model...")

    requests.post(OLLAMA_URL, json={
        "model": "phi3",
        "prompt": "Initialize system",
        "keep_alive": -1,
        "stream": False
    })

    print("✅ AI READY (instant mode ON)")

if __name__ == "__main__":
    wait_for_ollama()
    preload()
