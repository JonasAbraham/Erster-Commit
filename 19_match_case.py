# match-case in Python
# andere Darstellung von einem if-elif-else
# prüft mehrere Bdingungen

#match-case mit Strings
farbe = input("Was ist deine Lieblingsfarbe?").lower()

match farbe:
    case "rot":
        print("Rot ist eine schöne Farbe.")
    case "blau":
        print("Blau ist eine schöne Farbe")
    case "grün":
        print("Grün ist eine schöne Farbe")
    case _:
        print(f"{farbe} ist mir unbekannt.")


# match-case mit Zahlenwerten
zahl1 = int(input("Gib deine Lieblingszahl ein: "))

match zahl1:
    case 1:
        print("Die Zahl 1 ist eine schöne Zahl.")
    case 2:
        print("Die Zahl 2 ist eine schöne Zahl.")
    case 3:
        print("Die Zahl 3 ist eine schöne Zahl.")
    case _:
        print(f"{zahl1} ist aber eine komische Wahl...")