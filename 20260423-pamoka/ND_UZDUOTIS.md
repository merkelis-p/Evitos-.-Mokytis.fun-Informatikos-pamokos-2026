# Krepšinio Sezono Kronika

**Maksimalus vertinimas — 30 taškų**

> **Failas:** kurk `nd1.py` tame pačiame aplanke  
> **Tikrinimas:** paleisk `checker.py`  
> **Formatas:** tik `stdin` / `stdout`

---

## Situacija

Tavo draugė Eglė veda savo krepšinio komandos statistiką. Ji užsirašo kiekvieno
mačo rezultatą: kiek taškų tame mače buvo pelnyta, kiek klaidų padaryta, kiek
baudų metimų pataikyta. Sezono pabaigoje ji nori gauti visą analizę.

Tavo programa turi:

1. apskaičiuoti **kaupiamąją sumą** — kiek taškų iš viso užpelnyta po kiekvieno mačo;
2. išvesti mačus **atvirkštine tvarka** (nuo paskutinio iki pirmojo);
3. rasti **pirmą mačą**, po kurio kaupiamoji suma viršijo `s` taškų;
4. rasti **ilgiausią pergalių seriją** iš eilės;
5. su `while` ciklu suskaičiuoti, kiek treniruočių reikia, kad komanda pasiektų
   sezono tikslą `t` (per treniruotę pelno `p` taškų);
6. rasti **geriausią mačą** (daugiausiai taškų) ir **blogiausią** (mažiausiai taškų);
7. surikiuoti mačus pagal taškus nuo didžiausio iki mažiausio — **lyderių lentelė**
   (naudojant parinkimo rikiavimo algoritmą, be Python `sort`).

---

## Kaip veikia kaupiamoji suma?

Tai yra bėganti suma — po kiekvieno mačo sudedi visus taškus iki šiol.

Pavyzdžiui, jei komanda pelnė: 80, 70, 90

- po 1-ojo mačo kaupiamoji suma = 80
- po 2-ojo mačo kaupiamoji suma = 80 + 70 = 150
- po 3-iojo mačo kaupiamoji suma = 150 + 90 = 240

---

## Įvestis

Pirmoje eilutėje pateikiami keturi sveikieji skaičiai:

- `n` — mačų skaičius per sezoną;
- `s` — taškų riba, kurią peržengus komanda oficialiai dominuoja lygoje;
- `t` — sezono tikslas (bendras taškų skaičius, kurį norima pasiekti);
- `p` — kiek taškų komanda pelno per vieną papildomą treniruotę.

Toliau pateikiamos `n` eilučių. Kiekvienoje eilutėje yra:

- priešininko pavadinimas `varzybos` — vienas žodis;
- tame mače pelnytų taškų skaičius `taskai`;
- padarytų klaidų skaičius `klaidos`;
- pataikytų baudų metimų skaičius `baudos`;
- ar laimėjo `laimejo`, kur `1` reiškia pergalę, `0` — pralaimėjimą.

Visi duomenys vienoje eilutėje atskirti tarpais.

---

## Taisyklės

### Kaupiamoji suma

Po kiekvieno mačo suskaičiuok, kiek **iš viso** taškų užpelnyta nuo sezono pradžios
iki to mačo imtinai. Tai yra visų iki šiol buvusių mačų taškų bėganti suma.

### Efektyvumas

Kiekvieno mačo efektyvumas = `taskai − klaidos + baudos`.

Efektyvumą išvesk **dviem skaitmenimis po kablelio**.

### Mačo įvertinimas

- jei efektyvumas ≥ 80 → `Puikus`
- jei efektyvumas ≥ 50 → `Geras`
- jei efektyvumas ≥ 20 → `Vidutinis`
- kitu atveju → `Silpnas`

### Lyderystės mačas

Rask **pirmą** mačą, po kurio kaupiamoji suma tapo griežtai didesnė nei `s`.
Jei to niekada neįvyko — spausdink `NERA`.

Naudok **vėliavėlę** (`rasta = False`), kaip mokėtės pamokoje.

### Ilgiausia pergalių serija

Pergalių serija — tai eilė iš eilės laimėtų mačų. Rask ilgiausią tokią eilę.

Pavyzdys: laimėjimai `1 0 1 1 1 0 1 1` → ilgiausia serija = 3.

