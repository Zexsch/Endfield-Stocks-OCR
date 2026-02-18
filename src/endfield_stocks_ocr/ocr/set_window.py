from pathlib import Path

import pyautogui
from endfield_stocks_ocr.ocr.bounding_box import BoundingBoxHandler

def main():
    print("Move mouse to the TOP LEFT corner of the area and wait 3 seconds...")
    pyautogui.sleep(3)
    x1, y1 = pyautogui.position()

    print("Move mouse to the BOTTOM RIGHT corner of the area and wait 3 seconds...")
    pyautogui.sleep(3)
    x2, y2 = pyautogui.position()

    screen_width, screen_height = pyautogui.size()
    
    handler = BoundingBoxHandler()
    handler.set_user_bounding_box(x1 / screen_width, y1 / screen_height, x2 / screen_width, y2 / screen_height)

    relative_box = (x1 / screen_width, y1 / screen_height, x2 / screen_width, y2 / screen_height)
    print(f"Set bounding box to {relative_box}" )
    
if __name__ == '__main__':
    main()