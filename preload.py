import requests
import time

OLLAMA_URL = "http://localhost:11434/api/generate"

def wait_for_ollama():
    print("⏳ Waiting for Ollama to start...")
    while True:
        try:
            requests.get("http://localhost:11434")
            break
        except:
            time.sleep(1)

def preload():
    print("🔄 Preloading AI model into RAM...")

    requests.post(OLLAMA_URL, json={
        "model": "gemma:2b",
        "prompt": "Initialize system",
        "keep_alive": -1,
        "stream": False
    })

    print("✅ AI READY (instant response mode ON)")

if __name__ == "__main__":
    wait_for_ollama()
    preload()
