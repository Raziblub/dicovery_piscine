#!/usr/bin/env python3
try:
    age = int(input("Please tell me your age: "))
    if age < 0:
        print("Erreur : l'âge ne peut pas être négatif.")
    else:
        print(f"You are currently {age} years old.")
        print(f"In 10 years, you'll be {age + 10} years old.")
        print(f"In 20 years, you'll be {age + 20} years old.")
        print(f"In 30 years, you'll be {age + 30} years old.")
except ValueError:
    print("Erreur : veuillez entrer un nombre entier.")
