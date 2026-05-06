# U1. Suma ir vidurkis
# Nuskaityk n skaičių į sąrašą.
# Išvesk sumą ir vidurkį (dviem dešimtainėmis vietomis).

# Tavo kodas žemiau:

n = int(input())
skaiciai = []
for i in range(n):
    b = int(input())
    skaiciai.append(b)

suma = sum(skaiciai)
vidurkis = suma / n

print(f"Suma: {suma:.2f}")
print(f"Vidurkis: {vidurkis:.2f}")




# U5. Suma ir vidurkis
# Skaityk skaičius į sąrašą, kol negausim neigiamos reikšmės. Neigiamos reikšmės nevesk į sąrašą.
# Išvesk sumą ir vidurkį (dviem dešimtainėmis vietomis).


skaiciai = []
kiekis = 0
while True:
    tmp = int(input())
    if tmp < 0:
        break
    else:
        skaiciai.append(tmp)
        kiekis += 1

suma = sum(skaiciai)
vidurkis = suma / len(skaiciai)
vidurkis_su_kiekiu = suma / kiekis

print(f"Suma: {suma:.2f}")
print(f"Vidurkis: {vidurkis:.2f}")

