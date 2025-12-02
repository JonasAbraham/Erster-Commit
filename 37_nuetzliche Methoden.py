# nützliche Methoden in Python

# Für Listen mit gleichen Datentypen
liste = [1,5,8]
print(sum(liste)) #berechnet die SUmme aller Werte der Liste
print(max(liste)) # gibt den größten Wert der Liste zurück
print(min(liste)) # gibt den kleinsten Wert der Liste zurück

# Für Strings
text = "python ist COOL!"
print(text.title()) # Ausgabe : Python Ist Cool! --> jedes Wort beginnt mit einem Großbuchstaben
print(text.capitalize()) # Ausgabe: Python ist cool! --> nur der erste Buchstabe des gesamten Textes wird groß geschrieben, der Rest wird klein geschrieben
print(text.swapcase()) # Ausgabe: PYTHONIST cool! --> dreht Groß- und Kleinbuchstaben um
print(text.upper()) # Ausgabe: PYTHON IST COOL! --> erzeugt Großbuchstaben
print(text.lower()) # Ausgabe: python ist cool --> erzeugt Kleinbuchstaben
print(text.split()) # Ausgabe ['python', 'ist', 'COOL!'] --> erzeugt eine Liste, in der jedes Wort ein Eintrag in der Liste wird
print(text.replace("COOL", "toll")) #Ausgabe: python ist toll! --> ersetzt ein Wort durch ein anderes