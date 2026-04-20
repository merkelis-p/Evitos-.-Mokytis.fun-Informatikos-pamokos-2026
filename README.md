# Evitos programavimo pamokos

Šioje repozitorijoje saugomi programavimo pamokų failai, užduotys ir pagalbinė medžiaga.
Kalba: **Python**. Atnaujinta: **2026-04-20**.

---

## Turinys

- [Evitos programavimo pamokos](#evitos-programavimo-pamokos)
  - [Turinys](#turinys)
  - [Aktualu Dabar](#aktualu-dabar)
  - [Namų Darbai](#namų-darbai)
    - [0. Pirmiausia — perskaityk atnaujintą Git gidą](#0-pirmiausia--perskaityk-atnaujintą-git-gidą)
    - [1. Sukelk visus praeitus namų darbus į GitHub](#1-sukelk-visus-praeitus-namų-darbus-į-github)
    - [2. Pabaik nd1.py — ten kur pabaigėme](#2-pabaik-nd1py--ten-kur-pabaigėme)
    - [2. Perskaityti naują teoriją — sąrašai](#2-perskaityti-naują-teoriją--sąrašai)
    - [3. Įkelk viską į GitHub](#3-įkelk-viską-į-github)
  - [Svarbios Nuorodos](#svarbios-nuorodos)
  - [20260409-20260416 Pamokos Failai](#20260409-20260416-pamokos-failai)
  - [20260423 Pamokos Failai](#20260423-pamokos-failai)
  - [20260402 Pamokos Failai](#20260402-pamokos-failai)
  - [Senesnė Medžiaga](#senesnė-medžiaga)

---

## Aktualu Dabar

Dabartinis pagrindinis aplankas yra [20260409-20260416-pamoka](20260409-20260416-pamoka/).

Per pamoką kartu pradėjome spręsti `nd1.py` — „Robotų Arena". Baigti reikia namuose.

Kita pamoka (20260423) bus skirta **sąrašams** (`list`). Ta pamokos medžiaga jau yra [20260423-pamoka/PAMOKA.md](20260423-pamoka/PAMOKA.md).

---

## Namų Darbai

### 0. Pirmiausia — perskaityk atnaujintą Git gidą

Git gidas buvo papildytas — dabar yra skyrius **„Terminalas ir navigacija"**, kuriame aiškiai paaiškinta:

- kaip atidaryti PowerShell;
- kas yra `pwd`, `ls`, `cd`, `cd ..`;
- kaip eiti iki repozitorijos aplanko.

Perskaityk čia: [docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md](docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md)

### 1. Sukelk visus praeitus namų darbus į GitHub

Kaip tai padaryti:

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

Jei `git push` neveikia arba prašo slaptažodžio — žiūrėk gido skyrių apie SSH arba kreipkis pagalbos.

### 2. Pabaik nd1.py — ten kur pabaigėme

Failas: [20260409-20260416-pamoka/nd1.py](20260409-20260416-pamoka/nd1.py)

Tęsk nuo tos vietos, kur baigėme per pamoką. Užduotis: [20260409-20260416-pamoka/ND_UZDUOTIS.md](20260409-20260416-pamoka/ND_UZDUOTIS.md). Teorija: [20260409-20260416-pamoka/TEORIJA.md](20260409-20260416-pamoka/TEORIJA.md).

```
cd 20260409-20260416-pamoka
python3 checker.py -d nd1.py
python3 checker.py nd1.py
```

### 2. Perskaityti naują teoriją — sąrašai

Prieš kitą pamoką perskaityk: [20260423-pamoka/PAMOKA.md](20260423-pamoka/PAMOKA.md)

Ten yra visa teorija apie `list` — kas tai yra, kaip naudoti, taip pat yra ir 4 uždaviniai, bet su jais dirbsime per pamoką, todėl dabar juos spręsti nėra būtina.

### 3. Įkelk viską į GitHub

Kai baigsi nd1.py, įkelk į GitHub:

```
git add .
git commit -m "Namu darbai 20260409-20260416"
git push
```

Patikslinau dabar Git gidą, paaiškinantį, kur ir kada naudoti Git komandas: [docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md](docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md)

---

## Svarbios Nuorodos

| Kas | Kur |
|---|---|
| Git ir GitHub gidas (pradedantiems) | [docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md](docs/GIT_GITHUB_PRADEDANCIOJO_GIDAS.md) |
| VS Code + Python paruošimas | [docs/VS_CODE_SETUP_GUIDE.md](docs/VS_CODE_SETUP_GUIDE.md) |
| Dabartinės pamokos užduotis | [20260409-20260416-pamoka/ND_UZDUOTIS.md](20260409-20260416-pamoka/ND_UZDUOTIS.md) |
| Dabartinės pamokos teorija | [20260409-20260416-pamoka/TEORIJA.md](20260409-20260416-pamoka/TEORIJA.md) |
| Dabartinės pamokos tikrintuvas | [20260409-20260416-pamoka/checker.py](20260409-20260416-pamoka/checker.py) |
| Kitos pamokos medžiaga (sąrašai) | [20260423-pamoka/PAMOKA.md](20260423-pamoka/PAMOKA.md) |

---

## 20260409-20260416 Pamokos Failai

Dvi pamokos skirtos tai pačiai temai: `while`, `break`, `continue` ir ilgesnė užduotis.

| Failas | Kam skirtas |
|---|---|
| [20260409-20260416-pamoka/ND_UZDUOTIS.md](20260409-20260416-pamoka/ND_UZDUOTIS.md) | Ilga užduotis „Robotų Arena" |
| [20260409-20260416-pamoka/TEORIJA.md](20260409-20260416-pamoka/TEORIJA.md) | `while`, `break`, `continue`, duomenų nuskaitymas |
| [20260409-20260416-pamoka/nd1.py](20260409-20260416-pamoka/nd1.py) | Pagrindinis uždavinys — tęsti namuose |
| [20260409-20260416-pamoka/checker.py](20260409-20260416-pamoka/checker.py) | Tikrintuvas nd1.py |
| [20260409-20260416-pamoka/U_UZDUOTYS.md](20260409-20260416-pamoka/U_UZDUOTYS.md) | 4 pratybų užduotys |
| [20260409-20260416-pamoka/U_ATSAKYMAI.md](20260409-20260416-pamoka/U_ATSAKYMAI.md) | Atsakymai su paaiškinimais |
| [20260409-20260416-pamoka/u1.py](20260409-20260416-pamoka/u1.py)–[u4.py](20260409-20260416-pamoka/u4.py) | Pratybų failai |
| [20260409-20260416-pamoka/u_checker.py](20260409-20260416-pamoka/u_checker.py) | Tikrintuvas u1–u4 |

---

## 20260423 Pamokos Failai

Kitos pamokos tema — `list` (sąrašai).

| Failas | Kam skirtas |
|---|---|
| [20260423-pamoka/PAMOKA.md](20260423-pamoka/PAMOKA.md) | Teorija ir 4 uždaviniai apie sąrašus |
| [20260423-pamoka/u1.py](20260423-pamoka/u1.py)–[u4.py](20260423-pamoka/u4.py) | Uždavinių failai |

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



