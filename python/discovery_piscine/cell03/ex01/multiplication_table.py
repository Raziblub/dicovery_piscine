#! /usr/bin/env python3
try:
    num = int(input("Enter a number to display its multiplication table:\n"))
    for i in range(0, 11):
        result = num * i
        print(f"{num} x {i} = {result}")
except ValueError:
    print("error please enter a int number")