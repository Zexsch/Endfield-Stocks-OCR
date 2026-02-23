import argparse

from endfield_ocr_core import Region, Config

from endfield_stocks_ocr import get_values_manual
from endfield_stocks_ocr import get_values
from endfield_stocks_ocr import check_aspect_ratio
from endfield_stocks_ocr import EndfieldLogger


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wuling", action="store_true")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--manual", action="store_true")
    args = parser.parse_args()
    config = Config()

    logger = EndfieldLogger(debug=config.debug).get_logger()
    logger.debug(f"Starting OCR Scan with args {config}")

    if args.wuling:
        config.region = Region.WULING

    if args.debug:
        config.debug = True

    if args.manual:
        config.manual = True

    check_aspect_ratio(config)

    if config.manual:
        get_values_manual(config)
    else:
        get_values(config)
