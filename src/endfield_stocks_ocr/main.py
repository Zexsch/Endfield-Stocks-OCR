import argparse

from endfield_ocr_core.models.config import Region, Config

from endfield_stocks_ocr.ocr.get_values import get_values
from endfield_stocks_ocr.utils.aspect_ratio import check_aspect_ratio


def main():
    check_aspect_ratio()

    parser = argparse.ArgumentParser()
    parser.add_argument("--wuling", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    config = Config()

    if args.wuling:
        config.region = Region.WULING

    if args.debug:
        config.debug = True

    get_values(config)
