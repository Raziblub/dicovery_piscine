#!/usr/bin/env python3
try:
    num1 = float(input("Donne-moi le premier nombre : "))
    num2 = float(input("Donne-moi le deuxième nombre : "))

    print("Merci !")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Division par zéro impossible.")
    print(f"{num1} * {num2} = {num1 * num2}")
except ValueError:
    print("Erreur : veuillez entrer un nombre.")
