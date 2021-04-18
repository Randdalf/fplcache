# ⚽ fplcache

## Overview
This repository contains a cache of [https://fantasy.premierleague.com/](Fantasy Premier League) bootstrap data, a JSON object returned by the https://fantasy.premierleague.com/api/bootstrap-static/ endpoint. To significantly reduce storage size, these JSON objects are cached using the LZMA `.xz` file format. This cache is updated four times a day, spaced at 6 hour intervals, using [https://docs.github.com/en/actions](GitHub Actions).

## Organization
Cached objects are organized as follows within the `cache` directory:
```
{year}/{month}/{day}/{time}.json.xz
```

## Utilities
The following utility scripts are provided for managing cached objects.

### `cache.py`
```
usage: cache.py [-h] [--url URL] [--cache CACHE]

Fetch and cache FPL bootstrap data.

optional arguments:
  -h, --help     show this help message and exit
  --url URL      url to cache (default:
                 https://fantasy.premierleague.com/api/bootstrap-static/)
  --cache CACHE  cache path (default: cache)
```

### `cat.py`
```
usage: cat.py [-h] file

Write contents of LZMA-compressed JSON file to standard output.

positional arguments:
  file        path to file

optional arguments:
  -h, --help  show this help message and exit
```

### `diff.py`
```
usage: diff.py [-h] [-f {context,unified}] a b

Diff two LZMA-compressed JSON files.

positional arguments:
  a                     path to first file
  b                     path to second file

optional arguments:
  -h, --help            show this help message and exit
  -f {context,unified}, --format {context,unified}
                        diff format (default: context)
```
