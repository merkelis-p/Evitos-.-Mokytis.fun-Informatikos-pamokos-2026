# U1. Suma ir vidurkis

n = int(input())
skaiciai = []
for i in range(n):
    x = int(input())
    skaiciai.append(x)

s = sum(skaiciai)
vidurkis = s / len(skaiciai)

print("Suma:", s)
print(f"Vidurkis: {vidurkis:.2f}")
