# import math

preis = [2.5, 1.99, 3.49, 0.99]

# gesamtpreis = sum(preis)
# durchschnittspreis = gesamtpreis / len(preis)

# print(f"Der Gesamtpreis beträgt {gesamtpreis:.2f}")
# print(f"Der Durchschnittspreis beträgt {durchschnittspreis:.2f}")


gesamtpreis = 0

for preise in preis:
    gesamtpreis += preise
    durchschnittspreis = gesamtpreis / len(preis)
print(f"Der Gesamtpreis beträgt {gesamtpreis:.2f}")
print(f"Der Durchschnittspreis beträgt {durchschnittspreis:.2f}")