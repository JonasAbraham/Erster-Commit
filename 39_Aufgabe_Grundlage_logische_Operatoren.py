körpergröße = float(input("Wie groß bist du in Metern? "))
alter = int(input("Wie alt bist du? "))
begleitung = input("Bist du in Begleitung eines Erwachsenen? (ja/nein) ")

if körpergröße < 1.2:
    print("Du darfst nicht mitfahren, ess ein paar Fruchtzwerge.")
elif alter < 10:
    print("Du darfst nicht mitfahren, geh und suche deine Mama.")
elif 10 <= alter <= 15 and begleitung == "nein":
    print("Du darfst nicht mitfahren, komm wieder mit einer erwachsenen Begleitung.")
elif 10 <= alter <= 15 and begleitung == "ja":
    print("Du darfst mitfahren.")
else:
    print("Du darfst alleine mitfahren.")