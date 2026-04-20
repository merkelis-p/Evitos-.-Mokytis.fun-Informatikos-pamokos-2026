# Pamoka: sąrašai (`list`) ir ciklai su sąrašais

---

## Teorija

### 1. Kas yra sąrašas?

Sąrašas (`list`) — tai kintamasis, kuriame galima laikyti **kelis elementus** iš eilės.

Vietoj to, kad turėtum:

```python
a = 5
b = 8
c = 3
```

gali turėti vieną sąrašą:

```python
skaiciai = [5, 8, 3]
```

Elementai sąraše saugomi **eilės tvarka** ir kiekvienas turi **indeksą** — numerį, pradedantį nuo `0`.

---

### 2. Kaip sukurti sąrašą

Tuščias sąrašas:

```python
skaiciai = []
```

Sąrašas su iš anksto žinomis reikšmėmis:

```python
skaiciai = [10, 20, 30]
```

---

### 3. Kaip pridėti elementą: `append()`

`append()` prideda elementą į **sąrašo galą**:

```python
skaiciai = []
skaiciai.append(5)
skaiciai.append(8)
skaiciai.append(3)
# skaiciai dabar yra [5, 8, 3]
```

Taip dažniausiai pildome sąrašą cikle:

```python
n = int(input())
skaiciai = []
for i in range(n):
    x = int(input())
    skaiciai.append(x)
```

---

### 4. Kaip pasiekti elementą pagal indeksą

Indeksai prasideda nuo `0`:

```python
skaiciai = [10, 20, 30]
print(skaiciai[0])   # 10
print(skaiciai[1])   # 20
print(skaiciai[2])   # 30
```

Paskutinis elementas — indeksas `-1`:

```python
print(skaiciai[-1])  # 30
```

---

### 5. Sąrašo ilgis: `len()`

`len()` grąžina, kiek elementų yra sąraše:

```python
skaiciai = [10, 20, 30]
print(len(skaiciai))  # 3
```

---

### 6. Iteravimas per sąrašą su `for`

Paprasčiausias būdas pereiti visus elementus:

```python
skaiciai = [10, 20, 30]
for x in skaiciai:
    print(x)
```

Išvestis:

```
10
20
30
```

---

### 7. Iteravimas su indeksu

Jei reikia žinoti ir elemento **poziciją**, naudok `range(len(...))`:

```python
skaiciai = [10, 20, 30]
for i in range(len(skaiciai)):
    print(i, skaiciai[i])
```

Išvestis:

```
0 10
1 20
2 30
```

---

### 8. Naudingi sąrašo veiksmai

| Komanda | Ką daro |
|---|---|
| `len(s)` | Kiek elementų sąraše |
| `sum(s)` | Visų elementų suma |
| `min(s)` | Mažiausias elementas |
| `max(s)` | Didžiausias elementas |
| `s.append(x)` | Prideda `x` į galą |
| `s[i]` | Elementas indeksu `i` |
| `s[-1]` | Paskutinis elementas |

---

### 9. Kaip atspausdinti elementus vienoje eilutėje

Kartais reikia visus sąrašo elementus spausdinti vienoje eilutėje, atskirtus tarpais.

Per `for` ciklą:

```python
skaiciai = [1, 2, 3]
for x in skaiciai:
    print(x, end=" ")
print()  # eilutės pabaiga
```

Arba trumpiau su `join` (tinka kai elementai yra tekstas arba juos konvertuoji į tekstą):

```python
skaiciai = [1, 2, 3]
print(" ".join(str(x) for x in skaiciai))
```

---

## Uždaviniai

---

### U1. Suma ir vidurkis

Pateikiami `n` sveikųjų skaičių. Nuskaityk juos į sąrašą, tada apskaičiuok sumą ir vidurkį.

**Įvestis:**

Pirmoje eilutėje — `n` (teigiamas sveikasis skaičius). Toliau `n` eilučių, kiekvienoje vienas sveikasis skaičius.

**Išvestis:**

Dvi eilutės:

