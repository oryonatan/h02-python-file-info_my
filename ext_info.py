__author__ = 'yonatan'

import sys
import pathlib
from collections import defaultdict


def create_file_type():
    return {
        'count': 0,
        'size': 0,
    }


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("displays number of files and total size of files per extension in the specified path.")
        exit()

    path = sys.argv[1]
    files_data = defaultdict(create_file_type)
    items_in_folder = pathlib.Path(path).iterdir()

    for file in items_in_folder:
        if file.is_dir():
            continue
        else:
            sanitized_suffix = file.suffix if file.suffix else "."  # if there is no suffix - set it to "."
            files_data[sanitized_suffix]['count'] += 1
            files_data[sanitized_suffix]['size'] += file.stat().st_size

    suffixes = list(files_data.keys())
    suffixes.sort()

    for suffix in suffixes:
        print(" ".join(
            [suffix[1:] if suffix != "." else ".",  # Ignore the dot ... unless it's just a dot
             str(files_data[suffix]['count']),
             str(files_data[suffix]['size'])]))
