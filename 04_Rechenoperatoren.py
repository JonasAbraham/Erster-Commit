# Rechnen mit den folgenden Operatoren --> + - * /

zahl1 = 15
zahl2 = 10

ergebnis_Addition = zahl1 + zahl2
print(ergebnis_Addition)

ergebnis_Subtraktion = zahl1 - zahl2
print(ergebnis_Subtraktion)

ergebnis_Multiplikation = zahl1 * zahl2
print(ergebnis_Multiplikation)

ergebnis_Division = zahl1 / zahl2
print(ergebnis_Division)

# Division liefert immer einen float
ergebnis_Division2 = 12/4
print(ergebnis_Division2)
print(type(ergebnis_Division2))

#Floor-Division mit // --> hier wird IMMER abgerundet und als int gespeichert
ergebnis_floor_division = 10 // 4
print(ergebnis_floor_division)
print(type(ergebnis_floor_division))

# Modulo % --> führt eine Restwert Division durch
print(10%6)

#Verwendung um gerade und ungerade Zahlen herauszufinden indem man die Restdivision mit 2 durchführt
print(12 % 2) # Wenn Ergebnis = 0 --> Die Zahl ist gerade
print(13 % 2) # Wenn Ergebnis ungleich 0 --> Die Zahlist ungerade

#** --> Potenzen
print(2 ** 10)