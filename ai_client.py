import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "codellama:7b"

def get_ai_suggestion(code: str) -> str:
    if not code.strip():
        return (
            "No code detected.\n\n"
            "Copy code from your IDE and press Ctrl + Shift + A."
        )

    prompt = f"""
You are a strict embedded C reviewer.
RULES:
- Only review C code meant for microcontrollers.
- If the code is NOT C, respond with:
  "Error: Input is not embedded C code."
Target: STM32 HAL firmware.
Focus on:
- logical bugs
- buffer safety
- interrupt safety
- MISRA-C concerns

DO NOT review Python, networking, or desktop code.
Do not speculate beyond the code.
Keep response concise.

CODE:
{code}
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": True
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True,timeout=600)
        result = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                result += data.get("response", "")

        return result.strip()

    except requests.exceptions.ReadTimeout:
        return "Local AI is still thinking. Try smaller code blocks."

    except Exception as e:
        return f"AI communication error: {e}"
