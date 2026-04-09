# Išvesk skaičius nuo 1 iki 20


for i in range(1, 21):
    print(i)

print()

# Išvesk skaičius nuo 7 iki 23
for i in range(7, 24):
    print(i)


# Išvesk skaičius nuo 7 iki 23, kurie yra nelyginiai
x = 10

if (x % 2 == 0):
    print("Skaičius yra lyginis")
else:
    print("Skaičius yra nelyginis")

print()

for i in range(7, 24):
    if (i % 2 != 0):
        print(i)