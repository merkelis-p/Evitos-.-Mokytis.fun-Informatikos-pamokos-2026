# Evitos programavimo pamokos

Šioje repozitorijoje saugomi programavimo pamokų failai, užduotys ir pagalbinė medžiaga.
Kalba: **Python**. Atnaujinta: **2026-04-10**.

---

## Turinys

- [Evitos programavimo pamokos](#evitos-programavimo-pamokos)
  - [Turinys](#turinys)
  - [Aktualu Dabar](#aktualu-dabar)
  - [Svarbios Nuorodos](#svarbios-nuorodos)
  - [Namų Darbai](#namų-darbai)
    - [0. git pull — pirmiausia](#0-git-pull--pirmiausia)
    - [1. Pabaik failų kėlimą į GitHub](#1-pabaik-failų-kėlimą-į-github)
    - [2. nd4.py — iš 20260402-pamoka](#2-nd4py--iš-20260402-pamoka)
    - [3. u1.py–u4.py — iš 20260409-pamoka](#3-u1pyu4py--iš-20260409-pamoka)
    - [4. nd1.py — iš 20260409-pamoka (pagrindinis fokusas)](#4-nd1py--iš-20260409-pamoka-pagrindinis-fokusas)
    - [5. Įkelk į GitHub](#5-įkelk-į-github)
  - [20260409 Pamokos Failai](#20260409-pamokos-failai)
  - [20260402 Pamokos Failai](#20260402-pamokos-failai)
  - [Senesnė Medžiaga](#senesnė-medžiaga)

---

## Aktualu Dabar

Dabartinis pagrindinis aplankas yra [20260409-pamoka](20260409-pamoka/).

Šitos pamokos tema yra `while` ciklas, `break`, `continue` ir ilgesnis `for` ciklo uždavinys su keliomis sąlygomis vienu metu.

Per pamoką kartu atlikome:

- `nd1.py`, `nd2.py`, `nd3.py` iš [20260402-pamoka](20260402-pamoka/).

Namų darbams liko:

1. `nd4.py` iš [20260402-pamoka](20260402-pamoka/)
2. `u1.py`–`u4.py` iš [20260409-pamoka](20260409-pamoka/)
3. `nd1.py` iš [20260409-pamoka](20260409-pamoka/) — pagrindinis fokusas

---

## Svarbios Nuorodos

| Kas | Kur |
|---|---|
| VS Code + Python paruošimas | [docs/VS_CODE_SETUP_GUIDE.md](docs/VS_CODE_SETUP_GUIDE.md) |
| Git + GitHub pradžios gidas | [docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md](docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md) |
| Šios pamokos užduotis (ilga) | [20260409-pamoka/ND_UZDUOTIS.md](20260409-pamoka/ND_UZDUOTIS.md) |
| Šios pamokos teorija | [20260409-pamoka/TEORIJA.md](20260409-pamoka/TEORIJA.md) |
| Šios pamokos tikrintuvas | [20260409-pamoka/checker.py](20260409-pamoka/checker.py) |
| Pamokos pratybų užduotys | [20260409-pamoka/U_UZDUOTYS.md](20260409-pamoka/U_UZDUOTYS.md) |
| Pamokos pratybų atsakymai | [20260409-pamoka/U_ATSAKYMAI.md](20260409-pamoka/U_ATSAKYMAI.md) |
| Pratybų tikrintuvas | [20260409-pamoka/u_checker.py](20260409-pamoka/u_checker.py) |
| Praėjusios pamokos užduotys | [20260402-pamoka/ND_UZDUOTIS.md](20260402-pamoka/ND_UZDUOTIS.md) |
| Praėjusios pamokos tikrintuvas | [20260402-pamoka/checker.py](20260402-pamoka/checker.py) |

---

## Namų Darbai

### 0. git pull — pirmiausia

Prieš pradėdama, gauk naujausius failus:

```
cd C:\Users\evita\Evitos-.-Mokytis.fun-Informatikos-pamokos-2026
git pull
```

### 1. Pabaik failų kėlimą į GitHub

Jei dar neįkėlei ankstesnių darbų:

```
git status
git add .
git commit -m "Ikelti ankstesni namu darbai"
git push
```

### 2. nd4.py — iš 20260402-pamoka

Failas: [20260402-pamoka/nd4.py](20260402-pamoka/nd4.py)

Užduotis: [20260402-pamoka/ND_UZDUOTIS.md](20260402-pamoka/ND_UZDUOTIS.md) (skyrius ND4).
Teorija: [20260402-pamoka/TEORIJA.md](20260402-pamoka/TEORIJA.md) (skyriai 8 ir 9).

```
cd 20260402-pamoka
python3 checker.py -d nd4.py
python3 checker.py nd4.py
```

### 3. u1.py–u4.py — iš 20260409-pamoka

Šiose užduotyse naudojamos dvi naujos komandos, kurių per pamoką nespėjome aptarti:

- **`break`** — iš karto išeina iš ciklo, net jei ciklas dar nesibaigė. Naudinga kai randi ko ieškojai ir toliau tikrinti nebereikia.
- **`continue`** — praleidžia likusią ciklo iteraciją ir šoka į kitą. Naudinga kai nori praleisti tam tikras reikšmes, bet tęsti ciklą toliau.

```python
for i in range(10):
    if i == 3:
        break      # sustoja ties 3, toliau nevykdo
    print(i)       # spausdina 0, 1, 2

for i in range(5):
    if i == 2:
        continue   # kai i==2, praleidi print ir eini toliau
    print(i)       # spausdina 0, 1, 3, 4
```

Užduotys: [20260409-pamoka/U_UZDUOTYS.md](20260409-pamoka/U_UZDUOTYS.md)

Stenkis išspręsti pati. Atsakymai: [20260409-pamoka/U_ATSAKYMAI.md](20260409-pamoka/U_ATSAKYMAI.md)

```
cd 20260409-pamoka
python3 u_checker.py -d u1.py
python3 u_checker.py u1.py
python3 u_checker.py
```

### 4. nd1.py — iš 20260409-pamoka (pagrindinis fokusas)

Failas: [20260409-pamoka/nd1.py](20260409-pamoka/nd1.py)

1. Perskaityk užduotį: [20260409-pamoka/ND_UZDUOTIS.md](20260409-pamoka/ND_UZDUOTIS.md)
2. Įsigilnk į teoriją: [20260409-pamoka/TEORIJA.md](20260409-pamoka/TEORIJA.md)
3. Spręsk pati — stenkis nekopijuoti kodo iš teorijos.

```
cd 20260409-pamoka
python3 checker.py -d nd1.py
python3 checker.py nd1.py
```

### 5. Įkelk į GitHub

```
git add .
git commit -m "Namu darbai 20260409"
git push
```

---

## 20260409 Pamokos Failai

| Failas | Kam skirtas |
|---|---|
| [20260409-pamoka/ND_UZDUOTIS.md](20260409-pamoka/ND_UZDUOTIS.md) | Ilga užduotis „Robotų Arena" |
| [20260409-pamoka/TEORIJA.md](20260409-pamoka/TEORIJA.md) | `while`, `break`, `continue`, duomenų nuskaitymas |
| [20260409-pamoka/nd1.py](20260409-pamoka/nd1.py) | Pagrindinis uždavinys |
| [20260409-pamoka/checker.py](20260409-pamoka/checker.py) | Tikrintuvas nd1.py |
| [20260409-pamoka/U_UZDUOTYS.md](20260409-pamoka/U_UZDUOTYS.md) | 4 pratybų užduotys |
| [20260409-pamoka/U_ATSAKYMAI.md](20260409-pamoka/U_ATSAKYMAI.md) | Atsakymai su paaiškinimais |
| [20260409-pamoka/u1.py](20260409-pamoka/u1.py)–[u4.py](20260409-pamoka/u4.py) | Pratybų failai |
| [20260409-pamoka/u_checker.py](20260409-pamoka/u_checker.py) | Tikrintuvas u1–u4 |

---

## 20260402 Pamokos Failai

| Failas | Kam skirtas |
|---|---|
| [20260402-pamoka/ND_UZDUOTIS.md](20260402-pamoka/ND_UZDUOTIS.md) | 4 mini uždaviniai (nd1–nd4) |
| [20260402-pamoka/TEORIJA.md](20260402-pamoka/TEORIJA.md) | `for`, dalumas, intervalai, sekos |
| [20260402-pamoka/nd1.py](20260402-pamoka/nd1.py)–[nd4.py](20260402-pamoka/nd4.py) | Uždavinių failai |
| [20260402-pamoka/checker.py](20260402-pamoka/checker.py) | Tikrintuvas nd1–nd4 |
| [20260402-pamoka/u1.py](20260402-pamoka/u1.py)–[u4.py](20260402-pamoka/u4.py) | Klasės pavyzdžiai |

---

## Senesnė Medžiaga

- [docs/20260326-pamoka.md](docs/20260326-pamoka.md) — 2026-03-26 pamokos namų darbai
- [docs/VS_CODE_SETUP_GUIDE.md](docs/VS_CODE_SETUP_GUIDE.md) — VS Code diegimas
- [docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md](docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md) — Git/GitHub gidas


