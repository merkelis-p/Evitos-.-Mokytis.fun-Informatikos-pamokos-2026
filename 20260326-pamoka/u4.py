metai = int(input("Iveskite kiek jums metu: "))

# < 18 - jaunas
# > 18 - 30 - apysenis
# > 30 - senas

if metai < 18:
    print('jaunas')
elif metai >= 18 and metai < 30:
    print('apysenis') 
else:
    print('senas')


if metai == 2:
    print("taip")
elif metai == 3:
    print("ne")
else:
    print("gal")

