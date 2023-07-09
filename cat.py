#!/usr/bin/env python

"""
Write contents of LZMA-compressed JSON file to standard output.
"""

import argparse
import lzma
from pathlib import Path


def main(args):
    with lzma.open(args.file, 'rt', encoding='utf-8') as f:
        print(f.read())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Write contents of LZMA-compressed JSON file to standard output.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('file', type=Path, help='path to file')
    main(parser.parse_args())
