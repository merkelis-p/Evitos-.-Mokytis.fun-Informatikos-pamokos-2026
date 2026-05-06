# U4. Elementai virš vidurkio
# Nuskaityk n skaičių į sąrašą.
# Apskaičiuok vidurkį, tada išvesk tik tuos skaičius, kurie griežtai didesni už vidurkį.
# Jei tokių nėra — išvesk "Nera".

# Tavo kodas žemiau:
n = int(input())
skaiciai = []
for i in range(n):
    tmp = int(input())
    skaiciai.append(tmp)

vidurkis = sum(skaiciai) / len(skaiciai)

yra_did = False
for i in skaiciai:
    if i > vidurkis:
        print(i)
        yra_did = True

if not yra_did:
    print("Nera")