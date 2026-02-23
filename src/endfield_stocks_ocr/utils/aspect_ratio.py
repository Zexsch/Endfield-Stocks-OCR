import math

import pyautogui
import toml

from endfield_ocr_core.config.config import Config

from endfield_stocks_ocr.utils.package_dirs import PackageDirs
from endfield_stocks_ocr.utils.logger import EndfieldLogger


def check_aspect_ratio(args: Config):
    """Checks the aspect ratio of the Monitor and adjusts screenshot region"""
    width, height = pyautogui.size()
    gcd = math.gcd(width, height)

    ratio_width = width // gcd
    ratio_height = height // gcd

    if ratio_width == 16 and ratio_height == 9:
        return

    logger = EndfieldLogger(debug=args.debug).get_logger()

    logger.info(f"Found different aspect ratio: {ratio_width}:{ratio_height}")

    dirs = PackageDirs()

    with dirs.default_config.open("r", encoding="utf-8") as f:
        config = toml.load(f)

    if config["flags"]["aspect_ratio"]:
        return

    for region in config["regions"]:
        bbox = config[f"bounding_box_{region}"]
        bbox["x_percent"] = (bbox["x_percent"] / 16) * ratio_width
        bbox["y_percent"] = (bbox["y_percent"] / 9) * ratio_height
        bbox["width_percent"] = (bbox["width_percent"] / 16) * ratio_width
        bbox["height_percent"] = (bbox["height_percent"] / 9) * ratio_height

    config["flags"]["aspect_ratio"] = True

    with dirs.user_config.open("w", encoding="utf-8") as f:
        toml.dump(config, f)
