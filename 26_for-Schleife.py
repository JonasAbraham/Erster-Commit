# Die for-Schleife wird auch als Zählschleife bezeichnet
# Sie wird verwendet, um Code mehrfach hintereinander zu wiederholen
# man kann genau angeben, wie oft der Code wiederholt werden soll

# for i in range(3): # wenn nur ein Wert angegeben wird, startet die Zählschleife immer bei 0 und durchläuft die Schleife so oft wie angegeben
#     print(f"Durchgang {i}")

# for i in range(1,3): # erste Zahl ist der Startwert und inklusiv. Die letzte Zahl ist exklusiv, ergibt als zwei Durchgänge
#     print(f"Durchgang {i}")

# for i in range(1,4):
#     print(f"Durchgang: {i}") # Die Zählschleife wird 3 mal durchlaufen und startet bei 1

# # i ist die Programmrichtlinie, aber die Variable kann auch anders benannt werden
# for zahl in range(1,8):
#     print(f"Zahl: {zahl}")


# range(Anfange,Ende, Schrittweiter)
# for i in range(0,100,9):
#     print(f"Die Zahl lautet: {i}")

# mit negativen Zahlen
for i in range( -100, -5, -10):
    print(f"Die Zahl lautet: {i}")