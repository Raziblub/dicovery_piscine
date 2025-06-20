#! /usr/bin/env python3
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    if abs(result) < 1e-10:
        result = 0.0
    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is zero.")
    print("The result of the multiplication is:", result)
except ValueError:
    print("Error: Please enter a valid number.")