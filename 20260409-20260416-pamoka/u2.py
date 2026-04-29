# U2. Teigiamų filtras
# Įvestis: n, po to n skaičių
# Išvestis: teigiamų suma ir kiek praleista (nuliai + neigiami)
# Reikia naudoti: for, continue

# Tavo kodas žemiau
n = int(input())

suma = 0
praleista = 0

for _ in range(n):
    skaicius = int(input())
    
    if skaicius <= 0:
        praleista += 1
        continue
    
    suma += skaicius

print(suma, praleista)
