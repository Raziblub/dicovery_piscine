#!/usr/bin/env python3
try:
    import math
    num = float(input("Give me a number: "))
    rounded = math.ceil(num)
    print(rounded)
except ValueError:
    print("error please enter a number")