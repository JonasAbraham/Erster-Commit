#Vergleichsoperatoren
# ein Vergleich wird immer zu einem Boolean ausgewertet

zahl1 = 2
zahl2 = 3
zahl3 = 2

# == ist der Gleichheitsoperator
print(zahl1 == zahl2) # False
print(zahl1 == zahl3)  # True

# != Ungleichheitsoperator
print(zahl1 != zahl2) # True
print(zahl1 != zahl3)  #False

# > größer als
print(zahl1 > zahl2) # False
print(zahl2 > zahl3) # True

# < kleiner als
print(zahl1 < zahl2) # True
print(zahl2 < zahl3) # False
print(zahl1 < zahl3) # False

# >= größer gleich
print(zahl1 >= zahl2) # False
print(zahl2 >= zahl3) # True
print(zahl1 >= zahl3) # True

# <= kleiner gleich
print(zahl1 <= zahl2) # True
print(zahl1 <= zahl3) # True
print(zahl2 <= zahl1) # False