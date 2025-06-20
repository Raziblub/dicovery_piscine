#!/usr/bin/env python3
import sys
def shrink(s):
    print(s[:8])
def enlarge(s):
    print(s + 'Z' * (8 - len(s)))
args = sys.argv[1:]
if not args:
    print("none")
else:
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
import sys
def shrink(s):
    print(s[:8])

def enlarge(s):
    print(s + 'Z' * (8 - len(s)))
args = sys.argv[1:]
if not args:
    print("none")
else:
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
