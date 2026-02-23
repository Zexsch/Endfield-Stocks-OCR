import argparse

from endfield_ocr_core.config.config import Region, Config

from endfield_stocks_ocr.ocr.get_values_manual import get_values_manual
from endfield_stocks_ocr.ocr.get_values import get_values
from endfield_stocks_ocr.utils.aspect_ratio import check_aspect_ratio
from endfield_stocks_ocr.utils.logger import EndfieldLogger


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
