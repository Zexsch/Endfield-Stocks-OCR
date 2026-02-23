from datetime import datetime

import pyautogui
from endfield_ocr_core.get_ocr_values import get_ocr_values
from endfield_ocr_core.models.config import Config, Region
from endfield_ocr_core.crop_image import crop_image

from endfield_stocks_ocr.utils.package_dirs import PackageDirs


def get_values(args: Config):
    region = args.region.value

    img = pyautogui.screenshot()

    rows, cols = 0, 0

    if region == Region.WULING.value:
        rows = 1
        cols = 4

    if region == Region.VALLEY.value:
        rows = 2
        cols = 7

    crop_bbox = crop_image(img)

    cropped_img = pyautogui.screenshot(
        region=(crop_bbox.x, crop_bbox.y, crop_bbox.width, crop_bbox.height)
    )

    if args.debug:
        dirs = PackageDirs()

        img_path = dirs.debug_files / "Data"
        img_path.mkdir(parents=True, exist_ok=True)

        now = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        img_path_uncropped = img_path / f"{args.region.value}_{now}.png"
        img_path_cropped = img_path / f"{args.region.value}_cropped_{now}.png"

        img.save(str(img_path_uncropped))
        cropped_img.save(str(img_path_cropped))

    text = get_ocr_values(
        cropped_img, rows=rows, cols=cols, region=region, debug_files=args.debug
    )

    for key, value in text.items():
        if value > 6000:
            text[key] = 0

    print(text)
