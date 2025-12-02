# Listen
# Neuer Datentyp, der mehrere Werte beinhaltet

# # Eckige Klammern erzeugen eine Liste
# liste1 = [1,2,3,4,5]
# print(liste1)
# print(type(liste1))

# # einzelne Werte aus einer Liste auslesen
# print(liste1[0])
# print(liste1[1])
# print(liste1[2])
# print(liste1[3])
# print(liste1[4])
# # print(liste1[5]) # IndexError: list index out of range --> weil an der Stelle in der Liste kein Wert steht.

# # bestehende Werte in einer Liste ändern
# liste1[0] = 9
# print(liste1[0])
# print(liste1)

# # Länge einer Liste ausgeben
# print(len(liste1))

# # Liste mit Strings befüllen
# listen_farben = ["rot","blau","grün","gelb"]
# print(listen_farben[2])

#from random import choice
# zufall = choice(listen_farben)
# print(zufall)

# # random mit boolean
# zufall_boolean = choice([True, False])
# print(zufall_boolean)
# print(type(zufall_boolean))

# # Listen können mit verschiedenen Werten befüllt werden
# liste2 = [1, 2.2, "Text", True, [1,2]]
# print(liste2)

# # .append() Methode nutzen um eine Liste zu erweitern
# liste2.append("hinzugefügt")
# print(liste2)

# # .pop() Methode, um den letzten Eintrag der Liste zu entfernen
# letzter_wert_der_liste = liste2.pop(2) # mit der Angabe des Indexes kann beliebiges Element entfernt werden
# print(letzter_wert_der_liste)
# print(liste2)

# # mit list() können Listen aus Text oder Zahlen erstellt werden
# print(list(range(5)))
# print(list("Hello!"))
# print(list(range(1,6)))

# mit .sort() können Listen sortiert werden
liste_sortieren = [2,5,105,10,84,6,7]
liste_sortieren.sort() # aufsteigend sortiert
print(liste_sortieren)
liste_sortieren.sort(reverse=True) # absteigend sortiert
print(liste_sortieren)