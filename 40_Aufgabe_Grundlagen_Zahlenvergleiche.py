from random import randint

# zahl1 = randint(1,100)
# zahl2 = randint(1,100)

# if zahl1 > zahl2:
#     print(f"Die erste Zahl {zahl1} ist größer als die zweite Zahl {zahl2}.")
# elif zahl1 < zahl2:
#     print(f" Die zweite Zahl {zahl2} ist größer als die erste Zahl {zahl1}.")
# else:
#     print(f"Die Zahlen {zahl1} und {zahl2} sind gleich groß.")


# # AUFGABE 2
# zahl1 = randint(1,100)
# zahl2 = randint(1,100)
# zahl3 = randint(1,100)

# zahlen_liste = []
# zahlen_liste.append(zahl1)
# zahlen_liste.append(zahl2)
# zahlen_liste.append(zahl3)

# print(f"Zahlen: {zahlen_liste}")
# print(f"Größte Zahl: {max(zahlen_liste)}")
# print(f"Kleinste Zahl: {min(zahlen_liste)}")

# zahlen_liste.sort()

# print(f"Sortierte Reihenfolge: {zahlen_liste}")

## AUFGABE 3

zahl1 = randint(1,101)
zahl2 = randint(1,101)
zahl3 = randint(1,101)
zahl4 = randint(1,101)
zahl5 = randint(1,101)

zahlen_liste = [zahl1, zahl2, zahl3, zahl4, zahl5]
zahlen_liste.sort(reverse=True)

print(f"Zahlen: {zahlen_liste}")
print(f"Größte Zahl: {max(zahlen_liste)}")
print(f"Kleinste Zahl: {min(zahlen_liste)}")
print(f"Durchschnitt: {sum(zahlen_liste) / len(zahlen_liste)}")