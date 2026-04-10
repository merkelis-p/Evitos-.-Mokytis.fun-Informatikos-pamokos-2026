# 4 mini uždaviniai: skaičiai, dalumas ir sekos

Šiame aplanke yra 4 trumpi, bet kiek rimtesni uždaviniai, skirti įtvirtinti:

- `for` ciklą;
- `range()` naudojimą;
- `if / elif / else`;
- dalumą;
- sumą ir skaitiklius;
- intervalo analizę;
- didžiausios ir mažiausios reikšmės paiešką;
- darbą su gretimomis sekos reikšmėmis.

Failai:

- `nd1.py`
- `nd2.py`
- `nd3.py`
- `nd4.py`
- `checker.py`

Jei stringi, pasižiūrėk į klasės pavyzdžius tame pačiame aplanke:

- `u1.py`
- `u2.py`
- `u3.py`
- `u4.py`

---

## ND1 — Dalumo lentelė

Failas: `nd1.py`

Tavo programa turi pereiti per visus skaičius nuo `1` iki `n` ir kiekvienam skaičiui parašyti, kaip jis dalinasi iš `2` ir `3`.

### Taisyklės

- jei skaičius dalinasi ir iš `2`, ir iš `3`, išvesk `dalijasi_2_ir_3`;
- jei dalinasi tik iš `2`, išvesk `dalijasi_2`;
- jei dalinasi tik iš `3`, išvesk `dalijasi_3`;
- kitu atveju išvesk `nesidalija`.

### Įvestis

Vienas sveikasis skaičius `n`.

### Išvestis

Po vieną eilutę kiekvienam skaičiui nuo `1` iki `n`:

```text
skaicius zyme
```

### Pavyzdys

| stdin | stdout |
|---|---|
| `6` | `1 nesidalija`<br>`2 dalijasi_2`<br>`3 dalijasi_3`<br>`4 dalijasi_2`<br>`5 nesidalija`<br>`6 dalijasi_2_ir_3` |

---

## ND2 — Kvadratų statistika

Failas: `nd2.py`

Duota `n` sveikųjų skaičių. Tavo programa turi:

- apskaičiuoti visų skaičių sumą;
- apskaičiuoti jų kvadratų sumą;
- suskaičiuoti, kiek skaičių dalinasi iš `3`;
- apskaičiuoti skaičių vidurkį.

### Įvestis

Pirmoje eilutėje pateikiamas sveikasis skaičius `n`.

Toliau pateikiamos `n` eilutės. Kiekvienoje eilutėje yra vienas sveikasis skaičius.

### Išvestis

Išvesk tiksliai tokį formatą:

```text
Suma: x
Kvadratu_suma: y
Dalinasi_is_3: z
Vidurkis: w
```

Vidurkį išvesk dviem skaitmenimis po kablelio.

### Pavyzdys

| stdin | stdout |
|---|---|
| `4`<br>`2`<br>`-3`<br>`5`<br>`6` | `Suma: 10`<br>`Kvadratu_suma: 74`<br>`Dalinasi_is_3: 2`<br>`Vidurkis: 2.50` |

---

## ND3 — Intervalo analizė

Failas: `nd3.py`

Duoti du sveikieji skaičiai `a` ir `b`. Reikia išnagrinėti visus skaičius intervale nuo `a` iki `b` imtinai.

Tavo programa turi:

- apskaičiuoti visų intervalo skaičių sumą;
- apskaičiuoti lyginių intervalo skaičių sumą;
- suskaičiuoti, kiek skaičių dalinasi iš `3`, bet nesidalina iš `5`;
- suskaičiuoti, kiek skaičių dalinasi iš `2` arba iš `7`.

### Įvestis

Pirmoje eilutėje pateikiamas sveikasis skaičius `a`.

Antroje eilutėje pateikiamas sveikasis skaičius `b`.

Galima laikyti, kad visada `a <= b`.

### Išvestis

Išvesk tiksliai tokį formatą:

```text
Suma: x
Lyginiu_suma: y
Dalijasi_3_bet_ne_5: z
Dalijasi_2_arba_7: w
```

### Pavyzdys

| stdin | stdout |
|---|---|
| `3`<br>`9` | `Suma: 42`<br>`Lyginiu_suma: 18`<br>`Dalijasi_3_bet_ne_5: 3`<br>`Dalijasi_2_arba_7: 4` |

---

## ND4 — Sekos pokyčiai

Failas: `nd4.py`

Duota skaičių seka. Tavo programa turi:

- rasti didžiausią sekos reikšmę;
- rasti mažiausią sekos reikšmę;
- apskaičiuoti amplitudę, tai yra skirtumą tarp didžiausios ir mažiausios reikšmės;
- suskaičiuoti, kiek kartų sekoje skaičius padidėjo, lyginant su prieš tai buvusiu skaičiumi.

Padidėjimu laikome atvejį, kai dabartinis skaičius yra griežtai didesnis už ankstesnį.

### Įvestis

Pirmoje eilutėje pateikiamas sveikasis skaičius `n`.

Toliau pateikiamos `n` eilutės. Kiekvienoje eilutėje yra vienas sveikasis skaičius.

Galima laikyti, kad `n` visada yra bent `1`.

### Išvestis

Išvesk tiksliai tokį formatą:

```text
Didziausias: x
Maziausias: y
Amplitude: z
Padidejimu: w
```

### Pavyzdys

| stdin | stdout |
|---|---|
| `5`<br>`4`<br>`7`<br>`7`<br>`2`<br>`9` | `Didziausias: 9`<br>`Maziausias: 2`<br>`Amplitude: 7`<br>`Padidejimu: 2` |

---

## Svarbios pastabos

1. Spręsk su `for` ciklais.
2. Neprirašyk papildomo teksto, kurio nėra aprašyme.
3. Jei reikia vidurkio, spausdink jį dviem skaitmenimis po kablelio.
4. `nd4.py` uždavinyje pravers prisiminti, kaip saugoti ankstesnę reikšmę.

---

## Kaip bus tikrinama

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
python3 checker.py nd3.py
```

Visi failai su visais testais:

```bash
python3 checker.py
```

Checkeris tikrins:

- ar sprendimai duoda teisingą `output`;
- ar panaudotas `for` ciklas;
- ar yra reikalingi kalbos elementai pagal užduoties tipą.




