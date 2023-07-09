#!/usr/bin/env python

"""
Diff two LZMA-compressed JSON files.
"""

import argparse
import difflib
import lzma
from pathlib import Path
import sys

differs = {
    'context': difflib.context_diff,
    'unified': difflib.unified_diff
}


def main(args):
    with lzma.open(args.a, 'rt', encoding='utf-8') as f:
        a = f.readlines()

    with lzma.open(args.b, 'rt', encoding='utf-8') as f:
        b = f.readlines()

    diff = differs[args.format](a, b, fromfile=str(args.a), tofile=str(args.b))
    sys.stdout.writelines(diff)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Diff two LZMA-compressed JSON files.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-f', '--format', choices=differs.keys(), default='context', help='diff format')
    parser.add_argument('a', type=Path, help='path to first file')
    parser.add_argument('b', type=Path, help='path to second file')
    main(parser.parse_args())
