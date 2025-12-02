# Variablen und Datentypen in Python
# Variablen speichern Informationen und Werte, nützlich um diese an mehreren Stellen im Programm zu nutzen
# Variablen klein schreiben, entsprechend benennen und keine Schlüsselwörter!
# Python Schreibweise = hallo_weiteres_wort
# Java Schreibweise =halloWeiteresWort

# String ---> Zeichenkette, Text
first_name = "Jonas" # first_name ist der Bezeichner der Variable, also der eingetragene Name, mit dem = wird der Variable ein Wert zugewiesen
last_name = "Abraham"
vorstellung = "Ich heiße"

print(vorstellung, first_name, last_name)

#Datentypen geben die Art des Wertes einer Variablen an
#Zahlenwerte
zahl1 = 1
zahl2 = 2.5

print(zahl1, zahl2)

print(type(zahl1), type(zahl2)) #type() gibt den Datentyp an
print(type(zahl2))

#boolesche Werte haben immer nur den Zustand True oder False
bool1 = True
bool2 = False
bool1 = False

print(bool1, bool2)