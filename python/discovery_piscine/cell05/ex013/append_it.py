#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    for word in args:
        if not word.endswith("ism"):
            print(f"{word}ism")
