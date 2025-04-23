import os
import requests
import re

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
MODEL = "llama-3.3-70b-versatile"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"


HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
    #"HTTP-Referer": "http://localhost",  # Replace with your project site or GitHub if deploying
    "X-Title": "Code Review CLI Tool"
}

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_code_and_review(response_text):
    # Extract code block if present
    code_blocks = re.findall(r"```(?:python)?\s*(.*?)```", response_text, re.DOTALL)
    
    if code_blocks:
        code = code_blocks[0].strip()
        explanation = response_text.replace(code, "").replace("```", "").strip()
    else:
        lines = response_text.strip().splitlines()
        code_start = 0
        for i, line in enumerate(lines):
            if line.strip().startswith("def ") or line.strip().startswith("class "):
                code_start = i
                break
        explanation = "\n".join(lines[:code_start]).strip()
        code = "\n".join(lines[code_start:]).strip()

    return code, explanation

def review_code(code_text):
    prompt = (
        "You are a helpful code assistant. Please review the following Python code, "
        "explain the issues if any, and then output the corrected version.\n\n"
        f"```python\n{code_text}\n```"
    )
    
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()

    content = response.json()["choices"][0]["message"]["content"]
    return content

def process_code(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    print("[*] Reviewing code...")

    try:
        response_text = review_code(code)
        code_only, explanation = extract_code_and_review(response_text)

        with open(os.path.join(OUTPUT_DIR, "fixed_code.py"), "w", encoding="utf-8") as f_code:
            f_code.write(code_only)

        with open(os.path.join(OUTPUT_DIR, "review.txt"), "w", encoding="utf-8") as f_review:
            f_review.write(explanation)

        print("[✓] Code reviewed and saved to output/fixed_code.py")
        print("[✓] Explanation saved to output/review.txt")

    except Exception as e:
        print("[!] Error reviewing code:", e)

if __name__ == "__main__":
    file_to_review = "buggy_code.py"  # Replace with your actual file
    process_code(file_to_review)
