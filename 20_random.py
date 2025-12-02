from random import randint, uniform

#random wird genutzt um zufällige Zahlen zu erzeugen
#dafür wird ein Import benötigt, siehe Zeile 1

#gibt ganze Zahlen von 1-6 aus, immer inklusive der letzten Zahl
zahl1 = randint(1,6)
print(zahl1)

#gibt Fließkommazahlen aus
zahl2 = uniform(0.5,6.6)
print(zahl2)

#schreibe ein Programm, das eine Münze wirft und das Ergebnis ausgibt
wurf = randint(0,1)

if wurf == 1:
    ergebnis = "Kopf"
else:
    ergebnis = "Zahl"

print(f"Die Münze zeigt {ergebnis} an.")