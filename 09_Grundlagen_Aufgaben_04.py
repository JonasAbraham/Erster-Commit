titel = "Trinity of Magic: 'A new beginning'"
seiten = 741
gelesen = True
seiten_pro_tag = 80
lesedauer = (seiten // seiten_pro_tag)  + 1

print(f"""Mein Lieblingsbuch ist {titel}, das Buch hat {seiten} Seiten. 
Habe ich es schon durchgelesen? {gelesen}!
Ich habe {seiten_pro_tag} Seiten pro Tag gelesen und {lesedauer} Tage gebraucht um es durchzulesen.""")