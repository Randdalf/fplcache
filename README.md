# ⚽ fplcache

## Overview
This repository contains a cache of [Fantasy Premier League](https://fantasy.premierleague.com/) bootstrap data, a JSON object returned by the https://fantasy.premierleague.com/api/bootstrap-static/ endpoint. To significantly reduce storage size, these JSON objects are cached using the LZMA `.xz` file format. This cache is updated four times a day, spaced at 6 hour intervals, using [GitHub Actions](https://docs.github.com/en/actions).

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

### `dump.py`
```
usage: dump.py [-h] [-p PROPS] [-n LIMIT] [-o OUT] [-v] [--cache CACHE]

Extract and dump player data from cached FPL bootstrap data.

options:
  -h, --help            show this help message and exit
  -p PROPS, --props PROPS
                        comma-separated list of properties to dump (default: id,web_name,now_cost,chance_of_playing_this_round,total_points)
  -n LIMIT, --limit LIMIT
                        max no. of files to process (default: 0)
  -o OUT, --out OUT     CSV output path (default: dump.csv)
  -v, --verbose         enables verbose output (default: False)
  --cache CACHE         cache path (default: cache)
```
