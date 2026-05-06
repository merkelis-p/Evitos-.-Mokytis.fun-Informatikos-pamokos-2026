# Evitos programavimo pamokos

Šioje repozitorijoje saugomi programavimo pamokų failai, užduotys ir pagalbinė medžiaga.
Kalba: **Python**. Atnaujinta: **2026-04-29**.

---

## Turinys

- [Evitos programavimo pamokos](#evitos-programavimo-pamokos)
  - [Turinys](#turinys)
  - [Aktualu Dabar](#aktualu-dabar)
  - [Namų Darbai](#namų-darbai)
    - [1. Sukelk visus praeitus namų darbus į GitHub](#1-sukelk-visus-praeitus-namų-darbus-į-github)
    - [2. Spręsk nd1.py — Krepšinio Sezono Kronika](#2-spręsk-nd1py--krepšinio-sezono-kronika)
    - [3. Įkelk viską į GitHub](#3-įkelk-viską-į-github)
  - [Svarbios Nuorodos](#svarbios-nuorodos)
  - [20260423 Pamokos Failai](#20260423-pamokos-failai)
  - [20260409-20260416 Pamokos Failai](#20260409-20260416-pamokos-failai)
  - [20260402 Pamokos Failai](#20260402-pamokos-failai)
  - [Senesnė Medžiaga](#senesnė-medžiaga)

---

## Aktualu Dabar

Dabartinis pagrindinis aplankas yra [20260423-pamoka](20260423-pamoka/).

Per pamoką dirbome su **sąrašais** (`list`). Namų darbas — „Krepšinio Sezono Kronika": [20260423-pamoka/nd1.py](20260423-pamoka/nd1.py).

---

## Namų Darbai

### 1. Sukelk visus praeitus namų darbus į GitHub

Pirmiausia įkelk viską, kas dar neįkelta (praeitos pamokos darbai).

Atidaryti **PowerShell**, eiti į repozitorijos aplanką:

```
cd C:\Users\evita\Evitos-.-Mokytis.fun-Informatikos-pamokos-2026
```

Tada:

```
git status
git add .
git commit -m "Praeitu pamoku namu darbai"
git push
```

Jei `git push` neveikia arba prašo slaptažodžio — žiūrėk gido skyrių apie SSH arba kreipkis pagalbos: [docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md](docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md)

### 2. Spręsk nd1.py — Krepšinio Sezono Kronika

Failas: [20260423-pamoka/nd1.py](20260423-pamoka/nd1.py)

Užduotis: [20260423-pamoka/ND_UZDUOTIS.md](20260423-pamoka/ND_UZDUOTIS.md)

Teorija: [20260423-pamoka/TEORIJA.md](20260423-pamoka/TEORIJA.md)

Tikrink savo sprendimą su checkeriu:

```
cd 20260423-pamoka
python3 checker.py -d nd1.py
python3 checker.py nd1.py
```

### 3. Įkelk viską į GitHub

Kai baigsi nd1.py, įkelk į GitHub:

```
git add .
git commit -m "Namu darbai 20260423"
git push
```

---

## Svarbios Nuorodos

| Kas | Kur |
|---|---|
| Git ir GitHub gidas (pradedantiems) | [docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md](docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md) |
| VS Code + Python paruošimas | [docs/VS_CODE_SETUP_GUIDE.md](docs/VS_CODE_SETUP_GUIDE.md) |
| Dabartinės pamokos užduotis | [20260423-pamoka/ND_UZDUOTIS.md](20260423-pamoka/ND_UZDUOTIS.md) |
| Dabartinės pamokos teorija | [20260423-pamoka/TEORIJA.md](20260423-pamoka/TEORIJA.md) |
| Dabartinės pamokos tikrintuvas | [20260423-pamoka/checker.py](20260423-pamoka/checker.py) |

---

## 20260423 Pamokos Failai

Tema: `list` (sąrašai) — kaupiamoji suma, atvirkštinis iteravimas, min/max, rikiavimas.

| Failas | Kam skirtas |
|---|---|
| [20260423-pamoka/ND_UZDUOTIS.md](20260423-pamoka/ND_UZDUOTIS.md) | Namų darbo užduotis „Krepšinio Sezono Kronika" |
| [20260423-pamoka/TEORIJA.md](20260423-pamoka/TEORIJA.md) | Teorija ir pseudokodas uždaviniui spręsti |
| [20260423-pamoka/nd1.py](20260423-pamoka/nd1.py) | Pagrindinis namų darbo failas |
| [20260423-pamoka/checker.py](20260423-pamoka/checker.py) | Tikrintuvas nd1.py |
| [20260423-pamoka/PAMOKA.md](20260423-pamoka/PAMOKA.md) | Pamokos teorija apie sąrašus |
| [20260423-pamoka/u1.py](20260423-pamoka/u1.py)–[u4.py](20260423-pamoka/u4.py) | Pratybų failai iš pamokos |

---

## 20260409-20260416 Pamokos Failai

Tema: `while`, `break`, `continue` — užduotis „Robotų Arena".

| Failas | Kam skirtas |
|---|---|
| [20260409-20260416-pamoka/ND_UZDUOTIS.md](20260409-20260416-pamoka/ND_UZDUOTIS.md) | Užduotis „Robotų Arena" |
| [20260409-20260416-pamoka/TEORIJA.md](20260409-20260416-pamoka/TEORIJA.md) | `while`, `break`, `continue`, duomenų nuskaitymas |
| [20260409-20260416-pamoka/nd1.py](20260409-20260416-pamoka/nd1.py) | Uždavinio failas |
| [20260409-20260416-pamoka/checker.py](20260409-20260416-pamoka/checker.py) | Tikrintuvas nd1.py |
| [20260409-20260416-pamoka/U_UZDUOTYS.md](20260409-20260416-pamoka/U_UZDUOTYS.md) | 4 pratybų užduotys |
| [20260409-20260416-pamoka/U_ATSAKYMAI.md](20260409-20260416-pamoka/U_ATSAKYMAI.md) | Atsakymai su paaiškinimais |
| [20260409-20260416-pamoka/u1.py](20260409-20260416-pamoka/u1.py)–[u4.py](20260409-20260416-pamoka/u4.py) | Pratybų failai |
| [20260409-20260416-pamoka/u_checker.py](20260409-20260416-pamoka/u_checker.py) | Tikrintuvas u1–u4 |

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



