from pathlib import Path

import pytesseract
from PIL import Image


def test():
    image_dir = Path(__file__).parent.parent / "data/image"
    test_img = image_dir / "image.png"

    img = Image.open(str(test_img))

    print(pytesseract.image_to_string(img))
