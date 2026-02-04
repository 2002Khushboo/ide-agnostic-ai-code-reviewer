import requests
import json

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "codellama:7b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json()["response"]

if __name__ == "__main__":
    reply = ask_ollama("Review this C code:\nint *p;")
    print(reply)
