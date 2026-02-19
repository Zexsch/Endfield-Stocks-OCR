import math
from importlib import resources
from pathlib import Path

import pyautogui
import toml


def check_aspect_ratio():
    width, height = pyautogui.size()
    gcd = math.gcd(width, height)

    ratio_width = width // gcd
    ratio_height = height // gcd

    if ratio_width == 16 and ratio_height == 9:
        return

    config_dir = Path(__file__).parent / "config/default_config.toml"

    with resources.open_text("endfield_stocks_ocr.config", str(config_dir)) as f:
        config = toml.load(f)

    for region in config["regions"]:
        bbox = config[f"bounding_box_{region}"]
        bbox["x_percent"] = (bbox["x_percent"] / 16) * ratio_width
        bbox["y_percent"] = (bbox["y_percent"] / 9) * ratio_height
        bbox["width_percent"] = (bbox["width_percent"] / 16) * ratio_width
        bbox["height_percent"] = (bbox["height_percent"] / 9) * ratio_height

    with config_dir.open("w") as f:
        toml.dump(config, f)