```
Suma: <suma>
Vidurkis: <vidurkis dviem dešimtainėmis vietomis>
```

**Pavyzdžiai:**

| stdin | stdout |
|---|---|
| `4`<br>`10`<br>`20`<br>`30`<br>`40` | `Suma: 100`<br>`Vidurkis: 25.00` |
| `3`<br>`1`<br>`2`<br>`3` | `Suma: 6`<br>`Vidurkis: 2.00` |
| `1`<br>`7` | `Suma: 7`<br>`Vidurkis: 7.00` |

**Ko reikia:**
- nuskaityti skaičius į sąrašą su `append()`
- panaudoti `len()` arba `sum()` nekeičiant sąrašo su papildomu ciklu

---

### U2. Didžiausias ir jo pozicija

Pateikiami `n` sveikųjų skaičių. Surask didžiausią skaičių ir jo poziciją sąraše (skaičiuojant nuo `1`). Jei didžiausias kartojasi kelis kartus — nurodyti pirmą.

**Įvestis:**

Pirmoje eilutėje — `n`. Toliau `n` eilučių, kiekvienoje vienas sveikasis skaičius.

**Išvestis:**

Dvi eilutės:

```
Didziausia: <reikšmė>
Pozicija: <pozicija>
```

**Pavyzdžiai:**

| stdin | stdout |
|---|---|
| `5`<br>`3`<br>`9`<br>`1`<br>`9`<br>`4` | `Didziausia: 9`<br>`Pozicija: 2` |
| `3`<br>`7`<br>`2`<br>`5` | `Didziausia: 7`<br>`Pozicija: 1` |
| `4`<br>`-3`<br>`-1`<br>`-7`<br>`-2` | `Didziausia: -1`<br>`Pozicija: 2` |

**Ko reikia:**
- nuskaityti į sąrašą
- eiti per sąrašą su indeksu (per `range(len(...))`)
- sekti, kuris indeksas turi didžiausią reikšmę

---

### U3. Atvirkštinė eilė

Pateikiami `n` sveikųjų skaičių. Išvesk juos **atvirkštine tvarka**, atskiriant tarpais, vienoje eilutėje.

**Įvestis:**

Pirmoje eilutėje — `n`. Toliau `n` eilučių, kiekvienoje vienas sveikasis skaičius.

**Išvestis:**

Viena eilutė su skaičiais atvirkštine tvarka, atskiriant tarpais.

**Pavyzdžiai:**

| stdin | stdout |
|---|---|
| `4`<br>`1`<br>`2`<br>`3`<br>`4` | `4 3 2 1` |
| `3`<br>`10`<br>`20`<br>`30` | `30 20 10` |
| `1`<br>`5` | `5` |

**Ko reikia:**
- nuskaityti į sąrašą
- eiti per sąrašą nuo paskutinio iki pirmo elemento — naudok `range` su neigiamu žingsniu arba eik per indeksus pradedant nuo `len-1`

---

### U4. Elementai virš vidurkio

Pateikiami `n` sveikųjų skaičių. Apskaičiuok vidurkį, tada išvesk visus skaičius, kurie **griežtai didesni** už vidurkį. Jei tokių nėra — išvesk `Nera`.

**Įvestis:**

Pirmoje eilutėje — `n`. Toliau `n` eilučių, kiekvienoje vienas sveikasis skaičius.

**Išvestis:**

Skaičiai atskirtose eilutėse (ta pačia tvarka kaip įvestyje), arba `Nera`.

**Pavyzdžiai:**

| stdin | stdout |
|---|---|
| `5`<br>`1`<br>`5`<br>`3`<br>`7`<br>`4` | `5`<br>`7` |
| `4`<br>`2`<br>`2`<br>`2`<br>`2` | `Nera` |
| `3`<br>`10`<br>`1`<br>`1` | `10` |

**Ko reikia:**
- nuskaityti į sąrašą
- apskaičiuoti vidurkį
- antru ciklu pereiti sąrašą ir atspausdinti tik tuos, kurie didesni už vidurkį
- sekti, ar buvo atspausdinta nors viena reikšmė









