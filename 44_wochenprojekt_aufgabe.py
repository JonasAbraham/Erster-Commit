# Kleines interaktives Skript zum Sammeln von Reisezielen.

# Benutzung:
#  - Stadtname eingeben
#  - Bei ‚fertig‘ (ohne Anführungszeichen) wird die Eingabe beendet und die Liste ausgegeben
#  - Ansonsten werden Reisekosten und Aufenthaltsdauer abgefragt und in einer Liste gespeichert
#  - Dieser Vorgang wird solange wiederholt bis man bei der Stadteingabe ‚fertig‘ (ohne Anführungszeichen) eingibt

# - Es wurden weitere Ausgaben hinzugefügt (Teuerstes Ziel, durchschnittliche Kosten, Gesamtdauer usw.)


def stadt():
    while True:
        return input("Gib dein Reiseziel an (oder 'fertig' zum beenden ): ")

def reisekosten():
    while True:
        s = input("Gib die Reisekosten an: ")
        s.replace(",", ".")
        try:
            kosten = float(s)
            if kosten < 0:
                print("Kosten dürfen nicht negativ sein! Bitte erneut eingeben.")
                continue
            return kosten
        except ValueError:
            print("Die Eingabe ist ungültig. Bitte erneut eingeben.")

def dauer():
    while True:
        s = input("Gib die Aufenthaltsdauer an: ")
        try:
            tage = int(s)
            if tage <= 0:
                print("Aufenthaltsdauer darf nicht weniger oder gleich 0 sein! Bitte erneut eingeben.")
                continue
            return tage
        except ValueError:
            print("Die Eingabe ist ungültig. Bitte erneut eingeben.")        

def main():
    staedte = []
    kosten = []
    tage = []
    while True:
        city = stadt()
        if city.lower() == "fertig":
            break
        price = reisekosten()
        days = dauer()
        
        staedte.append(city)
        kosten.append(price)
        tage.append(days)

    if not staedte:
        print("Es wurden keine Reiseziele angegeben.")
        return

    print("Deine Reiseziele:")
    for i, (c,p,d) in enumerate(sorted(zip(staedte, kosten, tage), key=lambda x: x[1], reverse=True), start = 1):
        print(f"{i}. {c} - {p:.2f} € für {d} Tage.")

    teuerste_stadt = staedte[kosten.index(max(kosten))]
    guenstigste_stadt = staedte[kosten.index(min(kosten))]

    print("Reise-Analyse:")
    print(f"Anzahl der Reiseziele: {len(staedte)}")
    print(f"Gesamtkosten: {sum(kosten)} €")
    print(f"Gesamtdauer: {sum(tage)} Tage")
    print(f"Durchschnittskosten pro Ziel: {sum(kosten)/len(kosten):.2f} €")
    print(f"Durchschnittsdauer pro Ziel: {sum(tage)/len(tage):.0f} Tage")
    print(f"Teuerstes Ziel: {teuerste_stadt} ({max(kosten):.2f} €) ")
    print(f"Günstigstes Ziel: {guenstigste_stadt} ({min(kosten):.2f} €)")
    if sum(kosten) / len(kosten) <= 500.00:
        print("Deine Reisekosten sind im normalen Kostenbereich.")
    else:
        print(f"Deine Reisekosten sind {sum(kosten) - len(kosten) * 500.00:.2f} €, über dem Budget!")
        print(f"Deine Reisekosten sind {sum(kosten) / len(kosten) - 500.00:.2f} €, pro Reiseziel über dem Budget!")

if __name__ == "__main__":
    main()