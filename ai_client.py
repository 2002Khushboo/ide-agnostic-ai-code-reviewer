'''
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_ai_suggestion(code):
    prompt = f"""
You are a senior software engineer.
Review the following code and suggest improvements or point out issues.
Do not rewrite unless necessary.

CODE:
{code}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
'''
'''
def get_ai_suggestion(code: str) -> str:
    if not code.strip():
        return "No code detected. Please copy some code first."

    lines = code.splitlines()
    feedback = []

    feedback.append("Code Review (Mock AI)\n")

    if len(lines) > 50:
        feedback.append("- This function/file is quite long. Consider splitting it.")

    if "malloc" in code and "free" not in code:
        feedback.append("- Possible memory leak: malloc used without free.")

    if "printf" in code:
        feedback.append("- Debug print statements found. Remove for production.")

    if "TODO" in code:
        feedback.append("- TODO comments present. Make sure they are resolved.")

    feedback.append("\nGeneral Suggestion:")
    feedback.append("- Add comments for complex logic.")
    feedback.append("- Follow consistent naming conventions.")

    return "\n".join(feedback)
'''

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
