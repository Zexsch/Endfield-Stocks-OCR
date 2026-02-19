import argparse
from pathlib import Path

from endfield_stocks_ocr.ocr.get_values import get_values
from endfield_stocks_ocr.utils.unpack import unpack
from endfield_stocks_ocr.utils.aspect_ratio import check_aspect_ratio

def main():
    unpack()
    check_aspect_ratio()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--wuling", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    
    if args.wuling:
        region = "wuling"
    else:
        region = "valley"
    
    get_values(region, args.debug)
