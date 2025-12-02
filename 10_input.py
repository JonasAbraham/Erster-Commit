#Input = Eingaben vom Benutzer
# input() stoppt die Ausführung des Programms und wartet auf die Benutzereingabe
# der Input kann dann in einer Variablen gespeichert werden und weiterverarbeitet werden


benutzereingabe = input("Bitte gib eine Zahl ein: ")
print(benutzereingabe)
print(benutzereingabe * 10)
print(type(benutzereingabe))

# Eingaben sind IMMER strings, aber können konvertiert werden
# am besten direkt beim input

benutzereingabe = int(input("Bitte gib eine ganze Zahl ein: "))
print(benutzereingabe)
print(benutzereingabe * 10)
print(type(benutzereingabe))