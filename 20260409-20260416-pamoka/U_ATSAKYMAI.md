# Atsakymai ir paaiškinimai: `while`, `for`, `continue`, `break`, ciklas cikle

---

## U1. Mokėjimų planas — `while` ciklas

### Sprendimas

```python
S = int(input())
P = int(input())

menesiai = 0

while S > 0:
    S -= P
    menesiai += 1

print(menesiai)
```

### Kaip veikia

`while` ciklas tęsiasi tol, kol sąlyga teisinga. Čia — kol skola `S > 0`.

Kiekvieno žingsnio eigoje:
- atimame mėnesinį mokestį `P` iš skolos `S`;
- padidinamas mėnesių skaitiklis.

Kai `S` tampa nulis arba mažesnis, ciklas baigiasi.

### Ryšys su nd1.py

Boss level etape reikia skaičiuoti, kiek treniruočių silpniausia komanda turi praeiti, kad pasiektų finalo ribą. Tai lygiai tas pats `while` šablonas:

```python
while taskai < r:
    taskai += p
    treniruociu += 1
```

---

## U2. Teigiamų filtras — `for` + `continue`

### Sprendimas

```python
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
```

### Kaip veikia

`continue` iš karto pereina prie kito ciklo žingsnio — viskas po jo toje iteracijoje nevykdoma.

Kai `x <= 0`:
- padidiname `praleista`;
- `continue` praleidžia `suma += x`.

Kai `x > 0` — `continue` nepaleidžiamas, `suma` padidinama.

### Ryšys su nd1.py

Diskvalifikuotas komandas galima praleisti lygiai taip pat:

```python
if diskvalifikuota:
    continue
```

Tada visas tolimesnis tos komandos apdorojimas (finalistų tikrinimas, silpniausios paieška ir t. t.) bus praleistas automatiškai.

---

## U3. Pirmas tinkamas — `for` + `break`

### Sprendimas

```python
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
```

### Kaip veikia

`break` iš karto sustabdo visą `for` ciklą — net jei dar liko neskaityti skaičiai.

Radus pirmą tinkamą skaičių, jo reikšmė išsaugoma kintamajame `rastas` ir ciklas baigiamas.

Jei ciklas paėjo per visus skaičius ir `break` niekada nebuvo paliestas — `rastas` lieka `None`.

### Ryšys su nd1.py

Komandų radaras reikalauja rasti pirmą komandą, kuri surinko daugiau nei 90 taškų. Tas pats šablonas:

```python
if pirma_virs_90 == "NERA" and galutiniai > 90:
    pirma_virs_90 = vardas
```

Čia `break` negalima naudoti, nes likę duomenys dar reikalingi — todėl vietoj `break` naudojamas sąlygos patikrinimas `== "NERA"`.

---

## U4. Daugybos lentelė — ciklas cikle

### Sprendimas

```python
a = int(input())
b = int(input())

for i in range(1, a + 1):
    eilute = ""

    for j in range(1, b + 1):
        if j > 1:
            eilute += " "
        eilute += str(i * j)

    print(eilute)
```

### Alternatyvus sprendimas su `end`

```python
a = int(input())
b = int(input())

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if j < b:
            print(i * j, end=" ")
        else:
            print(i * j)
```

### Kaip veikia

Išorinis ciklas eina per eilutes (`i` — eilutės numeris).
Vidinis ciklas eina per stulpelius (`j` — stulpelio numeris).

Kiekviename žingsnyje spausdinamas sandaugos `i * j` rezultatas.

Svarbu: tarpas dedamas tarp skaičių, bet ne po paskutinio.

### Ryšys su nd1.py

Šiame uždavinyje ciklo cikle tiesiogiai nereikia, bet supratimas apie tai, kad vidinis ciklas pilnai pasibaigė prieš pereinant prie kito išorinio žingsnio, padeda suprasti, kaip veikia pagrindinė `for` eilutė su keliais `if` sakiniais viduje.
