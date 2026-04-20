# U4. Elementai virš vidurkio

n = int(input())
skaiciai = []
for i in range(n):
    x = int(input())
    skaiciai.append(x)

vidurkis = sum(skaiciai) / len(skaiciai)

rasta = False
for x in skaiciai:
    if x > vidurkis:
        print(x)
        rasta = True

if not rasta:
    print("Nera")
