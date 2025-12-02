# String Operatoren

vorname = "Jonas"
nachname = "Abraham"

print(vorname, nachname)
print(vorname + nachname)
print(vorname + " " + nachname)

alter = 36

# print(vorname + " " + nachname + " " + alter) --> Fehler, weil String und int nicht aneinander gehftet werden können
print(vorname + " " + nachname + " " + str(alter))

#f-Strings
print(f"Mein Name ist {vorname} {nachname} und ich bin {alter} Jahre alt.")

#f-string über mehrere Zeilen
print(f"Vorstellung: \n"
f"Mein Name ist {vorname} {nachname} und ich bin {alter} Jahre alt." )

#f-string Beispiel mit type()
zahl1 = 5
zahl2 = 2.5

print(f"Der Datentyp von Zahl1 ist {type(zahl1)} und der Datentyp von Zahl2 ist {type(zahl2)}.")

# lange String auf mehrere Zeilen teilen und ausgeben mit """", also 3 Anführungszeichen
print(f"""Hallo zusammen
wir lernen Python
in LF{zahl1}""")

#String Multiplikator mit * Operator
print( (vorname + " ") * zahl1)