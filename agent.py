import requests
import os
import re

API_KEY = "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"
def generate_code(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI-Agent"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",  # 🔥 WORKING MODEL
        "messages": [
            {
                "role": "system",
                "content": "Return ONLY code. No explanation. Use python code blocks."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    if "choices" not in result:
        print("❌ API ERROR:", result)
        return None

    return result["choices"][0]["message"]["content"]


# 🔥 Extract code safely
def extract_code(text):
    if not text:
        return ""

    code_blocks = re.findall(r"```python(.*?)```", text, re.DOTALL)

    if code_blocks:
        return "\n\n".join(code_blocks)

    return text


def save_code(code):
    clean_code = extract_code(code)

    with open("generated_app.py", "w", encoding="utf-8") as f:
        f.write(clean_code)


import subprocess

def push_to_github():
    git_path = r"C:\Program Files\Git\mingw64\bin\git.exe"

    subprocess.run([git_path, "add", "."])
    subprocess.run([git_path, "commit", "-m", "Auto-generated code by AI agent"])
    subprocess.run([git_path, "push", "origin", "main"])


if __name__ == "__main__":
    user_input = input("🧠 What do you want to build?\n> ")

    print("\n⚡ Generating code...\n")
    code = generate_code(user_input)

    if not code:
        print("⚠️ Failed. Fix API key or model.")
        exit()

    print("💾 Saving clean code...")
    save_code(code)

    print("🚀 Pushing to GitHub...")
    push_to_github()

    print("✅ Done! Check your GitHub repo.")