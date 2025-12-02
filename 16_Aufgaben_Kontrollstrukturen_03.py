altersabfrage = int(input("Bitte gib dein Alter als ganze Zahl ein: "))

if 0 < altersabfrage < 18:
    print("Du bist minderjährig.")
elif 18 <= altersabfrage < 67:
    print("Du bist volljährig.")
elif altersabfrage >= 67:
    print("Du bist im Rentenalter.")
else:
    print("Eingabe ungültig.")