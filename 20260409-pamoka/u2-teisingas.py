n = int(input())

suma = 0
praleista = 0

for _ in range(n):
    x = int(input())

    if x <= 0:
        praleista += 1
        continue

    suma += x

print(f"Suma: {suma}")
print(f"Praleista: {praleista}")
