# while-Schleifen wiederholen sich solange bis die bedingte Anweisung wahr ist
# ähnelt der for-Schleife, hat aber eine bedingte Anweisung anstelle der Zählervariable

i = 0
# while i<10:
#     print(f"{i} ist kleiner als 10")
#     i += 1 # Kurzschreibweise für i = i + 1

# # Endlosschleife
# while i < 5:
#     print(f"{i} ist kleiner als 5") #Achtung vor Endlosschleifen!!! Variablen immer anpasen bzw. erhöhen.
# # Falls es jedoch trotzdem passiert und man den Code schon ausgeführt hat, kann man es abbrechen mit dem Befehl "strg+c".

#continue und break steuern Schleifen

# #continue beendet den aktuellen Schleifendurchlauf
# for zahl in range(10):
#     if zahl % 2 == 0:
#         continue # sorgt dafür, dass der Schleifendurchlauf vorzeitig beendet wird und es wird direkt mit der nächsten Zahl weitergemacht
#     print(f"Die {zahl} ist ungerade")

# while True:
#     eingabe = input("Bitte gib ein Wort mit mindestens 3 Buchstaben ein: ")
#     if len(eingabe) < 3:
#         print(f"Eingabe ist zu kurz.")
#         continue # Wenn das Wort zu kurz ist, wird die nächste Zeile nicht mehr ausgeführt und es wird  die nächste Eingabe überprüft.
#     print(f"Sie haben folgendes Wort eingegeben: {eingabe}")
#     break

# # break beendet die Schleife
# for zahl1 in range(1,10):
#     print(f"Zahl: {zahl1}")
#     break

# while True:
#     print("Endlosschleife")
#     break

# Schreibe ein Programm, dass so lange eine zufällige Zahl von 1-6 würfelt, bis eine 6 gewürfelt wurde
from random import randint

while True:
    wurf = randint(1,6)
    if wurf != 6:
        print(f"Du hast eine {wurf} gewürfelt.")
    else:
        print(f"Du hast {wurf} gewürfelt.Glückwunsch!")
        break