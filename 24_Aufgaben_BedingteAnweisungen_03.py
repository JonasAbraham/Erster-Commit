from random import randint

aufgabentyp = randint(1,4)
zahl1 = randint(1,100)
zahl2 = randint(1,100)

match aufgabentyp:
    case 1:
        print(f"{zahl1} + {zahl2} = {zahl1+zahl2}")
    case 2:
        print(f"{zahl1} - {zahl2} = {zahl1-zahl2}")
    case 3:
        print(f"{zahl1} * {zahl2} = {zahl1*zahl2}")
    case _:
        print(f"{zahl1} / {zahl2} = {zahl1/zahl2:.2f}")