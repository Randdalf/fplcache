#!/usr/bin/env python

"""
Fetch and cache FPL bootstrap data.
"""

import argparse
import datetime
import json
import lzma
from pathlib import Path
import requests


def main(args):
    # Fetch the FPL bootstrap JSON.
    print(f'Fetching {args.url}... ', end='', flush=True)
    r = requests.get(args.url)
    if not r.ok:
        print(f'Failed: {r.status_code}.')
        exit(1)
    print('OK.')

    # Prettify the JSON so it can be diffed.
    print(f'Prettifying JSON... ', end='', flush=True)
    pretty = json.dumps(r.json(), indent=4, sort_keys=True)
    print(f'OK.')

    # Prepare the cache file path.
    now = datetime.datetime.today()
    path = args.cache / Path(f'{now.year}/{now.month}/{now.day}/{now.hour:02d}{now.minute:02d}.json.xz')
    path.parent.mkdir(parents=True, exist_ok=True)

    # Compress the JSON into the cache.
    print(f'Compressing into {path}... ', end='', flush=True)
    with lzma.open(path, 'wt', encoding='utf-8') as f:
        f.write(pretty)
    print(f'OK.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Fetch and cache FPL bootstrap data.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--url', default='https://fantasy.premierleague.com/api/bootstrap-static/', help='url to cache')
    parser.add_argument('--cache', type=Path, default=Path('cache'), help='cache path')
    main(parser.parse_args())
