# U3. Atvirkštinė eilė

n = int(input())
skaiciai = []
for i in range(n):
    x = int(input())
    skaiciai.append(x)

rez = ""
for i in range(len(skaiciai) - 1, -1, -1):
    if rez != "":
        rez = rez + " "
    rez = rez + str(skaiciai[i])

print(rez)
