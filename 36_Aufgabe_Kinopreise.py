from random import randint, choice

alter = randint(1,90)
dimension = choice([True, False]) 

if alter <= 5:
    ticket = 0
    if dimension == True:
        zuschlag = 0
        gesamtpreis = ticket + zuschlag
    else:
        zuschlag = 0
        gesamtpreis = ticket + zuschlag
elif 5 < alter < 17:
    ticket = 6.50
    if dimension == True:
        zuschlag = 1.5
        gesamtpreis = ticket + zuschlag
    else:
        zuschlag = 0
        gesamtpreis = ticket + zuschlag
elif 17 < alter <= 64:
    ticket = 11.00
    if dimension == True:
        zuschlag = 1.5
        gesamtpreis = ticket + zuschlag
    else:
        zuschlag = 0
        gesamtpreis = ticket + zuschlag
else:
    ticket = 8.00
    if dimension == True:
        zuschlag = 1.5
        gesamtpreis = ticket + zuschlag
    else:
        zuschlag = 0
        gesamtpreis = ticket + zuschlag


print(f"""Alter: {alter} Jahre
Ticketpreis: {ticket} €
3D-Zuschlag: {zuschlag} €
Gesamtpreis: {gesamtpreis} €""")