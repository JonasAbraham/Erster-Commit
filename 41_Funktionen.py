# Funktionen
# Python stellt uns einige Funktionen zur Verfügung wie z.B. print(), type(), round(), sum() usw.

# # eigene Funktionen mit dem Schlüsselwort def ( define = definieren)
# def meine_erste_funktionen():
#     print("Das ist meine erste Funktion.")

# # Funktionsaufruf
# meine_erste_funktionen()

# # Bei der Bennenung der Funktion sollte der Bezeichner so akkurat wie möglich beschreiben was er macht. 
# # Zum Beispiel in der Form einer Handlungsaufforderung

# def gib_aus(text): # Parameter sind Variablen in der Funktion und können auch nur IN der Funktion genutzt werden
#     print(text)

# # Beim Funktionsaufruf stehen Argumente in Klammern
# gib_aus("Hallo, führe die Funktion aus.")
# gib_aus(2)
# gib_aus({1,2,3})

# #mehrere Parameter in einer Funktion
# def addiere(zahl1, zahl2):
#     ergebnis = zahl1 + zahl2
#     print(ergebnis)

# Fiunktionsaufruf mit mehreren Argumenten
# addiere(5,7)
# addiere(10) # --> Fehler! Ein Argument zu wenig übergeben
# addiere(10,2,5,5)  # --> Fehler! zwei Argumente zu viel übergeben

# # Schlüsselwort return in Funktionen
# # gibt einen Rückgabewert am Ende der Funktion zurück
# def subtrahier(zahl1,zahl2):
#     ergebnis = zahl1 - zahl2
#     return ergebnis

# print(subtrahier(10,2))
# ergebnis1 = subtrahier(10,2)
# ergebnis1 += 1
# print(ergebnis1)

# Beispielaufgabe: urlaubsanspruch abhängig vom Alter und der Betriebszugehörigkeit
def gib_urlaubsanspruch_aus(alter,jahre_im_betrieb):
    grundurlaub = 22

    # Bonus für das ALter
    if alter >= 50:
        bonus_alter = 5
    else:
        bonus_alter = 0
    #Bonus für die Betriebszugehöriggkeit
    if jahre_im_betrieb > 10:
        bonus_betrieb = 3
    else:
        bonus_betrieb = 0
    
    gesamturlaub = grundurlaub + bonus_alter + bonus_betrieb
    print(f"Der Gesamturlaub beträgt: {gesamturlaub} Tage")

# Aufruf der Funktion gib_urlaubsanspruch_aus()
gib_urlaubsanspruch_aus(55, 14) # Der Gesamturlaub beträgt: 30 Tage
gib_urlaubsanspruch_aus(34, 4) # Der Gesamturlaub beträgt: 22 Tage
gib_urlaubsanspruch_aus(62, 8) # Der Gesamturlaub beträgt: 27 Tage
gib_urlaubsanspruch_aus(38, 16) # Der Gesamturlaub beträgt: 25 Tage