from random import randint

note = randint(1,6)

bewertungsliste = [
    "Sehr gut - Super gemacht!",
    "Gut - Weiter so!",
    "Befriedigend - Da geht noch mehr!",
    "Ausreichend - Gerade noch geschafft!",
    "Mangelhaft - Du solltest mehr üben!",
    "Ungenügend - Leider durchgefallen!"
    ] 

if note == 1:
    print(f"Deine Note: {note} {bewertungsliste[0]}")
elif note == 2:
    print(f"Deine Note: {note} {bewertungsliste[1]}")
elif note == 3:
    print(f"Deine Note: {note} {bewertungsliste[2]}")
elif note == 4:
    print(f"Deine Note: {note} {bewertungsliste[3]}")
elif note == 5:
    print(f"Deine Note: {note} {bewertungsliste[4]}")
else:
    print(f"Deine Note: {note} {bewertungsliste[5]}")

match note:
    case 1:
        print(f"Deine Note: {note} {bewertungsliste[0]}")
    case 2:
        print(f"Deine Note: {note} {bewertungsliste[1]}")
    case 3:
        print(f"Deine Note: {note} {bewertungsliste[2]}")
    case 4:
        print(f"Deine Note: {note} {bewertungsliste[3]}")
    case 5:
        print(f"Deine Note: {note} {bewertungsliste[4]}")
    case _:
        print(f"Deine Note: {note} {bewertungsliste[5]}")