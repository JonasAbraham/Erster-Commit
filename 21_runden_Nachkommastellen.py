# Wie kann man Zahlen in Python auf- oder abrunden?

#Python rundet bis .50 ab
print(round(4.49))
print(round(4.50))
print(round(4.51))

# Wie kann man entscheiden auf welche Stelle nach dem Komma gerundet werden soll?
# auf n beliebeige nachkommastellen runden, Ausnahme ist die Zahl .5! 
# Da wird immer so gerundet wird, dass die letzte nicht weggelassene Ziffer gerade ist.
print(round(1.23, 1))
print(round(1.236, 2))
print(round(1.2365, 3))

#bei GENAU .5 rundet Python zur geraden Zahl entweder auf oder ab!
print(round(0.5)) #0
print(round(1.5)) #2
print(round(2.5)) #2
print(round(3.5)) #4
print(round(4.5)) #4

#Funktionen zum auf- und abrunden

from math import ceil, floor

#aufrunden mit ceil()
print(ceil(2.1)) #3
print(ceil(-2.1)) #-2

#abrunden mit floor()
print(floor(2.1)) #2
print(floor(-2.1)) #-3

#Nachkommastellen und formatieren mit einem f-string --> mit:.2f angeben
zahl1 = 3.14756456533
print(f"Die Zahl ist: {zahl1:.2f}")
print(f"Die Zahl ist: {zahl1:.3f}")