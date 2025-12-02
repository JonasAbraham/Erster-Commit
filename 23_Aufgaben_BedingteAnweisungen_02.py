from random import randint

benutzereingabe = int(input("Bitte gib eine Zahl zwischen 1 und 10 ein: "))

zufallszahl = randint(1,10)

if benutzereingabe == zufallszahl:
    print("Herzlichen Glückwunsch, du hast gewonnen!")
else:
    print(f"Leider falsch geraten! Die richtige Zahl ist {zufallszahl}.")