# Agents Suite Project Documentation

## 🧾 Project Overview

This project demonstrates an automated code generation, review, optimization, and testing workflow using Python, several LLMs via APIs (Gemini, Groq), and GitHub Actions.  A user provides a prompt in `input.txt`, code is generated, reviewed, fixed, and finally tested.  The entire process is managed through GitHub Actions workflows.  Documentation is also auto-generated.

## ⚙️ Setup & Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   ```

3. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate  # On Linux/macOS
   .venv\Scripts\activate  # On Windows
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up API keys:**
    - Create a `.env` file in the root directory.
    - Add the following environment variables, replacing placeholders with your actual keys:
        ```
        GEMINI_API_KEY=<your_gemini_api_key>
        GROQ_API_KEY=<your_groq_api_key>
        ```

## 🧩 Explanation of Key Modules, Classes, and Functions

This project primarily uses functions organized within different Python files, orchestrated by GitHub actions.  There are no custom classes.

### `agents/code_generator.py`

- `read_prompt_from_file(file_path="input.txt") -> str`: Reads the prompt from `input.txt`. Returns a default prompt if the file is not found.
- `generate_code_from_prompt(prompt: str) -> str`: Sends the prompt to the Gemini API and returns the generated code. Cleans up markdown code fences if present.
- `main()`: Orchestrates the code generation process, saving the output to `generated_code/generated.py` and `buggy_code.py`.

### `agents/reviewer.py`

- `log_message(message)`: Logs a message with a timestamp to a log file and prints it to the console.
- `read_code_from_file(file_path)`: Reads and returns code content from a file. Handles file reading errors.
- `review_code(code_content)`: Sends code to the Groq API for review and returns the review report.
- `save_review(review_text, original_file)`: Saves the review to a file. (Incomplete in the provided codebase).

### `agents/optimizer.py`

- `extract_code_and_review(response_text)`: Extracts code and explanation from LLM response.
- `review_code(code_text)`:  Sends code to Groq API for review and potential fixes.
- `process_code(file_path)`: Reads, reviews, and saves the fixed code and review explanation.  Writes output to `output/fixed_code.py`, `output/review.txt`, and `reviewed_code.py`.


### `agents/tester.py`

- Sets up logging to `test_generation.log`.
- Loads the Groq API key.
- Reads code from `reviewed_code.py`.
- Sends the code to the Groq API to generate pytest test cases.
- Saves the generated tests to `test_reviewed_code.py`.

### `reviewed_code.py`

- `sum_of_even_numbers(numbers: list[int]) -> int`: Calculates the sum of even numbers in a list. Includes type hints and error handling.

### `buggy_code.py`

- `sum_of_even_numbers(numbers)`:  A potentially buggy version of the `sum_of_even_numbers` function.  Used as input to the review/fix process.

### `doc-keeper.py` (Incomplete)

- Designed to generate documentation for the repository using the Gemini API.  The provided code is incomplete.



## 🗂 Folder & File Structure with Descriptions

```
.
├── agents                    # Contains agent scripts for code generation, review, optimization, and testing
│   ├── code_generator.py
│   ├── optimizer.py
│   ├── reviewer.py
│   └── tester.py
├── .github                  # GitHub Actions workflow files
│   └── workflows
│       ├── code-review.yml      # Workflow for code review using Groq
│       ├── dockeeper.yml        # Workflow for documentation generation
│       ├── generate-code.yml    # Workflow for code generation
│       ├── optimize.yml         # Workflow for code optimization (fixing)
│       └── run-tests.yml       # Workflow for running tests
├── generated_code           # Output directory for generated code
│   └── generated.py
├── input.txt                # Input prompt for code generation
├── output                   # Output directory for reviewed and fixed code
│   ├── fixed_code.py
│   └── review.txt
├── buggy_code.py           # Buggy code to be reviewed (overwritten by generated code)
├── reviewed_code.py         # Reviewed and fixed code
├── requirements.txt         # Project dependencies
├── README.md                 # Project README file
├── test_reviewed_code.py      # pytest cases for reviewed code
└── test_generation.log        # log output from test generation


```

## 🔧 How to Use

The primary interaction with this project is through the `input.txt` file and the GitHub Actions workflows.

1. **Modify `input.txt`:**  Write a clear and concise prompt describing the code you want to generate.

2. **Commit and Push:**  Committing and pushing `input.txt` to the `main` branch will trigger the following workflows:

    - **Code Generator on Prompt Input:** Generates code based on `input.txt` and commits it as `buggy_code.py`.
    - **Code Review:** Reviews the generated code using Groq and saves the review to `reviews/`.
    - **Code Optimizer:** Fixes the code based on the review and commits the fixed code to `output/` and `reviewed_code.py`.
    - **Run Tests on Reviewed Code:** Generates and runs tests for the reviewed code using Groq and `pytest`, and commits results to `test` branch.
    - **Generate Repository Documentation:** Regenerates this documentation file. (Incomplete)



## 🧪 Testing & Debugging Instructions


Test cases are generated automatically by the `agents/tester.py` script and placed in `test_reviewed_code.py`. You can run these tests locally using `pytest`:

```bash
pytest test_reviewed_code.py -v  # -v for verbose output
```

The test generation process is logged in  `test_generation.log`.



## 🤝 Contribution Guidelines (Not Applicable for this automated example)

N/A  (This example focuses on automated workflows.  A real project would include contribution details here)



##  Missing Pieces in the provided codebase

*   The `doc-keeper.py` script is incomplete and does not fully generate documentation.
*   The `agents/reviewer.py` file's `save_review()` function is also incomplete.


This documentation provides a comprehensive guide to the provided project, covering its key components, functionality, and usage. Remember to set up your API keys correctly and follow the instructions to trigger the automated workflows.