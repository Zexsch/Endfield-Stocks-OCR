from dataclasses import asdict
from pathlib import Path

import pyautogui
from endfield_ocr_core.get_number import get_number

from endfield_stocks_ocr.ocr.bounding_box import BoundingBoxHandler

def get_values(region: str, debug: bool):
    handler = BoundingBoxHandler(region=region)

    relative_box = list(asdict(handler.config).values())

    screen_width, screen_height = pyautogui.size()

    left = int(screen_width * relative_box[0])
    top = int(screen_height * relative_box[1])
    right = int(screen_width * relative_box[2])
    bottom = int(screen_height * relative_box[3])

    img = pyautogui.screenshot(region=(left, top, right - left, bottom - top))
    img_path = Path(__file__).parent.parent / 'data/latest_image.png'
    img.save(str(img_path))
    
    if region == "wuling":
        rows = 1
        cols = 4
    else:
        rows = 2
        cols = 7
    
    text = get_number(img, rows=rows, cols=cols, region=region, debug_files=debug)
    print(text)