#!/usr/bin/env python

"""
Extract and dump player data from cached FPL bootstrap data.
"""

import argparse
import csv
from datetime import datetime
import json
import lzma
from pathlib import Path

default_props = [
    'id',
    'web_name',
    'now_cost',
    'chance_of_playing_this_round',
    'total_points'
]


def main(args):
    # Find all compressed JSON files in the cache.
    paths = []
    for path in args.cache.glob('**/*.json.xz'):
        time = datetime(
            year=int(path.parts[1]),
            month=int(path.parts[2]),
            day=int(path.parts[3]),
            hour=int(path.parts[4][:2]),
            minute=int(path.parts[4][2:4]))
        paths.append((time, path))
    paths.sort()

    if args.limit and args.limit > 0:
        paths = paths[:args.limit]

    # Process each file in the cache and extract the player data.
    props = args.props.split(',')
    with args.out.open('wt', encoding='utf-8', newline='') as c:
        writer = csv.writer(c)
        writer.writerow(','.join(['time'] + props))
        for i, (time, path) in enumerate(paths):
            if args.verbose:
                print(f'[{i+1:4d}/{len(paths):4d}] {path}')
            with lzma.open(path, 'rt', encoding='utf-8') as f:
                data = json.loads(f.read())
            for player in data['elements']:
                row = [str(time)]
                row.extend(player[prop] for prop in props)
                writer.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Extract and dump player data from cached FPL bootstrap data.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-p', '--props', default=','.join(default_props), help='comma-separated list of properties to dump')
    parser.add_argument('-n', '--limit', type=int, default=0, help='max no. of files to process')
    parser.add_argument('-o', '--out', type=Path, default=Path('dump.csv'), help='CSV output path')
    parser.add_argument('-v', '--verbose', action='store_true', help='enables verbose output')
    parser.add_argument('--cache', type=Path, default=Path('cache'), help='cache path')
    main(parser.parse_args())
