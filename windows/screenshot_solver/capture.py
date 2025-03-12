import mss
import mss.tools

def capture_screenshot_from_second_monitor(output_path='screenshot.png'):
    """
    Capture a screenshot from the second monitor and save it as an image.
    """
    with mss.mss() as sct:
        monitors = sct.monitors
        if len(monitors) < 2:
            print("Second monitor not found!")
            return None

        second_monitor = monitors[2]
        screenshot = sct.grab(second_monitor)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=output_path)
        return output_path
