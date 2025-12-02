#Einfacher Taschenrechner mit Benutzereingabe und den 4 Basis-Rechenoperatoren

print("Willkommen beim einfachen Taschenrechner.")
print("Bitte gib nacheinander die erste Zahl, den Rechenoperator und die zweite Zahl ein, für die Berechnung.")
print("Es sind nur die Rechenoperatoren +,-,/,*,// und % möglich!")

zahl1 = float(input("Bitte gib die erste Zahl ein. "))
rechenoperator = input("Bitte gib den Rechenoperator ein:")
zahl2 = float(input("Bitte gib die zweite Zahl ein um die Berchnung zu starten: "))

if rechenoperator == "+":
    ergebnis =  zahl1 + zahl2
    print(ergebnis)
elif rechenoperator == "-":
    ergebnis =  zahl1 - zahl2
    print(ergebnis)
elif rechenoperator == "*":
    ergebnis =  zahl1 * zahl2
    print(ergebnis)
elif rechenoperator == "/":
    ergebnis =  zahl1 / zahl2
    print(ergebnis)
elif rechenoperator == "//":
    ergebnis =  zahl1 // zahl2
    print(ergebnis)
elif rechenoperator == "%":
    ergebnis =  zahl1 % zahl2
    print(ergebnis)
else:
    print("Eingabe ungültig")