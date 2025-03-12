import keyboard
from .capture import capture_screenshot_from_second_monitor
from .gpt_client import query_gpt4

def run():
    print("Press F3 to take a screenshot and get solution from GPT-4. Press ESC to exit.")

    while True:
        if keyboard.is_pressed('F3'):
            image_path = capture_screenshot_from_second_monitor()
            if image_path:
                print("Screenshot saved as 'screenshot.png'")
                response = query_gpt4(image_path)
                print("\nGPT-4 Response:\n")
                print(response)
            break
        elif keyboard.is_pressed('esc'):
            print("Exiting program.")
            break

if __name__ == "__main__":
    run()
