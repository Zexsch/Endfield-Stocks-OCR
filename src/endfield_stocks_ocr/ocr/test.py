from pathlib import Path
from dataclasses import asdict
import random
import string
from datetime import datetime

import pytesseract
import pyautogui
from PIL import Image

from endfield_stocks_ocr.ocr.bounding_box import BoundingBoxHandler

def test():
    image_dir = Path(__file__).parent.parent / "data/image"
    handler = BoundingBoxHandler()
    
    relative_box = list(asdict(handler.config).values())
    
    screen_width, screen_height = pyautogui.size()
    
    left = int(screen_width * relative_box[0])
    top = int(screen_height * relative_box[1])
    right = int(screen_width * relative_box[2])
    bottom = int(screen_height * relative_box[3])
    
    screenshot = pyautogui.screenshot(region=(left, top, right-left, bottom-top))
    
    now = datetime.now().strftime('%Y_%m_%d_%H%M%S_')
    identifier = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    
    image_name = now + identifier + '.png'
    print(image_name)
    
    image_path = image_dir / image_name
    print(str(image_path))
    
    screenshot.save(str(image_path))
