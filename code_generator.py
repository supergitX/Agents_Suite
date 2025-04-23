import os
import datetime
import re
from pathlib import Path
import google.generativeai as genai

# Directory where the generated code will be saved
OUTPUT_DIR = Path("generated_code")
OUTPUT_DIR.mkdir(exist_ok=True)

# Gemini API setup: API key provided via GitHub Secrets as environment variable 'GEMINI_API_KEY'
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY environment variable not set.")
genai.configure(api_key=api_key)

def read_prompt_from_file(file_path="input.txt") -> str:
    """Reads the plain-text prompt from a .txt file."""
    if not os.path.exists(file_path):
        print("⚠️ input.txt not found. Using fallback prompt.")
        return "Write a Python function to sort a list."

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def generate_code_from_prompt(prompt: str) -> str:
    """Generates code using Gemini based on the provided prompt."""
    directive = (
        "You are a code generation assistant. "
        "When responding, output only the requested code snippet without any additional explanation or commentary."
    )
    full_prompt = f"{directive}\n{prompt}"
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(full_prompt)
    text = response.text.strip()

    # Remove markdown code fences if present
    fence_match = re.search(r"```(?:python)?\n([\s\S]*?)```", text)
    return fence_match.group(1).strip() if fence_match else text

def main():
    prompt = read_prompt_from_file("input.txt")
    generated_code = generate_code_from_prompt(prompt)
    #timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / "generated.py"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(generated_code)

    with open("buggy_code", "w", encoding="utf-8") as f_main:
            f_main.write(generated_code)

    print(f"✅ Code generated and saved to {output_file}")
    print("Code also saved as buggy_code in main")

if __name__ == "__main__":
    main()
