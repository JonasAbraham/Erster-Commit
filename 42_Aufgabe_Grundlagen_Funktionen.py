from random import randint


def hauptmenue():
    print("""1 - Begrüßung
2 - Witz
3 - Kompliment
4 - Beenden""")
    return input("Bitte gib eine Zahl von 1-4 an: ")

    
def begruessung():
    gruss = "Hallo, ich bin Siegfried. Dein persönlicher Chatbot."
    print(gruss)

def witz():
    witze_liste = ["""Was macht eine Blondine in der Wüste?
Staubsaugen!""", """Was ist rot und hat einen Schnupfen?
Ein Ranieschen.""", """Ich war heute bei einem Seminar für Kleptomanie.
Hab davon einiges mitgenommen.""", """Wie nennt man einen Schneemann im Sommer?
Pfütze!""" ]
    print(witze_liste[randint(0,len(witze_liste)-1)])

def kompliment():
    kompliment_liste = ["Du siehst gut aus!", "Du bist sehr intelligent!","Geiler Style!", "Coole Jacke!", "Du hast ein gutes Herz.", "Du bist echt stark!"]
    print(kompliment_liste[randint(0,len(kompliment_liste)- 1)])

def beenden():
    print("Auf Wiedersehen!")


while True:
    auswahl = hauptmenue()
    if auswahl == "1":
        begruessung()
    elif auswahl == "2":
        witz()
    elif auswahl == "3":
        kompliment()
    elif auswahl == "4":
        beenden()
        break
    else:
        print("Ungültige Menüauswahl")