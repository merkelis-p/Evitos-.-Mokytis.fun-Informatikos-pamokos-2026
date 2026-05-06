# Teorija namų darbui

Pirmiausia perskaityk visą užduoties aprašymą `ND_UZDUOTIS.md`.

Šis failas nėra sprendimas. Čia sudėti bendri pavyzdžiai, kaip naudoti tuos pačius
programavimo įrankius, kurių prireiks namų darbe. Pavyzdžiai sąmoningai pateikti
kitame kontekste, kad matytum principą, o ne kopijuotum atsakymą.

---

## 1. Kaip pačiai susidėlioti sprendimą

Šioje užduotyje kiekviena išvesties dalis atsiranda iš konkretaus veiksmo. Todėl
patogu ne bandyti viską parašyti iš karto, o eiti per užduoties reikalavimus ir
paklausti: kokių duomenų tam reikia, kada juos turiu ir kurį pavyzdį iš teorijos
galiu pritaikyti?

Pirmiausia reikia nuskaityti pirmą įvesties eilutę. Joje yra keli skaičiai vienoje
eilutėje, todėl čia tinka [3 skyrius apie kelių skaičių nuskaitymą](#3-kaip-nuskaityti-kelis-skaičius-vienoje-eilutėje).
Toliau kiekviena mačo eilutė turi ir tekstą, ir skaičius, todėl ją skaityk taip,
kaip parodyta [4 skyriuje apie mišrius duomenis](#4-kaip-nuskaityti-mišrius-duomenis).

Kai užduotis prašo išvesti `Macu_kronika`, tau kiekvienam mačui reikia turėti jo
pavadinimą, taškus, kaupiamąją sumą, efektyvumą ir įvertinimą. Kaupiamoji suma
atsiranda tada, kai prie iki šiol turėtos sumos pridedi einamojo mačo taškus -
čia tiesiogiai pritaikomas [6 skyrius apie bėgančią sumą](#6-bėganti-suma).
Efektyvumas yra skaičiavimas pagal formulę, o įvertinimas yra `if / elif / else`
pagal ribas, todėl pasižiūrėk į [7 skyrių](#7-skaičiavimas-pagal-formulę-ir-įvertinimas).

Kai užduotis prašo išvesti mačus atvirkštine tvarka, vien spausdinti mačą ciklo
metu nebeužtenka. Vėliau reikės prisiminti visus pavadinimus, todėl ciklo metu
juos reikia dėti į sąrašą. Čia tinka [5 skyrius apie sąrašus ir `append()`](#5-sąrašas-ir-append).
Kai sąrašas jau sukauptas, jį galima pereiti nuo paskutinio elemento iki pirmojo,
kaip parodyta [11 skyriuje](#11-atvirkštinis-iteravimas-per-sąrašą).

Kai užduotis prašo rasti pirmą mačą, po kurio kaupiamoji suma viršijo ribą `s`,
reikia tikrinti kaupiamąją sumą po kiekvieno jos atnaujinimo. Kad atsakymas liktų
pirmas tinkamas mačas, reikia vėliavėlės: kai dar nerasta - leidžiame įrašyti
atsakymą, kai jau rasta - daugiau jo nebekeičiame. Pritaikyk
[8 skyrių apie vėliavėlę](#8-vėliavėlė-kaip-rasti-pirmą-tinkamą-elementą).

Kai užduotis prašo ilgiausios pergalių serijos, tau reikia žiūrėti į kiekvieno
mačo `laimejo` reikšmę. Jeigu reikšmė reiškia pergalę, dabartinė serija didėja.
Jeigu ne, dabartinė serija nutrūksta ir grįžta į nulį. Atskirai reikia saugoti
didžiausią iki šiol rastą seriją. Tai tas pats principas kaip
[9 skyriuje apie ilgiausią seriją](#9-ilgiausia-iš-eilės-einanti-serija).

Kai užduotis prašo suskaičiuoti, kiek treniruočių reikia iki tikslo `t`, šis
veiksmas daromas po pagrindinio ciklo, nes tik tada jau žinai bendrą taškų sumą.
Jeigu tikslas dar nepasiektas, reikia vis pridėti `p`, kol suma pasiekia arba
viršija tikslą. Tam naudok [12 skyrių apie `while`](#12-while-ciklas).

Kai užduotis prašo rasti geriausią ir blogiausią mačą pagal taškus, tai galima
daryti tame pačiame pagrindiniame cikle, kuriame skaitai mačus. Kadangi reikšmės
ateina po vieną iš `input()`, pradinei didžiausiai ir mažiausiai reikšmei naudok
pirmą nuskaitytą mačą, o kitus lygink su juo. Čia labiausiai tinka
[10.2 skyrius apie min/max skaitant duomenis](#102-kai-reikšmes-skaitome-su-input).

Kai užduotis prašo lyderių lentelės, tau reikia turėti mačų pavadinimus ir jų
taškus sąrašuose. Šie du sąrašai yra susiję: jei sukeiti taškus, turi sukeisti ir
atitinkamą pavadinimą. Tam pirma prireikia [5 skyriaus apie sąrašus](#5-sąrašas-ir-append),
o pačiam rikiavimui - [13 skyriaus apie parinkimo rikiavimą](#13-parinkimo-rikiavimas).

Geriausia sprendimą auginti dalimis. Pirma padaryk įvesties skaitymą ir
`Macu_kronika` dalį. Tada paleisk checkerį. Kai veikia, pridėk atvirkštinę tvarką,
tada sezono analizės eilutes, tada rikiavimą. Taip aiškiau matysi, kuri vieta
neveikia. Pabaigoje svarbiausia išvesti tekstą tiksliai tokiu formatu, kaip
parašyta užduotyje.

---

## 2. `stdin` ir `stdout`

`stdin` reiškia, kad programa duomenis gauna per `input()`.

`stdout` reiškia, kad programa atsakymus pateikia per `print()`.

Jeigu užduotyje parašyta, kad reikia naudoti tik `stdin` / `stdout`, programa neturi
prašyti papildomų paaiškinimų, pvz.:

```python
skaicius = int(input())
print(skaicius * 2)
```

Nerašome taip:

```python
skaicius = int(input("Ivesk skaiciu: "))
```

Checkeris tikisi tik tikslaus įvesties ir išvesties formato.

---

## 3. Kaip nuskaityti kelis skaičius vienoje eilutėje

Tarkime, pirmoje eilutėje pateikti trys skaičiai:

```text
5 100 12
```

Juos galima nuskaityti taip:

```python
eilute = input().split()

kiekis = int(eilute[0])
riba = int(eilute[1])
priedas = int(eilute[2])
```

Kas čia vyksta:

- `input()` nuskaito visą eilutę kaip tekstą;
- `.split()` padalija tekstą pagal tarpus;
- gauname atskiras teksto dalis;
- `int(...)` paverčia tekstą į skaičių.

Trumpesnis variantas:

```python
kiekis, riba, priedas = map(int, input().split())
```

---

## 4. Kaip nuskaityti mišrius duomenis

Kartais vienoje eilutėje būna ir tekstas, ir skaičiai. Pavyzdžiui, bibliotekoje
viena eilutė aprašo knygą:

```text
Haris 320 5 1
```

Čia:

- `Haris` yra pavadinimas;
- `320` yra puslapių skaičius;
- `5` yra įvertinimas;
- `1` reiškia, kad knyga perskaityta.

Python kodas:

```python
eilute = input().split()

pavadinimas = eilute[0]
puslapiai = int(eilute[1])
ivertinimas = int(eilute[2])
perskaityta = int(eilute[3])
```

Svarbu: po `split()` viskas yra tekstas, todėl skaičius reikia paversti su `int()`.

---

## 5. Sąrašas ir `append()`

Sąrašas leidžia laikyti kelias reikšmes vienoje vietoje.

```python
miestai = []
miestai.append("Vilnius")
miestai.append("Kaunas")
miestai.append("Klaipeda")
```

Dabar:

```python
miestai == ["Vilnius", "Kaunas", "Klaipeda"]
```

Jei skaitome kelias eilutes, ciklo metu galime kaupti duomenis:

```python
pavadinimai = []
kainos = []

for i in range(kiekis):
    eilute = input().split()
    preke = eilute[0]
    kaina = int(eilute[1])

    pavadinimai.append(preke)
    kainos.append(kaina)
```

Taip po ciklo turime visus pavadinimus ir visas kainas ta pačia tvarka.

---

## 6. Bėganti suma

Bėganti suma yra suma, kuri didėja po kiekvienos naujos reikšmės.

Pavyzdžiui, kelionėje kiekvieną dieną nueiname tiek kilometrų:

```text
4 7 3
```

Tada:

- po 1 dienos iš viso nueita 4;
- po 2 dienų iš viso nueita 11;
- po 3 dienų iš viso nueita 14.

Kodas:

```python
is_viso = 0

for i in range(dienu_kiekis):
    km = int(input())
    is_viso += km
    print(is_viso)
```

Principas paprastas: prieš ciklą suma lygi 0, o cikle prie jos pridedame naują
reikšmę.

---

## 7. Skaičiavimas pagal formulę ir įvertinimas

Dažnai iš kelių duomenų reikia apskaičiuoti vieną rezultatą. Pavyzdžiui, produkto
balas skaičiuojamas taip:

```python
balas = kokybe - defektai + premija
```

Tada pagal balą galima priskirti tekstinį įvertinimą:

```python
if balas >= 90:
    lygis = "Aukstas"
elif balas >= 60:
    lygis = "Vidutinis"
elif balas >= 30:
    lygis = "Zemas"
else:
    lygis = "Labai_zemas"
```

Svarbu tikrinti nuo didžiausios ribos žemyn. Jeigu pradėtume nuo mažos ribos,
didesni rezultatai per anksti patektų į netinkamą grupę.

Jei reikia spausdinti du skaitmenis po kablelio:

```python
print(f"{balas:.2f}")
```

Pavyzdžiui, `75` bus išspausdinta kaip `75.00`.

---

## 8. Vėliavėlė: kaip rasti pirmą tinkamą elementą

Vėliavėlė yra `True` arba `False` reikšmė, kuri padeda prisiminti, ar jau radome
tai, ko ieškojome.

Pavyzdys: turime dienų temperatūras ir norime rasti pirmą dieną, kai temperatūra
pakilo virš 25 laipsnių.

```python
rasta = False
pirma_karsta_diena = "NERA"
suma = 0

for i in range(dienu_kiekis):
    temperatura = int(input())
    suma += temperatura

    if not rasta and temperatura > 25:
        pirma_karsta_diena = i + 1
        rasta = True
```

Kodėl reikia `not rasta`? Kad išsaugotume būtent pirmą tinkamą atvejį. Vėlesni
tinkami atvejai jo nebepakeičia.

---

## 9. Ilgiausia iš eilės einanti serija

Serijai skaičiuoti dažniausiai reikia dviejų kintamųjų:

- `dabartine` - kiek tinkamų reikšmių eina iš eilės dabar;
- `ilgiausia` - kokia didžiausia serija buvo iki šiol.

Pavyzdys: norime rasti ilgiausią dienų seriją, kai mokinys padarė namų darbus.
`1` reiškia padarė, `0` reiškia nepadarė.

```python
dabartine = 0
ilgiausia = 0

for i in range(dienu_kiekis):
    padare = int(input())

    if padare == 1:
        dabartine += 1
        if dabartine > ilgiausia:
            ilgiausia = dabartine
    else:
        dabartine = 0
```

Pavyzdys su reikšmėmis `1 0 1 1 1 0 1`:

| Reikšmė | dabartine | ilgiausia |
|---|---:|---:|
| 1 | 1 | 1 |
| 0 | 0 | 1 |
| 1 | 1 | 1 |
| 1 | 2 | 2 |
| 1 | 3 | 3 |
| 0 | 0 | 3 |
| 1 | 1 | 3 |

Ilgiausia serija yra `3`.

---

## 10. Didžiausios ir mažiausios reikšmės radimas

Jei reikia rasti didžiausią ir mažiausią reikšmę be `max()` ir `min()`, patikimas
būdas yra pirmą tikrą reikšmę paimti kaip pradinę. Tada visas kitas reikšmes
lyginame su ja.

### 10.1. Kai reikšmės jau yra sąraše

Tarkime, turime sąrašą su savaitės išlaidomis. Reikia rasti didžiausią ir
mažiausią išlaidų sumą.

```python
islaidos = [8, 3, 10, 4]

didziausia = islaidos[0]
maziausia = islaidos[0]

for i in range(1, len(islaidos)):
    if islaidos[i] > didziausia:
        didziausia = islaidos[i]

    if islaidos[i] < maziausia:
        maziausia = islaidos[i]
```

Kodėl ciklas prasideda nuo `1`? Nes elementą su indeksu `0` jau panaudojome kaip
pradinę reikšmę.

Jei kartu reikia išsaugoti ir pavadinimą, naudojame du lygiagrečius sąrašus:

```python
prekes = ["Obuoliai", "Sultys", "Duona", "Suris"]
kainos = [2, 4, 1, 6]

brangiausia_kaina = kainos[0]
pigiausia_kaina = kainos[0]
brangiausia_preke = prekes[0]
pigiausia_preke = prekes[0]

for i in range(1, len(kainos)):
    if kainos[i] > brangiausia_kaina:
        brangiausia_kaina = kainos[i]
        brangiausia_preke = prekes[i]

    if kainos[i] < pigiausia_kaina:
        pigiausia_kaina = kainos[i]
        pigiausia_preke = prekes[i]
```

### 10.2. Kai reikšmes skaitome su `input()`

Kartais reikšmių dar neturime sąraše - jos ateina po vieną. Tada pirmą nuskaitytą
eilutę naudojame kaip pradžią, o kitas jau lyginame.

Pavyzdys: skaitome prekes ir jų kainas. Reikia rasti brangiausią ir pigiausią prekę.

```python
for i in range(prekiu_kiekis):
    eilute = input().split()
    preke = eilute[0]
    kaina = int(eilute[1])

    if i == 0:
        brangiausia_kaina = kaina
        pigiausia_kaina = kaina
        brangiausia_preke = preke
        pigiausia_preke = preke

    else:
        if kaina > brangiausia_kaina:
            brangiausia_kaina = kaina
            brangiausia_preke = preke

        if kaina < pigiausia_kaina:
            pigiausia_kaina = kaina
            pigiausia_preke = preke
```

Čia `i == 0` reiškia: skaitome pirmą prekę, todėl dar neturime su kuo lyginti.
Pirmą prekę laikinai laikome ir brangiausia, ir pigiausia. Kai skaitome antrą,
trečią ir kitas prekes, jau galime normaliai lyginti.

Jei dvi prekės turi tą pačią kainą, toks kodas paliks pirmą rastą, nes naudojame
`>` ir `<`, o ne `>=` ir `<=`.

---

## 11. Atvirkštinis iteravimas per sąrašą

Jei norime pereiti per sąrašą nuo paskutinio elemento iki pirmojo:

```python
skaiciai = [10, 20, 30, 40]

for i in range(len(skaiciai) - 1, -1, -1):
    print(skaiciai[i], end=" ")

print()
```

Rezultatas:

```text
40 30 20 10
```

Kas reiškia `range(len(skaiciai) - 1, -1, -1)`:

- pirmas argumentas - pradedame nuo paskutinio indekso;
- antras argumentas - sustojame prieš `-1`, todėl pasiekiame indeksą `0`;
- trečias argumentas - einame atgal po vieną.

Jeigu nori viską išvesti vienoje eilutėje be papildomo tarpo gale, gali susikurti
naują sąrašą ir naudoti `" ".join(...)`:

```python
atvirksciai = []

for i in range(len(skaiciai) - 1, -1, -1):
    atvirksciai.append(str(skaiciai[i]))

print(" ".join(atvirksciai))
```

---

## 12. `while` ciklas

`while` kartoja veiksmus tol, kol sąlyga yra teisinga.

Pavyzdys: žmogus taupo pinigus. Jis jau turi `turima`, nori pasiekti `tikslas`, o
kas savaitę sutaupo `per_savaite`.

```python
savaiciu = 0
truksta = tikslas - turima

while truksta > 0:
    truksta -= per_savaite
    savaiciu += 1
```

Jei `turima` jau yra daugiau arba lygu `tikslas`, tada `truksta <= 0`, todėl ciklas
nei karto neprasidės ir `savaiciu` liks `0`.

---

## 13. Parinkimo rikiavimas

Jeigu tiesiog reikėtų surikiuoti paprastą sąrašą Python programoje, dažnai galėtume
naudoti `sort()` arba `sorted()`:

```python
skaiciai = [8, 3, 10, 4]
skaiciai.sort()
print(skaiciai)  # [3, 4, 8, 10]
```

Bet mokantis algoritmų dažnai duodama užduotis rikiavimą padaryti pačiai arba
atpažinti kodą, kuris rikiuoja sąrašą. Tada reikia suprasti ne tik rezultatą, bet
ir veiksmų eigą.

Vienas iš paprastų rikiavimo algoritmų vadinamas **parinkimo rikiavimu**
(`selection sort`). Jo idėja: kiekvienoje pozicijoje surandame didžiausią reikšmę
likusioje sąrašo dalyje ir sukečiame ją su dabartine pozicija.

Pavyzdys: norime surikiuoti prekes pagal kainą nuo brangiausios iki pigiausios.
Turime du lygiagrečius sąrašus:

```python
prekes = ["Obuoliai", "Sultys", "Duona", "Suris"]
kainos = [2, 4, 1, 6]
```

Svarbu: prekės pavadinimas ir jos kaina turi judėti kartu.

Algoritmas veikia taip:

1. Atsistojame į pirmą poziciją `i = 0`.
2. Nuo tos pozicijos iki sąrašo galo ieškome didžiausios kainos.
3. Radę didžiausią kainą, sukeičiam ją su kaina pozicijoje `i`.
4. Kartu sukeičiam ir prekių pavadinimus.
5. Pereiname į kitą poziciją `i = 1` ir kartojame tą patį.

Su mūsų pavyzdžiu eiga būtų tokia:

| Žingsnis | Ką tikriname | Didžiausia rasta reikšmė | Sąrašai po sukeitimo |
|---|---|---:|---|
| Pradžia | - | - | `Obuoliai 2`, `Sultys 4`, `Duona 1`, `Suris 6` |
| `i = 0` | pozicijos `0..3` | `6` | `Suris 6`, `Sultys 4`, `Duona 1`, `Obuoliai 2` |
| `i = 1` | pozicijos `1..3` | `4` | `Suris 6`, `Sultys 4`, `Duona 1`, `Obuoliai 2` |
| `i = 2` | pozicijos `2..3` | `2` | `Suris 6`, `Sultys 4`, `Obuoliai 2`, `Duona 1` |
| `i = 3` | pozicija `3` | `1` | `Suris 6`, `Sultys 4`, `Obuoliai 2`, `Duona 1` |

Po kiekvieno išorinio ciklo praėjimo viena reikšmė atsistoja į galutinę vietą:
pirmiausia didžiausia, tada antra didžiausia, tada trečia ir taip toliau.

```python
for i in range(len(kainos)):
    maks_i = i

    for j in range(i + 1, len(kainos)):
        if kainos[j] > kainos[maks_i]:
            maks_i = j

    kainos[i], kainos[maks_i] = kainos[maks_i], kainos[i]
    prekes[i], prekes[maks_i] = prekes[maks_i], prekes[i]
```

Po rikiavimo:

```python
prekes == ["Suris", "Sultys", "Obuoliai", "Duona"]
kainos == [6, 4, 2, 1]
```

Jei originalių sąrašų dar reikės vėliau, prieš rikiavimą galima pasidaryti kopijas:

```python
rikiuojamos_prekes = prekes[:]
rikiuojamos_kainos = kainos[:]
```

Šis algoritmas yra aiškus, bet tikrai lėtas, palyginus su geresniais rikiavimo
algoritmais. Viename žingsnyje didžiausios reikšmės paieška likusioje sąrašo dalyje
yra panaši į `O(n)` darbą, bet tokią paiešką kartojame daug kartų. Todėl visas
parinkimo rikiavimas yra `O(n^2)`. Tai reiškia: jei duomenų kiekis padidėja,
veiksmų skaičius auga labai greitai.

---

## 14. Dažnos klaidos

### Pamirštama paversti tekstą į skaičių

```python
kaina = eilute[1]      # čia tekstas
kaina = int(eilute[1]) # čia skaičius
```

### Naudojamas `=` vietoj `==`

Sąlygoje reikia lyginti su `==`:

```python
if padare == 1:
    dabartine += 1
```

### Prarandamas pirmas rastas atsakymas

Jei reikia pirmo tinkamo atvejo, naudok vėliavėlę:

```python
if not rasta and reiksme > riba:
    atsakymas = pavadinimas
    rasta = True
```

### Rikiuojant sukeičiamas tik vienas sąrašas

Jei turi du lygiagrečius sąrašus, sukeisti reikia abu:

```python
kainos[i], kainos[maks_i] = kainos[maks_i], kainos[i]
prekes[i], prekes[maks_i] = prekes[maks_i], prekes[i]
```

### Išvedamas papildomas tekstas

Jeigu užduotyje prašoma:

```text
Atsakymas: 15
```

reikia spausdinti būtent tai, o ne:

```text
Mano atsakymas yra 15
```
