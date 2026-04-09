# Teorija: `for` ciklas, dalumas ir sekos

Pirmiausia perskaityk `ND_UZDUOTIS.md` ir tik po to pradėk spręsti `nd1.py`–`nd4.py`.

Šita teorija skirta padėti susidėlioti sprendimo žingsnius, bet ne duoti gatavus atsakymus.

---

## 1. `for` ciklas

`for` ciklas naudojamas tada, kai žinai, kiek kartų nori kartoti veiksmą.

Pavyzdys:

```python
for i in range(5):
    print(i)
```

Čia bus išvesta:

```text
0
1
2
3
4
```

---

## 2. `range()` naudojimas

### `range(n)`

```python
for i in range(5):
    print(i)
```

Reiškia: kartok nuo `0` iki `4`.

### `range(1, n + 1)`

```python
for i in range(1, 6):
    print(i)
```

Reiškia: kartok nuo `1` iki `5`.

### `range(a, b + 1)`

Jei reikia pereiti per visą intervalą nuo `a` iki `b`, dažniausiai reikės:

```python
for i in range(a, b + 1):
    ...
```

---

## 3. Kaip nuskaityti `n` reikšmių

Jei pirmoje eilutėje yra `n`, o po to eina dar `n` eilučių su skaičiais:

```python
n = int(input())

for _ in range(n):
    x = int(input())
    print(x)
```

`_` naudojamas tada, kai tau nereikia paties ciklo numerio.

---

## 4. Suma ir skaitikliai

Labai dažnas šablonas:

```python
suma = 0
kiekis = 0

for _ in range(n):
    x = int(input())
    suma += x

    if x % 2 == 0:
        kiekis += 1
```

Čia:

- `suma` kaupia bendrą sumą;
- `kiekis` skaičiuoja, kiek kartų įvyko tam tikra sąlyga.

---

## 5. Dalumas ir sąlygos

### Liekana su `%`

Jei skaičius dalinasi iš `k`, tai:

```python
x % k == 0
```

Pavyzdžiai:

```python
if x % 2 == 0:
    print("dalijasi iš 2")

if x % 3 == 0:
    print("dalijasi iš 3")
```

### `and`

Abi sąlygos turi būti teisingos.

```python
if x % 2 == 0 and x % 3 == 0:
    print("dalijasi ir iš 2, ir iš 3")
```

### `or`

Pakanka, kad būtų teisinga bent viena sąlyga.

```python
if x % 2 == 0 or x % 7 == 0:
    print("tinka")
```

### `if / elif / else`

Kai galimi keli skirtingi atvejai, dažnai reikia tokios struktūros:

```python
if salyga1:
    ...
elif salyga2:
    ...
else:
    ...
```

Tai ypač pravers `nd1.py` uždavinyje.

---

## 6. Kvadratas ir kvadratų suma

Skaičiaus kvadratą gali rasti taip:


```python
kvadratas = x ** 2
```

arba tiesiog taip:

```python
kvadratas = x * x
```

Jei nori kaupti kvadratų sumą:

```python
kvadratu_suma = 0

for _ in range(n):
    x = int(input())
    kvadratu_suma += x * x
```

---

## 7. Vidurkis ir formatavimas

Vidurkis skaičiuojamas taip:

```python
vidurkis = suma / n
```

kur `suma` yra visų skaičių suma, o `n` – kiekis.

Jei reikia tiksliai dviejų skaitmenų po kablelio:

```python
print(f"Vidurkis: {vidurkis:.2f}")
```

Pavyzdžiai:

- `4` turi būti spausdinama kaip `4.00`;
- `2.5` turi būti spausdinama kaip `2.50`.

---

## 8. Didžiausia ir mažiausia reikšmė

Kai reikia rasti didžiausią ir mažiausią reikšmę be sąrašų, patogu pradėti nuo pirmos reikšmės.

```python
n = int(input())

pirmas = int(input())
didziausias = pirmas
maziausias = pirmas

for _ in range(n - 1):
    x = int(input())

    if x > didziausias:
        didziausias = x

    if x < maziausias:
        maziausias = x
```

Po to amplitudė būtų:

```python
amplitude = didziausias - maziausias
```

---

## 9. Ankstesnė reikšmė

Jei reikia lyginti dabartinį skaičių su ankstesniu, turi saugoti ankstesnę reikšmę atskirame kintamajame.

Pavyzdžio idėja:

```python
n = int(input())

ankstesnis = int(input())
padidejimu = 0

for _ in range(n - 1):
    dabartinis = int(input())

    if dabartinis > ankstesnis:
        padidejimu += 1

    ankstesnis = dabartinis
```

Svarbu:

- pirmą reikšmę pasiimi prieš ciklą;
- ciklo gale `ankstesnis` atnaujinamas.

---

## 10. Kaip galvoti apie uždavinius

### ND1

1. Nuskaityk `n`.
2. Su `for` eik per skaičius nuo `1` iki `n`.
3. Kiekvienam skaičiui iš eilės patikrink 4 galimus atvejus.
4. Išvesk skaičių ir jo žymę.

### ND2

1. Nuskaityk `n`.
2. Pasiruošk `suma`, `kvadratu_suma` ir skaitiklį dalumui iš `3`.
3. Kartok `n` kartų.
4. Pabaigoje apskaičiuok vidurkį.

### ND3

1. Nuskaityk `a` ir `b`.
2. Su `for` eik per intervalą `a` iki `b`.
3. Tuo pačiu kaupti sumas ir skaitiklius.
4. Atkreipk dėmesį į sąlygą „dalijasi iš 3, bet nesidalina iš 5“.

### ND4

1. Nuskaityk `n`.
2. Pirmą reikšmę pasiimk prieš ciklą.
3. Iš jos pradėk `didziausias`, `maziausias` ir `ankstesnis`.
4. Likusias reikšmes lygink su tuo, ką jau turi.
5. Gale išvesk amplitudę ir padidėjimų skaičių.

---

## 11. Kaip tikrintis

### Su `-d` — rodo vieną pavyzdinę užduotį

Prarodo vieną testinį atvejį: kokia įvestis bus paduota ir koks output tikimasi. Tinka tada, kai dar tik rašai sprendimą ir nori pamatyti, ką programa turėtų atspausdinti.

```bash
python3 checker.py -d nd1.py
```

Visų failų pavyzdiniai atvejai:

```bash
python3 checker.py -d
```

### Be `-d` — tikrina visus testus

Paleidžia visus tris testinius atvejus ir parodo, ar programa duoda teisingus atsakymus. Naudok tada, kai manai, kad sprendimas jau veikia.

```bash
python3 checker.py nd2.py
```

Visi failai su visais testais:

```bash
python3 checker.py
```

Jei checkeris rodo, kad trūksta `for`, `and`, `or`, `*` ar kitų požymių, vadinasi svarbu ne tik gauti teisingą atsakymą, bet ir spręsti tuo būdu, kurio dabar mokaisi.



