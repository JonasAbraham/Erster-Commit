temperatur = float(input("Wie viel Grad hat es? "))

if temperatur < 0:
    print("Gefroren!")
elif 0 <= temperatur <= 20:
    print("Kühl!")
elif 21 <= temperatur <= 30:
    print("Angenehm!")
elif temperatur > 30:
    print("Heiß!")
else:
    print("Perfekt!")