# U3. Atvirkštinė eilė
# Nuskaityk n skaičių į sąrašą.
# Išvesk juos atvirkštine tvarka, vienoje eilutėje, atskirant tarpais.

# Tavo kodas žemiau:
listas = [1, 2, 3, 4]

for i in range(len(listas) - 1, -1, -1):
    print(listas[i], end=" ")

n = int(input())
skaiciai = []
for i in range(n):
    tmp = int(input())
    skaiciai.append(tmp)

for i in range(len(skaiciai) - 1, -1, -1):
    print(skaiciai[i], end=" ")






