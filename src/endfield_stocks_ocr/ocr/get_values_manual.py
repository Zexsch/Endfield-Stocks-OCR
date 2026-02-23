from dataclasses import asdict
from datetime import datetime

import pyautogui
from endfield_ocr_core import get_ocr_values
from endfield_ocr_core import Config, Region

from endfield_stocks_ocr import BoundingBoxHandler
from endfield_stocks_ocr import PackageDirs
from endfield_stocks_ocr import EndfieldLogger


def get_values_manual(args: Config):
    logger = EndfieldLogger(debug=args.debug).get_logger()

    region = args.region.value
    handler = BoundingBoxHandler(region=region)

    relative_box = list(asdict(handler.config).values())

    screen_width, screen_height = pyautogui.size()

    left = int(screen_width * relative_box[0])
    top = int(screen_height * relative_box[1])
    right = int(screen_width * relative_box[2])
    bottom = int(screen_height * relative_box[3])

    logger.debug(
        f"Taking screenshot of region: {left, top, right - left, bottom - top}"
    )
    img = pyautogui.screenshot(region=(left, top, right - left, bottom - top))

    if args.debug:
        dirs = PackageDirs()

        img_path = dirs.debug_files / "Data"
        img_path.mkdir(parents=True, exist_ok=True)

        now = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        img_path = img_path / f"{args.region.value}_{now}.png"

        img.save(str(img_path))

    rows, cols = 0, 0

    if region == Region.WULING.value:
        rows = 1
        cols = 4

    if region == Region.VALLEY.value:
        rows = 2
        cols = 7

    text = get_ocr_values(
        img, rows=rows, cols=cols, region=region, debug_files=args.debug
    )
    print(text)
