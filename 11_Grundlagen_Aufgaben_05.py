wohnort = input("Bitte gib deinen Wohnort an:")
print(f"Guten Tag, Bewohner aus {wohnort}!")

uhrzeit = input("Bitte gib die aktuelle Uhrzeit an:")
name = input("Bitte gib deinen Namen an:")
print(f"Guten Morgen {name}. Es ist {uhrzeit}.")

lieblingszahl = int(input(f"Was ist deine Lieblingszahl {name}?"))
# lieblingszahl2 = lieblingszahl * 2
print(f"Also ist das doppelte deiner Lieblingszahl {lieblingszahl * 2}.")

nettopreis = float(input(f"Was war der Nettopreis des Gegenstandes {name}?"))
bruttopreis = nettopreis * 1.19
print(f"Der Bruttopreis beträgt {bruttopreis:.2f} €.")
print(bruttopreis)