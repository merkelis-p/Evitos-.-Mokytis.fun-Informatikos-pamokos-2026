n = int(input())

rastas = None

for _ in range(n):
    x = int(input())

    if x % 7 == 0:
        rastas = x
        break

if rastas is not None:
    print(rastas)
else:
    print("Nerasta")
