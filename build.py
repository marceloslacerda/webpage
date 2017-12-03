#!/usr/bin/env python3

import re
import os
import os.path
from subprocess import call
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
INPUT_DIR = Path(CURRENT_DIR, 'src')
OUTPUT_DIR = Path(CURRENT_DIR, 'out')


def build():
    if not INPUT_DIR.is_dir():
        raise OSError('Could not find source directory {}'.format(INPUT_DIR))
    for entry in INPUT_DIR.glob('**/*.rst'):
        if entry.is_file():
            if os.access(str(entry), os.R_OK):
                output = entry.relative_to(INPUT_DIR)
                output = OUTPUT_DIR / output
                output = output.with_suffix('.html')
                output.parent.mkdir(parents=True, exist_ok=True)
                build_html(str(entry), str(output))


def build_html(input_, output):
    ret = call(['rst2html5', input_, output])
    if ret != 0:
        exit(ret)
    # rst2html5 entry.path output.path/output.filename.html

if __name__ == '__main__':
    build()
