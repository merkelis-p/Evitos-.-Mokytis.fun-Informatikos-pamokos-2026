


for i in range(5):
    print(i) # 0, 1, 2, 3, 4

for i in range(5):
    print("Hello, World!") # Hello, World! (5 times)

for _ in range(5):
    print("Hello, World!") # Hello, World! (5 times)

for i in range(5):
    print(f"{i+1}. Hello, World!") # n. Hello, World! (5 times)

print()

for i in range(1, 6):
    print(f"{i}. Hello, World!") # n. Hello, World! (5 times)


print()

suma = 0

for i in range(1, 6):
    suma += i # suma = suma + i

print(f"Suma: {suma}")

# 1+2+3+4+5 = 15