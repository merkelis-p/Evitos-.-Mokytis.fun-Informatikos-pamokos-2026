a = int(input())
b = int(input())

for i in range(1, a + 1):
    eilute = ""

    for j in range(1, b + 1):
        if j > 1:
            eilute += " "
        eilute += str(i * j)

    print(eilute)
