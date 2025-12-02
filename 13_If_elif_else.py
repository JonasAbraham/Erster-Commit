#Bedingte Anweisung (if-Anweisung)
#man kann den Ablauf des Programms beeinflussen, je nachdem welche Bedingung erfüllt wird, nimmt das Programm einen anderen Verlauf

#if-else-Bedingung
#Wenn erste Bedingung wahr ist, führe den eingerückten Code aus.

zahl1 = -2
if zahl1 < 0: 
    print("Die Zahl ist negativ!")
else:
    print("Die Zahl ist positiv!")


#if-elif-else
zahl2 = 4
zahl3 = 4

if zahl2 > zahl3:
    print(f"{zahl2} ist größer als {zahl3}.")
elif zahl2 < zahl3:
    print(f"{zahl2} ist kleiner als {zahl3}")
else:
    print("Die Zahlen sind gleich groß.")


#if-elif-else mit strings
#ampelfarbe = "gelb"

ampelfarbe = input("Welche Farbe hat die Ampel? ")

if ampelfarbe == "rot":
    print("Bremsen und stehenbleiben!")
elif ampelfarbe == "gelb":
    print("Die Ampel ist gelb. Bereite dich vor loszufahren!")
elif ampelfarbe == "grün":
    print("Die Ampel ist grün. Du kannst losfahren")
else:
    print("Fehler, Ampel ist nicht funktionsfähig!")