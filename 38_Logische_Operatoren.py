# Logische Operatoren
# werden auch boolesche Operatoren genannt
# ermöglichen die gleichzeitige Abfrag von mehreren Bedingungen

# and (in anderen Programmiersprachen auch oft als &&)
print(2<3 and 3<4) # es wird geprüft, ob BEIDE Aussagen True oder False sind --> beide True 18
# ist nur True wenn beide bedingungen erfüllt sind
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# or - Operator ( in anderen Programmiersprachen auch oft als ||)
# wird True wenn eine der Bedingungen erfüllt ist
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

# not - Operator
# Umkehrung für den Wahrheitswert
print( not True) # False
print( not False) # True

regnet_es = True

if not regnet_es:
    print("Es regnet nicht!")
else:
    print("Es regnet...")


# Beispielaufgabe: Darf ich ins Kino?
# mindestens 16 Jahre alt oder 14 Jahre alt und in Begleitung eines Erwachsenen
# unter 14 Jahren darf ich nicht ins Kino

alter = int(input("Wie alt bist du? "))
begleitung = input("Bist du in begleitung eines Erwachsenen? (ja/nein) ")

if alter >= 16 or (alter >= 14 and begleitung == "ja"):
    print("Du darfst ins Kino!")
else:
    print("Du darfst nicht ins Kino!")

# or erlaubt den Zutritt, wenn eine der 2 Bedingunen erfüllt ist. Entweder alter >= 16 oder ( alter >= 14 and begleitung == "ja")
# and zeigt an, dass 14 und 15 Jährige nur mit Begleitung ins Kino dürfen --> beide Bedingungen müssen True sein