#!/usr/bin/env python3
import sys
params = sys.argv[1:]
if len(params) != 1:
    print("none")
else:
    input_string = params[0]
    z_chars = [char for char in input_string if char == 'z']
    
    if z_chars:
        print(''.join(z_chars))
    else:
        print("none")