Tau prireiks dviejų kintamųjų:
- `dabartine` — kiek laimėjimų dabar iš eilės (pradžioje = 0)
- `ilgiausia` — kiek daugiausia buvo iš eilės (pradžioje = 0)

### Treniruočių skaičiavimas

Jei bendras taškų skaičius (paskutinė kaupiamoji suma) jau pasiekė ar viršijo
tikslą `t` — treniruočių reikia `0`.

Kitu atveju su `while` ciklu skaičiuok, kiek kartų reikia pridėti `p` taškų,
kol kaupiamoji suma pasieks arba viršys `t`. Čia tikimasi `while` ciklo.

### Geriausias ir blogiausias mačas

Rask mačą, kuriame buvo pelnyta **daugiausiai** taškų (`taskai`), ir mačą,
kuriame **mažiausiai**. Jei keli mačai turi vienodai taškų — imk **pirmą** tokį.

Šių ieškoti reikia per pagrindinį `for` ciklą — lygindamas su kintamuoju,
kuriame saugai dabartinį geriausią / blogiausią (panašiai kaip U2 uždavinyje).

### Lyderių lentelė (rikiavimas)

Surikiuok mačus pagal pelnytų taškų skaičių (`taskai`) nuo **didžiausio** iki
**mažiausio**. Tada išvesk juos sunumeruotus.

Naudok **parinkimo rikiavimą** (selection sort). Idėja:

- Eini per sąrašą. Kiekvienoje pozicijoje `i` randi, kuriame indekse
  (nuo `i` iki galo) yra **didžiausias** `taskai`.
- Sukeiti tą elementą su elementu pozicijoje `i`.
- Po pirmo praėjimo — didžiausias yra pozicijoje 0.
- Po antro — antras didžiausias yra pozicijoje 1. Ir t. t.

**Svarbu:** mačo pavadinimas ir taškų skaičius turi judėti kartu. Turėk du
lygiagrečius sąrašus `macu_vardai` ir `macu_taskai` — sukeidamas elementą
vienoje vietoje, sukeisk ir kitame sąraše.

---

## Išvestis

Programa turi išvesti **tiksliai** tokį formatą.

Pirmiausia:

```
Macu_kronika:
```

Toliau — po vieną eilutę kiekvienam mačui ta pačia tvarka, kaip jie pateikti įvestyje:

```
varzybos taskai kaupiamoji efektyvumas ivertinimas
```

Po to palik **vieną tuščią eilutę** ir išvesk:

```
Atvirkstine_tvarka:
varzybos1 varzybos2 ...
```

(visi mačų pavadinimai vienoje eilutėje, nuo paskutinio iki pirmojo)

Po to palik **vieną tuščią eilutę** ir išvesk:

```
Sezono_analize:
Bendri_taskai: x
Lyderystes_macas: varzybos
Ilgiausia_serija: y
Treniruociu_iki_tikslo: z
Geriausias_macas: varzybos taskai
Blogiausias_macas: varzybos taskai
```

Po to palik **vieną tuščią eilutę** ir išvesk surikiuotą lyderių lentelę:

```
Lyderiu_lentele:
1. varzybos taskai
2. varzybos taskai
...
```

---

## Svarbios pastabos

1. Programa turi veikti su **bet kokiais teisingais testais**, ne tik su pavyzdžiu.
2. Neprirašyk papildomo teksto, kurio nėra aprašyme.
3. Mačų pavadinimai yra iš vieno žodžio.
4. Testai bus įvairūs, todėl negalima sprendimo pririšti prie konkrečių reikšmių.
5. Efektyvumas spausdinamas **dviem skaitmenimis po kablelio**.
6. `Atvirkstine_tvarka` eilutėje — **visi** `n` mačų pavadinimai vienoje eilutėje,
   atskirti tarpais. **Tam reikia sąrašo.**
7. Lyderių lentelei rikiuoti naudok du lygiagrečius sąrašus su selection sort.
8. Jei nei vienas mačas nelaimėtas — ilgiausia serija = 0.

---

## Ko čia tikrai prireiks

- `append()` ir sąrašo iteravimo;
- atvirkštinio iteravimo `range(len(...) - 1, -1, -1)`;
- bėgančios sumos kaupimo kintamuoju;
- vėliavėlės (`rasta = False`) pirmam radiniui;
- dviejų kintamųjų (`dabartine` ir `ilgiausia`) serijai;
- `while` ciklo;
- min/max radimo be `min()`/`max()` funkcijų;
- dviejų lygiagrečių sąrašų rikiavimo su selection sort.

