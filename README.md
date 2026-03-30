# Evitos programavimo pamokos

Šioje repozitorijoje saugomi visi **Evitos Š.** programavimo pamokų failai, namų darbų užduotys ir mokomoji medžiaga.
Kalba: **Python**. Atnaujinta: **2026-03-30**.

---

## Turinys

1. [Sparčios nuorodos](#sparčios-nuorodos)
2. [Repozitorijos struktūra](#repozitorijos-struktūra)
3. [Pamokų apžvalga](#pamokų-apžvalga)
4. [Teorija: duomenų tipai](#teorija-duomenų-tipai)
5. [Teorija: operatoriai](#teorija-operatoriai)
6. [Teorija: sąlyginė valdymo struktūra](#teorija-sąlyginė-valdymo-struktūra)
7. [Namų darbai](#namų-darbai)

---

## Sparčios nuorodos

| Kas | Kur |
|---|---|
| VS Code + Python konfigūravimo gidas | [docs/VS_CODE_SETUP_GUIDE.md](docs/VS_CODE_SETUP_GUIDE.md) |
| Pirma pamoka (2026-03-19) | [20260319-pamoka/main.py](20260319-pamoka/main.py) |
| Antra pamoka – klasės darbai (2026-03-26) | [20260326-pamoka/](20260326-pamoka/) |
| Namų darbai po 20260326 pamokos | [nd1.py](20260326-pamoka/nd1.py) – [nd6.py](20260326-pamoka/nd6.py) |

---

## Repozitorijos struktūra

```
.
├── README.md                    # esi čia – pagrindinis informacinis dokumentas
├── 20260319-pamoka/
│   └── main.py                  # pirmos pamokos kodas
├── 20260326-pamoka/
│   ├── u1.py                    # klasės darbas: duomenų tipai, input
│   ├── u2.py                    # klasės darbas: aritmetiniai operatoriai (skaičiuotuvas)
│   ├── u3.py                    # klasės darbas: palyginimas (lyginis / nelyginis)
│   ├── u4.py                    # klasės darbas: if / elif / else
│   ├── nd1.py                   # namų darbas 1: slaptažodžio sistema
│   ├── nd2.py                   # namų darbas 2: dalumo testas
│   ├── nd3.py                   # namų darbas 3: sekundės -> val / min / sek
│   ├── nd4.py                   # namų darbas 4: dviženklio skaičiaus analizė
│   ├── nd5.py                   # namų darbas 5: trikampio tikrinimas
│   └── nd6.py                   # namų darbas 6: keliamieji metai
└── docs/
    └── VS_CODE_SETUP_GUIDE.md   # VS Code ir Python diegimo gidas
```

---

## Pamokų apžvalga

### Pamoka 1 — 2026-03-19

Failas: [20260319-pamoka/main.py](20260319-pamoka/main.py)

Pirmoje pamokoje susipažinome su Python aplinka ir pagrindiniais principais:
- `print()` – teksto ir reikšmių spausdinimas
- Kintamieji ir jų keitimas
- Aritmetinės operacijos su kintamaisiais
- Bazinės funkcijos (trumpas pavyzdys)

---

### Pamoka 2 — 2026-03-26

Klasės darbų failai:

| Failas | Aprašymas |
|---|---|
| [u1.py](20260326-pamoka/u1.py) | `int`, `float`, `str`, `bool` tipai; `input()`; `type()` |
| [u2.py](20260326-pamoka/u2.py) | Aritmetiniai operatoriai: `+`, `-`, `*`, `/`, `%`, `**`, `//` |
| [u3.py](20260326-pamoka/u3.py) | Palyginimo operatorius `==`; lyginis / nelyginis tikrinimas |
| [u4.py](20260326-pamoka/u4.py) | `if`, `elif`, `else`; loginiai operatoriai `and`, `or` |

---

## Teorija: duomenų tipai

Python turi keturis pagrindinius paprastus duomenų tipus, kuriuos naudojame šiuo metu:

| Tipas | Pavadinimas | Pavyzdys |
|---|---|---|
| `int` | Sveikasis skaičius | `x = 5` |
| `float` | Dešimtainis skaičius | `y = 3.14` |
| `str` | Tekstas (eilutė) | `z = "labas"` |
| `bool` | Loginė reikšmė | `b = True` |

```python
x = 5          # int
y = 3.14       # float
z = "labas"    # str
b = True       # bool

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
```

**Tipo konvertavimas** (casting):
```python
n = int(input("Iveskite skaiciu: "))  # input() visada grąžina str -> verčiame į int
```

---

## Teorija: operatoriai

### Aritmetiniai operatoriai

| Operatorius | Operacija | Pavyzdys | Rezultatas |
|---|---|---|---|
| `+` | Sudėtis | `7 + 3` | `10` |
| `-` | Atimtis | `7 - 3` | `4` |
| `*` | Daugyba | `7 * 3` | `21` |
| `/` | Dalyba (dešimtainė) | `7 / 2` | `3.5` |
| `//` | Sveikoji dalyba | `7 // 2` | `3` |
| `%` | Liekana | `7 % 2` | `1` |
| `**` | Kėlimas laipsniu | `2 ** 8` | `256` |

```python
a, b = 7, 2
print(f"Dalyba: {a / b}")     # 3.5
print(f"Sveikoji: {a // b}")  # 3
print(f"Liekana: {a % b}")    # 1
print(f"Laipsnis: {a ** b}")  # 49
```

> **Patarimas:** `%` (liekana) labai dažnai naudojama norint patikrinti, ar skaičius dalinasi iš kito:
> `x % 2 == 0` → skaičius lyginis

### Palyginimo operatoriai

Palyginimas visada grąžina `True` arba `False`.

| Operatorius | Reikšmė | Pavyzdys | Rezultatas |
|---|---|---|---|
| `==` | Lygu | `5 == 5` | `True` |
| `!=` | Nelygu | `5 != 3` | `True` |
| `>` | Daugiau | `5 > 3` | `True` |
| `<` | Mažiau | `5 < 3` | `False` |
| `>=` | Daugiau arba lygu | `5 >= 5` | `True` |
| `<=` | Mažiau arba lygu | `4 <= 5` | `True` |

### Loginiai operatoriai

| Operatorius | Reikšmė | Pavyzdys |
|---|---|---|
| `and` | Ir (abu turi būti teisingi) | `x > 0 and x < 100` |
| `or` | Arba (bent vienas turi būti teisingas) | `x == 0 or x == 1` |
| `not` | Ne (apverčia loginę reikšmę) | `not (x > 0)` |

```python
x = 25
print(x >= 18 and x < 30)  # True – x yra tarp 18 ir 30
print(x < 0 or x > 100)    # False – nei viena salyga netenkinama
print(not (x > 0))         # False – x > 0 yra True, not apvercia i False
```

---

## Teorija: sąlyginė valdymo struktūra

`if`, `elif`, `else` leidžia programai priimti sprendimus.

### Sintaksė

```python
if <salyga>:
    # vykdoma, jei salyga True
elif <kita salyga>:
    # vykdoma, jei pirmoji False, bet si True
else:
    # vykdoma, jei visos salygos False
```

> **Svarbu:** Python naudoja **įtrauką (4 tarpai arba Tab)** vietoj skliaustų. Blokas prasideda po `:`.

### Pavyzdys

```python
amzius = int(input("Iveskite amziu: "))

if amzius < 18:
    print("Nepilnametis")
elif amzius < 65:
    print("Suauges")
else:
    print("Pensininkas")
```

### Įdėtinės sąlygos

```python
x = int(input("Skaicius: "))

if x % 2 == 0:
    print("Lyginis")
    if x > 100:
        print("...ir didesnis nei 100")
else:
    print("Nelyginis")
```

---

## Namų darbai

**Pirma užduotis:** Naudojantis gidu [docs/VS_CODE_SETUP_GUIDE.md](docs/VS_CODE_SETUP_GUIDE.md), pasiruošti darbui — susikonfigūruoti „Visual Studio Code" ir „Python" aplinką savo kompiuteryje.

Tada atlikti **6 mini programavimo uždavinius**. Kiekvienas uždavinys turi savo failą su aprašymu. Kodą rašyk tiesiai į tą failą, žemiau docstring teksto (kai `"""..."""` baigiasi).

---

### ND1 — Slaptažodžio sistema

Failas: [20260326-pamoka/nd1.py](20260326-pamoka/nd1.py)

**Užduotis:**
- Paprašyk vartotojo įvesti slaptažodį.
- Jei įvedė `"admin123"` → išvesk `"Prisijungta"`.
- Kitaip → išvesk `"Klaida"`.

**Naudojama:** `input()`, `if`, `else`, palyginimo operatorius `==`

---

### ND2 — Dalumo testas

Failas: [20260326-pamoka/nd2.py](20260326-pamoka/nd2.py)

**Užduotis:**
- Paprašyk vartotojo įvesti skaičių.
- Patikrink, ar jis dalinasi iš 2, 3 ir 5.
- Išvesk vieną iš šių atsakymų:
  - `"Dalinasi iš 2 ir 3"`
  - `"Dalinasi tik iš 2"`
  - `"Dalinasi tik iš 3"`
  - `"Dalinasi tik iš 5"`
  - `"Nesidalina nei iš 2, nei iš 3, nei iš 5"`

**Naudojama:** `input()`, `int()`, `%`, `==`, `if`, `elif`, `else`, `and`

---

### ND3 — Sekundės → valandos, minutės, sekundės

Failas: [20260326-pamoka/nd3.py](20260326-pamoka/nd3.py)

**Užduotis:**
- Paprašyk vartotojo įvesti sekundžių skaičių.
- Paversk į valandas, minutes ir likusias sekundes.

| Įvestis | Rezultatas |
|---|---|
| `135` | `0 val, 2 min, 15 sek` |
| `4953` | `1 val, 22 min, 33 sek` |

**Naudojama:** `//` (sveikoji dalyba), `%` (liekana)

> **Patarimas:**
> Naudok sveikąją dalybą ir liekanos operatorius gauti rezutatus.

---

### ND4 — Dviženklio skaičiaus analizė

Failas: [20260326-pamoka/nd4.py](20260326-pamoka/nd4.py)

**Užduotis:**
- Įvesk skaičių ir patikrink, ar jis **dviženklis** (nuo 10 iki 99).
- Jei ne → išvesk `"Skaičius nėra dviženklis"`.
- Jei taip → apskaičiuok:
  - ar lyginis / nelyginis
  - dešimčių skaitmenį
  - vienetų skaitmenį
  - skaitmenų sumą
  - kuris skaitmuo didesnis
  - atvirkštinį skaičių (apsuktais skaitmenimis)

**Naudojama:** `//`, `%`, `if`, `elif`, `else`, `and`, palyginimo operatoriai

> **Patarimas:**
> ```python
> desimtys = x // 10   # pvz. 74 // 10 = 7
> vienetai = x % 10    # pvz. 74 % 10 = 4
> ```

---

### ND5 — Trikampio tikrinimas

Failas: [20260326-pamoka/nd5.py](20260326-pamoka/nd5.py)

**Užduotis:**
- Paprašyk įvesti 3 trikampio kraštines: `a`, `b`, `c`.
- Patikrink, ar iš jų galima sudaryti trikampį.
- Trikampio taisyklė — kiekviena kraštinė turi būti mažesnė nei dviejų kitų suma:
  - `a + b > c`
  - `a + c > b`
  - `b + c > a`
- Išvesk `"Trikampis galimas"` arba `"Trikampis negalimas"`.

**Naudojama:** `input()`, `float()` arba `int()`, `>`, `and`, `if`, `else`

---

### ND6 — Keliamieji metai

Failas: [20260326-pamoka/nd6.py](20260326-pamoka/nd6.py)

**Užduotis:**
- Paprašyk įvesti metus.
- Nustatyk, ar jie **keliamieji**.

**Taisyklė:**
- Dalinasi iš 400 → keliamieji
- Dalinasi iš 4, bet nesidalina iš 100 → keliamieji
- Visais kitais atvejais → nekeliamieji

**Naudojama:** `%`, `==`, `!=`, `and`, `or`, `if`, `else`

---

## Namų darbų suvestinė

| # | Failas | Tema | Statusas |
|---|---|---|---|
| 1 | [nd1.py](20260326-pamoka/nd1.py) | Slaptažodžio sistema | ⬜ |
| 2 | [nd2.py](20260326-pamoka/nd2.py) | Dalumo testas | ⬜ |
| 3 | [nd3.py](20260326-pamoka/nd3.py) | Sekundės → val / min / sek | ⬜ |
| 4 | [nd4.py](20260326-pamoka/nd4.py) | Dviženklio skaičiaus analizė | ⬜ |
| 5 | [nd5.py](20260326-pamoka/nd5.py) | Trikampio tikrinimas | ⬜ |
| 6 | [nd6.py](20260326-pamoka/nd6.py) | Keliamieji metai | ⬜ |

> Atliktas = pakeisk ⬜ į ✅ arba pasakyk mokytojui!
