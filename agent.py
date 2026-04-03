import requests
import os
import re
import subprocess
from dotenv import load_dotenv

# 🔐 Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")


# 🔥 Generate code from AI
def generate_code(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI-Agent"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "Return ONLY code. No explanation."
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


# 🔥 Extract code blocks
def extract_code(text):
    if not text:
        return ""

    # ✅ Extract code inside ``` blocks
    code_blocks = re.findall(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)

    if code_blocks:
        return "\n\n".join(code_blocks).strip()

    # ✅ Fallback: remove markdown-like text
    cleaned = text.strip()

    # Remove common unwanted lines
    if cleaned.lower().startswith("here is") or "code" in cleaned.lower():
        return ""

    return cleaned 
# 🔥 Detect file type
def detect_file_extension(code, prompt):
    prompt_lower = prompt.lower()

    if "vb.net" in prompt_lower or "vb" in prompt_lower:
        return ".vb"
    elif "html" in prompt_lower:
        return ".html"
    elif "css" in prompt_lower:
        return ".css"
    elif "javascript" in prompt_lower or "js" in prompt_lower:
        return ".js"
    else:
        return ".py"


# 💾 Save code
def save_code(code, prompt):
    clean_code = extract_code(code)

    extension = detect_file_extension(clean_code, prompt)
    filename = "generated_app" + extension

    with open(filename, "w", encoding="utf-8") as f:
        f.write(clean_code)

    print(f"✅ Saved as {filename}")


# 🚀 Push to GitHub
def push_to_github():
    git_path = r"C:\Program Files\Git\mingw64\bin\git.exe"

    subprocess.run([git_path, "add", "."])
    subprocess.run([git_path, "commit", "-m", "Auto-generated code by AI agent"])
    subprocess.run([git_path, "push", "origin", "main"])


# 🧠 MAIN
if __name__ == "__main__":
    user_input = input("🧠 What do you want to build?\n> ")

    print("\n⚡ Generating code...\n")
    code = generate_code(user_input)

    if not code:
        print("⚠️ Failed. Check API key.")
        exit()

    print("💾 Saving clean code...")
    save_code(code, user_input)

    print("🚀 Pushing to GitHub...")
    push_to_github()

    print("✅ Done! Check your GitHub repo.")