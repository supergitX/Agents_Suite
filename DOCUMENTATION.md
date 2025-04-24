# Agents_Suite Documentation

🧾 **Project Overview**

This project is an automated code generation, review, testing, and optimization workflow implemented using GitHub Actions and several Python scripts.  It leverages language models (Gemini and Groq) to generate code from a prompt, review and fix code, and create test cases. The entire process is orchestrated through GitHub Actions workflows.

⚙️ **Setup & Installation Instructions**

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Linux/macOS
   .venv\Scripts\activate  # On Windows
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add the following:
   ```
   GEMINI_API_KEY=<your_gemini_api_key>
   GROQ_API_KEY=<your_groq_api_key>
   ```

🧩 **Explanation of Key Modules, Classes, and Functions**

This project relies on several Python scripts located in the `agents` directory, as well as core logic files such as `reviewed_code.py` and `buggy_code.py`.  There are no explicitly defined classes.

**Key Modules and Files:**

- **`reviewed_code.py`**: This file contains the Python function `sum_of_even_numbers()` which serves as the target for review, testing, and optimization.  The code in this file is iteratively improved.

- **`buggy_code.py`**:  A copy of initially generated code. Triggers the code review workflow.

- **`agents/code_generator.py`**: Reads a prompt from `input.txt` and uses Gemini to generate code, saving it as `generated_code/generated.py` and `buggy_code.py`.

- **`agents/reviewer.py`**: Reviews the code in `buggy_code.py` using Groq and saves the review report to the `reviews` directory.

- **`agents/optimizer.py`**: Uses Groq to analyze reviewed code in `buggy_code.py` and provide an optimized version.  It saves the output to `output/fixed_code.py` and `reviewed_code.py`, along with an explanation in `output/review.txt`.

- **`agents/tester.py`**: Generates test cases using Groq for the code in `reviewed_code.py`. It saves the generated tests to `test_reviewed_code.py`.

- **`doc-keeper.py`**: Auto-generates this documentation using Gemini and saves it as `DOCUMENTATION.md`.

- **`input.txt`**: Contains the prompt for code generation.

- **`requirements.txt`**: Lists the project dependencies.

- **`.github/workflows`**: Contains the GitHub Actions workflow files that orchestrate the entire process.



🗂 **Folder & File Structure with Descriptions**

```
.
├── agents                   # Contains the agent scripts
│   ├── code_generator.py   # Code generation agent
│   ├── optimizer.py        # Code optimization agent
│   ├── reviewer.py         # Code review agent
│   └── tester.py           # Test case generation agent
├── generated_code          # Stores the generated code
│   └── generated.py      # Generated code from prompt in input.txt
├── .github                 # GitHub Actions workflow files
│   └── workflows
│       ├── code-review.yml       # Workflow for code review
│       ├── dockeeper.yml       # Workflow for documentation generation
│       ├── generate-code.yml       # Workflow for code generation
│       ├── optimize.yml       # Workflow for code optimization
│       └── run-tests.yml       # Workflow for running tests
├── input.txt                 # Input prompt for code generation
├── logs                    # Log directory from code review
│   └── review_log.txt
├── output                  # Output directory from optimizer agent
│   ├── fixed_code.py     # Fixed code produced by the optimizer
│   └── review.txt         # Code review from the optimizer
├── reviews                 # Output directory from reviewer agent
│   ├── ...                       # Code reviews, named by timestamp
├── buggy_code.py             # The "buggy" code to be reviewed
├── doc-keeper.py            # Script to generate documentation
├── README.md                # Project README
├── requirements.txt          # Project dependencies
├── reviewed_code.py         # The most recent reviewed and optimized code
├── test_reviewed_code.py     # Output from test generation
└── test_generation.log        # Log file from test generation
```

🔧 **How to Use**

This project is designed to be used automatically through the defined GitHub Actions workflows.  The workflows are triggered by pushes to specific files or by other workflows. You can manually trigger workflows through the GitHub Actions interface.

1. **Code Generation:** Push changes to `input.txt` to trigger the `Code Generator on Prompt Input` workflow.

2. **Code Review:**  A push to `buggy_code.py` (usually created by the code generation) or completion of the `Code Generator on Prompt Input` workflow will start the `Code Review` workflow.

3. **Code Optimization:** Triggered upon successful completion of the `Code Review` workflow.  

4. **Test Generation & Execution:** The `Run Tests on Reviewed Code` workflow starts upon completion of the `Code Optimizer` workflow.

5. **Documentation Generation:**  Push to any branch or use workflow dispatch to trigger the `Generate Repository Documentation` workflow which uses the `doc-keeper.py` script to generate documentation.



🤝 **Contribution Guidelines**

While not explicitly defined in the code, contributions are welcome.  Fork the repository, make your changes, and submit a pull request.


🧪 **Testing & Debugging Instructions**

Tests are generated and run automatically using the `Run Tests on Reviewed Code` workflow.  The test results, including a detailed log, are saved in `test_generation.log`. This log includes pytest output and any errors encountered during test generation.


The provided code already has docstrings. They are not repeated here.

