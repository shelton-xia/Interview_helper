# Interview_helper
**A FREE tool to help generate answers**

## Why I built this with GPT
I personally think LeetCode-style coding challenges are outdated and no longer reflect what makes a great engineer today. But if you feel the same, we should try to push for change rather than trying to make money from it.

**Besides, it's not hard to build, it took me one night with GPT's help. It's easy to try something with AI today.**

To those who are interested: If you need this — and I believe since you found this, you will install it, try it — you already have the potential to be or already are a great engineer. This could be a good start for you to become a better engineer or to feel how LLMs will change our lives.

Welcome to commit or try!

By Shelton

# GPT-4 Screenshot Solver

A Python tool to capture a screenshot of a coding problem from a second monitor and get a detailed solution from GPT-4.

## Features
- Take a screenshot of coding problems from a second monitor.
- Send image to GPT-4 for step-by-step coding solutions.
- Auto-format response with explanations and test cases.

## Installation

1. **Clone this repo or download `screenshot_solver_windows.py` or open ``screenshot_solver_windows.ipynb` in your Jupyter.**
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Replace 'YOUR_API_KEY_HERE' with your actual OpenAI API key or set as environment variable in line 38
   ```bash
   OPENAI_API_KEY = 'YOUR_API_KEY_HERE'
   ```
## Usage
  ```bash
  python -m screenshot_solver_windows.main
  ```
Press F2 to take a screenshot and get a solution.
Press ESC to exit.