---

## Pavyzdžiai

| Testas | stdin | stdout |
|---|---|---|
| 1 | `4 200 400 15`<br>`Zalgiris 85 5 10 1`<br>`Rytas 70 8 5 0`<br>`Wolves 90 3 12 1`<br>`Neptuno 60 10 8 1` | `Macu_kronika:`<br>`Zalgiris 85 85 90.00 Puikus`<br>`Rytas 70 155 67.00 Geras`<br>`Wolves 90 245 99.00 Puikus`<br>`Neptuno 60 305 58.00 Geras`<br>_(tuščia eilutė)_<br>`Atvirkstine_tvarka:`<br>`Neptuno Wolves Rytas Zalgiris`<br>_(tuščia eilutė)_<br>`Sezono_analize:`<br>`Bendri_taskai: 305`<br>`Lyderystes_macas: Wolves`<br>`Ilgiausia_serija: 2`<br>`Treniruociu_iki_tikslo: 7`<br>`Geriausias_macas: Wolves 90`<br>`Blogiausias_macas: Neptuno 60`<br>_(tuščia eilutė)_<br>`Lyderiu_lentele:`<br>`1. Wolves 90`<br>`2. Zalgiris 85`<br>`3. Rytas 70`<br>`4. Neptuno 60` |
| 2 | `3 300 250 20`<br>`Skycop 95 2 15 1`<br>`Legia 80 10 5 1`<br>`Barca 75 6 8 0` | `Macu_kronika:`<br>`Skycop 95 95 108.00 Puikus`<br>`Legia 80 175 75.00 Geras`<br>`Barca 75 250 77.00 Geras`<br>_(tuščia eilutė)_<br>`Atvirkstine_tvarka:`<br>`Barca Legia Skycop`<br>_(tuščia eilutė)_<br>`Sezono_analize:`<br>`Bendri_taskai: 250`<br>`Lyderystes_macas: NERA`<br>`Ilgiausia_serija: 2`<br>`Treniruociu_iki_tikslo: 0`<br>`Geriausias_macas: Skycop 95`<br>`Blogiausias_macas: Barca 75`<br>_(tuščia eilutė)_<br>`Lyderiu_lentele:`<br>`1. Skycop 95`<br>`2. Legia 80`<br>`3. Barca 75` |
| 3 | `5 500 600 10`<br>`Kaunas 50 15 5 0`<br>`Vilnius 60 10 8 0`<br>`Klaipeda 70 5 12 1`<br>`Siauliai 55 20 3 0`<br>`Panevezys 80 8 10 1` | `Macu_kronika:`<br>`Kaunas 50 50 40.00 Geras`<br>`Vilnius 60 110 58.00 Geras`<br>`Klaipeda 70 180 77.00 Geras`<br>`Siauliai 55 235 38.00 Geras`<br>`Panevezys 80 315 82.00 Puikus`<br>_(tuščia eilutė)_<br>`Atvirkstine_tvarka:`<br>`Panevezys Siauliai Klaipeda Vilnius Kaunas`<br>_(tuščia eilutė)_<br>`Sezono_analize:`<br>`Bendri_taskai: 315`<br>`Lyderystes_macas: NERA`<br>`Ilgiausia_serija: 1`<br>`Treniruociu_iki_tikslo: 29`<br>`Geriausias_macas: Panevezys 80`<br>`Blogiausias_macas: Kaunas 50`<br>_(tuščia eilutė)_<br>`Lyderiu_lentele:`<br>`1. Panevezys 80`<br>`2. Klaipeda 70`<br>`3. Vilnius 60`<br>`4. Siauliai 55`<br>`5. Kaunas 50` |

---

## Kaip bus tikrinama

`checker.py` tikrins ne vieną pavyzdį, o daug skirtingų testų:

- pavyzdinius testus (tie patys kaip aukščiau);
- ribinių atvejų testus (vienas mačas, visi pralaimėjimai, tikslas jau pasiektas ir kt.);
- slaptus testus su atsitiktiniais duomenimis.

Checkeris rodys:

- progresą pagal testų grupes;
- bendrą rezultatą;
- kurių kodo elementų (sąrašas, atvirkštinis iteravimas ir kt.) dar trūksta.
