# U2. Didžiausias ir jo pozicija

n = int(input())
skaiciai = []
for i in range(n):
    x = int(input())
    skaiciai.append(x)

didz = skaiciai[0]
poz = 0
for i in range(len(skaiciai)):
    if skaiciai[i] > didz:
        didz = skaiciai[i]
        poz = i

print("Didziausia:", didz)
print("Pozicija:", poz + 1)
