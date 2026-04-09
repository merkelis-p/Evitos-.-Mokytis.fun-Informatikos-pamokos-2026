# Evitos programavimo pamokos

Šioje repozitorijoje saugomi programavimo pamokų failai, užduotys ir pagalbinė medžiaga.
Kalba: **Python**. Atnaujinta: **2026-04-08**.

---

## Turinys

- [Evitos programavimo pamokos](#evitos-programavimo-pamokos)
  - [Turinys](#turinys)
  - [Aktualu Dabar](#aktualu-dabar)
  - [Svarbios Nuorodos](#svarbios-nuorodos)
  - [Namų Darbas Kitai Pamokai](#namų-darbas-kitai-pamokai)
    - [1. GitHub pasiruošimas](#1-github-pasiruošimas)
    - [2. Jei dar neįkėlei senesnių namų darbų](#2-jei-dar-neįkėlei-senesnių-namų-darbų)
    - [3. Dabartinė pamoka: 4 mini uždaviniai](#3-dabartinė-pamoka-4-mini-uždaviniai)
    - [4. Kaip tikrintis](#4-kaip-tikrintis)
  - [20260402 Pamokos Failai](#20260402-pamokos-failai)
  - [Paruošta Kitai Pamokai](#paruošta-kitai-pamokai)
  - [Senesnė Medžiaga](#senesnė-medžiaga)

---

## Aktualu Dabar

Dabartinis pagrindinis aplankas yra [20260402-pamoka](20260402-pamoka/).

Šitos pamokos tema yra `for` ciklas ir jo jungimas su ankstesnėmis temomis:

- skaičių intervalais;
- dalumu ir keliomis sąlygomis vienu metu;
- `if / elif / else`;
- suma, kvadratų suma ir skaitikliais;
- didžiausios ir mažiausios reikšmės paieška;
- sekos pokyčių analizė.

Jei atsidarai repo ir nežinai nuo ko pradėti, pradėk nuo šitos sekos:

1. [20260402-pamoka/ND_UZDUOTIS.md](20260402-pamoka/ND_UZDUOTIS.md)
2. [20260402-pamoka/TEORIJA.md](20260402-pamoka/TEORIJA.md)
3. [20260402-pamoka/u1.py](20260402-pamoka/u1.py) – [20260402-pamoka/u4.py](20260402-pamoka/u4.py)
4. [20260402-pamoka/nd1.py](20260402-pamoka/nd1.py) – [20260402-pamoka/nd4.py](20260402-pamoka/nd4.py)
5. [20260402-pamoka/checker.py](20260402-pamoka/checker.py)

---

## Svarbios Nuorodos

| Kas | Kur |
|---|---|
| VS Code + Python paruošimas | [docs/VS_CODE_SETUP_GUIDE.md](docs/VS_CODE_SETUP_GUIDE.md) |
| Git + GitHub pradžios gidas | [docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md](docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md) |
| Dabartinės pamokos užduotys | [20260402-pamoka/ND_UZDUOTIS.md](20260402-pamoka/ND_UZDUOTIS.md) |
| Dabartinės pamokos teorija | [20260402-pamoka/TEORIJA.md](20260402-pamoka/TEORIJA.md) |
| Dabartinės pamokos tikrintuvas | [20260402-pamoka/checker.py](20260402-pamoka/checker.py) |
| Kitos pamokos ilga užduotis | [20260409-pamoka/ND_UZDUOTIS.md](20260409-pamoka/ND_UZDUOTIS.md) |
| Praėjusios pamokos medžiaga | [docs/20260326-pamoka.md](docs/20260326-pamoka.md) |

---

## Namų Darbas Kitai Pamokai

Iki kitos pamokos reikia atlikti šiuos žingsnius.

### 1. GitHub pasiruošimas

Perskaityk ir pasidaryk GitHub setup iki `SSH` dalies:

- [docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md](docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md)

Reikia:

1. Susikurti `GitHub` paskyrą.
2. Įsidiegti `Git`.
3. Susitvarkyti bazinį `git config`.
4. Išmokti `git clone`, `git status`, `git add`, `git commit`, `git push`, `git pull`.

### 2. Jei dar neįkėlei senesnių namų darbų

Jei dar neįkėlei 2026-03-26 pamokos namų darbų, jų aprašymai yra čia:

- [docs/20260326-pamoka.md](docs/20260326-pamoka.md)

Jei juos nori sukelti į repozitoriją, gali naudoti:

```bash
git status
git add .
git commit -m "Ikelti ankstesni namu darbai"
git push
```

### 3. Dabartinė pamoka: 4 mini uždaviniai

Dirbk tokia tvarka:

1. Perskaityk [20260402-pamoka/ND_UZDUOTIS.md](20260402-pamoka/ND_UZDUOTIS.md).
2. Perskaityk [20260402-pamoka/TEORIJA.md](20260402-pamoka/TEORIJA.md).
3. Jei reikia, pasižiūrėk į [20260402-pamoka/u1.py](20260402-pamoka/u1.py), [20260402-pamoka/u2.py](20260402-pamoka/u2.py), [20260402-pamoka/u3.py](20260402-pamoka/u3.py), [20260402-pamoka/u4.py](20260402-pamoka/u4.py).
4. Išspręsk [20260402-pamoka/nd1.py](20260402-pamoka/nd1.py), [20260402-pamoka/nd2.py](20260402-pamoka/nd2.py), [20260402-pamoka/nd3.py](20260402-pamoka/nd3.py) ir [20260402-pamoka/nd4.py](20260402-pamoka/nd4.py).

### 4. Kaip tikrintis

Su `-d` — parodo vieną pavyzdinį atvejį (ką turi atspausdinti programa). Naudok rašydama sprendimą:

```bash
cd 20260402-pamoka
python3 checker.py -d nd1.py
```

Be `-d` — paleidžia visus testus ir tikrina, ar atsakymai teisingi. Naudok kai manai, kad sprendimas jau veikia:

```bash
cd 20260402-pamoka
python3 checker.py nd1.py
```

Visų failų tikrinimas iš karto:

```bash
cd 20260402-pamoka
python3 checker.py
```

---

## 20260402 Pamokos Failai

| Failas | Kam skirtas |
|---|---|
| [20260402-pamoka/ND_UZDUOTIS.md](20260402-pamoka/ND_UZDUOTIS.md) | 4 matematiškesni mini uždaviniai |
| [20260402-pamoka/TEORIJA.md](20260402-pamoka/TEORIJA.md) | `for`, dalumo, intervalų ir sekų teorija |
| [20260402-pamoka/nd1.py](20260402-pamoka/nd1.py) | Mini uždavinys 1 |
| [20260402-pamoka/nd2.py](20260402-pamoka/nd2.py) | Mini uždavinys 2 |
| [20260402-pamoka/nd3.py](20260402-pamoka/nd3.py) | Mini uždavinys 3 |
| [20260402-pamoka/nd4.py](20260402-pamoka/nd4.py) | Mini uždavinys 4 |
| [20260402-pamoka/checker.py](20260402-pamoka/checker.py) | Tikrintuvas visiems 4 failams |
| [20260402-pamoka/u1.py](20260402-pamoka/u1.py) | `for` ciklo pradžios pavyzdžiai |
| [20260402-pamoka/u2.py](20260402-pamoka/u2.py) | `range()` ir intervalų pavyzdžiai |
| [20260402-pamoka/u3.py](20260402-pamoka/u3.py) | Suma ir vidurkis su `for` |
| [20260402-pamoka/u4.py](20260402-pamoka/u4.py) | `while` ir `for` palyginimas |

---

## Paruošta Kitai Pamokai

Ilga užduotis „Robotų Arena“ perkelta į [20260409-pamoka](20260409-pamoka/).

Ten šiuo metu yra:

- [20260409-pamoka/ND_UZDUOTIS.md](20260409-pamoka/ND_UZDUOTIS.md)
- [20260409-pamoka/TEORIJA.md](20260409-pamoka/TEORIJA.md)
- [20260409-pamoka/checker.py](20260409-pamoka/checker.py)
- [20260409-pamoka/nd1.py](20260409-pamoka/nd1.py)

---

## Senesnė Medžiaga

Senesnė su 2026-03-26 pamoka susijusi medžiaga ir namų darbų aprašymai perkelti į:

- [docs/20260326-pamoka.md](docs/20260326-pamoka.md)

Taip pagrindinis `README.md` lieka trumpas ir orientuotas į dabar aktualią užduotį.








