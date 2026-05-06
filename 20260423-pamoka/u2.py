# U2. Didžiausias ir jo pozicija
# Nuskaityk n skaičių į sąrašą.
# Išvesk didžiausią reikšmę ir jos poziciją (nuo 1).

# Tavo kodas žemiau:

n = int(input())
skaiciai = []
for i in range(n):
    tmp = int(input())
    skaiciai.append(tmp)

didz = skaiciai[0]
didz_ind = 0
for i in range(1, n+1):
    if  skaiciai[i] > didz:
        didz = skaiciai[i]
        didz_int = i

print(f"Didziausia reiksme : {didz}")
print(f"Didziausios pozicija: {didz_ind+1}")
