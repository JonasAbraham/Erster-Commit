einkaufsliste = ["Apfel", "Milch", "Brot", "Butter", "Käse"]
benutzereingabe = input("Bitte gib ein Lebensmittel ein: ")

if benutzereingabe in einkaufsliste:
    print(f"{benutzereingabe} ist auf der Liste.")
else:
    print(f"{benutzereingabe} fehlt auf der Liste")