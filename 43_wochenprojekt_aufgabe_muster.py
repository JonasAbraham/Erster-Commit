# """Kleines interaktives Skript zum Sammeln von Reisezielen.

# Benutzung:
#  - Stadtname eingeben
#  - Bei ‚fertig‘ (ohne Anführungszeichen) wird die Eingabe beendet und die Liste ausgegeben
# """

# def stadt():
#     return input("Gib den Namen einer Stadt als Reiseziel an (oder 'fertig' zum Beenden): ").strip()

# def reisekosten():
#     while True:
#         s = input("Gib die Kosten des Reiseziels an (z. B. 123.45): ").strip()
#         # Akzeptiere auch Komma als Dezimaltrennzeichen
#         s = s.replace(',', '.')
#         try:
#             kosten = float(s)
#             if kosten < 0:
#                 print("Kosten dürfen nicht negativ sein. Bitte erneut eingeben.")
#                 continue
#             return kosten
#         except ValueError:
#             print("Ungültige Eingabe. Bitte eine Zahl eingeben (z. B. 123.45).")

# def dauer():
#     while True:
#         s = input("Gib die Aufenthaltsdauer in Tagen an (ganze Zahl): ").strip()
#         try:
#             tage = int(s)
#             if tage < 0:
#                 print("Tage dürfen nicht negativ sein. Bitte erneut eingeben.")
#                 continue
#             return tage
#         except ValueError:
#             print("Ungültige Eingabe. Bitte eine ganze Zahl eingeben.")

# def main():
#     staedte = []
#     kosten = []
#     aufenthaltsdauer = []

#     while True:
#         city = stadt()
#         if city.lower() == 'fertig':
#             break
#         price = reisekosten()
#         days = dauer()

#         staedte.append(city)
#         kosten.append(price)
#         aufenthaltsdauer.append(days)

#     if not staedte:
#         print("Es wurden keine Reiseziele eingegeben.")
#         return

#     print('\nDeine Reiseliste:')
#     for i, (c, p, d) in enumerate(zip(staedte, kosten, aufenthaltsdauer), start=1):
#         print(f"{i}. {c} - {p:.2f} € für {d} Tage")


# if __name__ == '__main__':
#     main()
a = "eins"
b = a + 1.2
print(b)