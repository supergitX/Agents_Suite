import argparse
import os
import datetime
import requests

# Load API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    log_message("Error: GROQ_API_KEY environment variable is not set.")
    exit(1)

# Groq model and endpoint
MODEL = "deepseek-r1-distill-llama-70b"  # Corrected to a real model variant
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}

def log_message(message):
    """Logs a message with timestamp to log file and prints it."""
    log_folder = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, "review_log.txt")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")

def read_code_from_file(file_path):
    """Reads and returns the code content from the specified file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()
        log_message(f"Successfully read code from: {file_path}")
        return code if code.strip() else None
    except Exception as e:
        log_message(f"Failed to read file: {e}")
        return None

def review_code(code_content):
    """Sends code to Groq API and returns the code review report."""
    system_prompt = (
        "You are an expert code reviewer. Carefully check for linting errors, boundary conditions, "
        "runtime risks, and missing try-except blocks. Generate a verbose report with feedback on code quality, "
        "robustness, and specific problematic areas. "
        "Start with 'Code Review Report by supergit_reviewer:' and end with 'End of Review Report'."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Please review the following code:\n\n```python\n{code_content}\n```"}
    ]

    payload = {"model": MODEL, "messages": messages}
    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        log_message("Review received successfully.")
        return content
    except Exception as e:
        log_message(f"Failed to get review: {e}")
        return "Error in code review process."

def save_review(review_text, original_file):
    """Saves the review report to a file in the reviews folder."""
    reviews_folder = os.path.join(os.getcwd(), "reviews")
    os.makedirs(reviews_folder, exist_ok=True)
    name_without_ext = os.path.splitext(os.path.basename(original_file))[0]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    review_file_path = os.path.join(reviews_folder, f"{name_without_ext}_review_{timestamp}.txt")

    try:
        with open(review_file_path, "w", encoding="utf-8") as f:
            f.write(review_text)
        log_message(f"Review saved at: {review_file_path}")
        return review_file_path
    except Exception as e:
        log_message(f"Failed to save review: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Code Reviewer using supergit reviewer via Groq API.")
    parser.add_argument('--file', '-f', type=str, required=True, help='Path to the code file to review')
    args = parser.parse_args()

    log_message("Starting code review job.")
    code = read_code_from_file(args.file)

    if code:
        review = review_code(code)
        save_review(review, args.file)
    else:
        log_message("No code content to review.")

    log_message("Code review job completed.")

if __name__ == "__main__":
    main()
