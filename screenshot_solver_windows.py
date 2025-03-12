"""
GPT-4 Screenshot Coding Solver
------------------------------
A simple Python tool to capture a screenshot from the second monitor and automatically get a coding solution using GPT-4 Vision (gpt-4o).

Features:
- Capture a screenshot of coding problems from the second monitor.
- Send image directly to GPT-4 for AI-generated solutions.
- Display result directly in terminal.

Dependencies:
- pyautogui
- keyboard
- openai
- mss
- requests

Install dependencies:
pip install pyautogui keyboard openai mss requests

Usage:
1. Set your OpenAI API key (replace 'YOUR_API_KEY_HERE').
2. Run the script:
   python gpt4_screenshot_solver.py
3. Press F3 to take a screenshot and get solution.
4. Press ESC to exit.

"""

import pyautogui
import keyboard
import openai
import mss
import mss.tools
import requests
import base64
import os

# --------------------------- Configuration --------------------------- #

# Replace 'YOUR_API_KEY_HERE' with your actual OpenAI API key or set as environment variable
OPENAI_API_KEY = os.getenv('YOUR_API_KEY_HERE')

# GPT-4 Vision model (gpt-4o or other available models)
OPENAI_MODEL = "gpt-4o"

# --------------------------------------------------------------------- #


def capture_screenshot(output_path='screenshot.png'):
    """
    Capture a screenshot from the second monitor and save it.
    """
    with mss.mss() as sct:
        monitors = sct.monitors
        if len(monitors) < 2:
            print("[Error] Second monitor not detected!")
            return None

        second_monitor = monitors[2]  # Second monitor is index 2 in mss
        screenshot = sct.grab(second_monitor)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=output_path)
        print(f"[Info] Screenshot saved as {output_path}")
        return output_path


def encode_image(image_path):
    """
    Encode image file to base64 for API usage.
    """
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except FileNotFoundError:
        print("[Error] Screenshot file not found.")
        return None


def query_gpt4_with_image(encoded_image):
    """
    Send the encoded image to GPT-4 Vision and get the solution.
    """
    if OPENAI_API_KEY == 'YOUR_API_KEY_HERE':
        print("[Error] Please set your OpenAI API key in the script or via environment variable.")
        return

    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a Python expert helping with coding problems."},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "This is a screenshot of a coding problem. Please provide:\n"
                                "1. The most optimized solution with clear explanation and time complexity.\n"
                                "2. A solution without any external package, explained line by line.\n"
                                "Ensure clear, well-commented code and run through a sample test case."
                            )
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=2000
        )

        answer = response.choices[0].message.content
        return answer

    except Exception as e:
        print(f"[Error] Failed to get response from GPT-4: {e}")
        return None


def main():
    print("\n====== GPT-4 Screenshot Coding Solver ======\n")
    print("Press F2 to take a screenshot of the second monitor and get a solution.")
    print("Press ESC to exit the program.\n")

    while True:
        if keyboard.is_pressed('F2'):
            print("[Info] Taking screenshot...")
            image_path = capture_screenshot()
            if image_path:
                encoded_image = encode_image(image_path)
                if encoded_image:
                    print("[Info] Querying GPT-4 for solution. Please wait...")
                    response = query_gpt4_with_image(encoded_image)
                    if response:
                        print("\n====== GPT-4 Response ======\n")
                        print(response)
                        print("\n============================\n")
            print("Press F3 to take another screenshot, or ESC to exit.\n")

        elif keyboard.is_pressed('esc'):
            print("[Info] Exiting program.")
            break


if __name__ == "__main__":
    main()
