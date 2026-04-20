# Teorija: kaip spręsti `nd1.py`

Pirmiausia rekomenduoju perskaityti visą užduoties aprašymą `ND_UZDUOTIS.md`, kad susidarytum bendrą vaizdą, kas yra prašoma.

Šis dokumentas skirtas ne tam, kad duotų pilną sprendimą, o tam, kad parodytų, iš kokių mažų dalių toks sprendimas susideda.

Svarbiausia mintis:

> Net jei dar nesimokėm kaip naudoti `list` ir `dictionary`, tokią užduotį vis tiek galima išspręsti.

Užtenka:

- nuskaityti duomenis;
- suskaičiuoti reikšmes;
- turėti keletą kintamųjų bendriems rezultatams;
- su `for` ciklu perskaityti visas komandas;
- su `while` ciklu išspręsti paskutinę dalį.

---

## 1. `stdin` ir `stdout`

`stdin` reiškia, kad programa duomenis gauna per `input()`.

`stdout` reiškia, kad programa atsakymus pateikia per `print()`.

Paprastas pavyzdys:

```python
x = int(input())
print(x * 2)
```

Jei įvestis yra:

```text
7
```

tuomet išvestis bus:

```text
14
```

---

## 2. Kaip nuskaityti kelis skaičius vienoje eilutėje

Jei pirmoje eilutėje yra trys skaičiai,galime rašyti taip:

```python
pirma_eilute = input().split()

n = int(pirma_eilute[0])
r = int(pirma_eilute[1])
p = int(pirma_eilute[2])
```

Kas čia vyksta:

- `input()` nuskaito visą eilutę;
- `.split()` padalija tekstą pagal tarpus;
- gauname 3 atskiras teksto dalis;
- kiekvieną reikalingą dalį paverčiame į `int`.

Jei įvesta:

```text
3 80 8
```

gaunama:

- `n = 3`
- `r = 80`
- `p = 8`

Trumpesnis variantas irgi egzistuoja:

```python
n, r, p = map(int, input().split())
```

Čia jau svarbu suprasti ne tik `int`, bet ir patį `map`.

## Kaip veikia `map`

`map` yra Python funkcija.

Ji dažniausiai priima bent 2 dalykus:

- **pirmą argumentą**: funkciją, kurią reikia pritaikyti;
- **antrą argumentą**: reikšmių seką, per kurią reikia eiti.

Paprasčiausia forma atrodo taip:

```python
map(funkcija, reiksmes)
```

Tai reiškia:

> paimk kiekvieną `reiksmes` elementą ir pritaikyk jam `funkcija`

Pavyzdžiui:

```python
skaiciai_tekstu = ["3", "80", "8"]
rezultatas = map(int, skaiciai_tekstu)
```

Čia:

- `int` yra funkcija;
- `skaiciai_tekstu` yra reikšmės, per kurias einama;
- `map` daro maždaug tokį darbą:
    - `int("3")`
    - `int("80")`
    - `int("8")`

Taigi labai grubiai galima įsivaizduoti, kad:

```python
map(int, ["3", "80", "8"])
```

reiškia beveik tą patį kaip:

```python
int("3"), int("80"), int("8")
```

Tik `map` tą daro automatiškai visiems elementams iš eilės.

## Ką reiškia `int` šitoje vietoje

Labai svarbi mintis:

- `int` čia nėra tekstas;
- `int` čia nėra jau paleistas veiksmas;
- `int` čia yra **funkcija**, kuri paverčia tekstą į sveikąjį skaičių.

Pavyzdžiui:

```python
print(int("25"))
```

Išveda:

```text
25
```

Vadinasi, kai rašome:

```python
map(int, kazkas)
```

mes sakome:

> `map`, naudok funkciją `int` kiekvienai reikšmei

## Kaip tai susiję su `input().split()`

Pažiūrėkime visą eilutę:

```python
n, r, p = map(int, input().split())
```

Ji vyksta tokiais žingsniais:

1. `input()` nuskaito visą eilutę, pavyzdžiui:

```text
3 80 8
```

2. `.split()` padalija ją į tekstines dalis:

```python
["3", "80", "8"]
```

3. `map(int, ...)` paima kiekvieną dalį ir pritaiko `int()`:

```python
int("3")
int("80")
int("8")
```

4. Galiausiai gaunami normalūs skaičiai:

```python
3, 80, 8
```

5. Jie priskiriami kintamiesiems:


```python
n, r, p = 3, 80, 8
```
kas reiškia tiesiog:
```python
n = 3
r = 80
p = 8
```


---

## 3. Kaip nuskaityti mišrius duomenis

Komandos eilutėje yra ir tekstas, ir skaičiai.

Pradžioje gali nuskaityti viską kaip tekstą:

```python
vardas, taskai, pergales, bonusai, baudos, rungtys, disk = input().split()
```

Bet tada skaitinius kintamuosius reikia paversti į `int`:

```python
taskai = int(taskai)
pergales = int(pergales)
bonusai = int(bonusai)
baudos = int(baudos)
rungtys = int(rungtys)
disk = int(disk)
```

---

## 4. Skaičiavimai su operatoriais

Pamokose jau buvo:

- `+` sudėtis
- `-` atimtis
- `*` daugyba
- `/` dalyba
- `//` sveikoji dalis
- `%` liekana
- `**` kėlimas laipsniu

Pavyzdžiai:

```python
a = 17
b = 5

print(a + b)   # 22
print(a - b)   # 12
print(a * b)   # 85
print(a / b)   # 3.4
print(a // b)  # 3
print(a % b)   # 2
print(b ** 2)  # 25
```

---

## 5. Formatavimas su `f` string ir `:.2f`

Jei nori įdėti kintamąjį į tekstą:

```python
vardas = "Aidas"
taskai = 88
print(f"{vardas} {taskai}")
```

Jei turi dešimtainį skaičių ir nori visada rodyti 2 skaitmenis po kablelio:

```python
vidurkis = 17
print(f"{vidurkis:.2f}")
```

Išves:

```text
17.00
```

Dar pavyzdys:

```python
vidurkis = 29.333333
print(f"{vidurkis:.2f}")
```

Išves:

```text
29.33
```

---

## 6. Sąlygos: `if`, `elif`, `else`

Kai reikia priimti sprendimą, naudojame šakas.

Paprastas nesusijęs pavyzdys:

```python
x = 25
if x > 30:
    print("Daugiau nei 30")
elif x > 20:
    print("Daugiau nei 20, bet ne daugiau nei 30")
else:
    print("20 arba mažiau")
```
Išves:

```text
Daugiau nei 20, bet ne daugiau nei 30
```


Svarbu:

- tikrinama iš viršaus į apačią;
- kai viena sąlyga tinka, žemiau esančios nebetikrinamos;
- todėl tvarka labai svarbi.

Mūsų užduotyje svarbu tikrinti aukščiausias ribas pirmiausia, nes jos duoda geriausią medalį:

```
jeigu taskai daugiau arba lygūs 100
    tuomet medalis yra Auksas
jeigu taskai daugiau arba lygūs 80
    tuomet medalis yra Sidabras
jeigu taskai daugiau arba lygūs 60
    tuomet medalis yra Bronza
kitu atveju
    medalis yra Be_medalio
```


---

## 7. Loginiai operatoriai

### `and`

Abi sąlygos turi būti teisingos.

```python
if taskai >= r and disk == 0:
    print("Finale")
```

### `or`

Užtenka, kad teisinga būtų bent viena sąlyga.

```python
if taskai < 50 or baudos > 20:
    print("Rizika")
```

### `not`

Apverčia loginę reikšmę.

```python
diskvalifikuota = False

if not diskvalifikuota:
    print("Aktyvi komanda")
```

---

## 8. `for` ciklas, kai komandų skaičius žinomas

Pakartokime `for` ciklo sintaksę:


kai `range()` vienas argumentas, jis reiškia, kiek kartų kartoti:

```python
for i in range(3):
    print(i)
```
Išves:

```text
0
1
2
```

kai `range()` du argumentai, pirmas reiškia, nuo kur pradėti, antras – iki kur kartoti:

```python
for i in range(1, 4):
    print(i)
```
Išves:  

```text
1
2
3
``` 

kai `range()` trys argumentai, pirmas reiškia, nuo kur pradėti, antras – iki kur kartoti, trečias – kokio dydžio žingsnį daryti:

```python
for i in range(0, 10, 2):
    print(i)
```
Išves:  

```text
0
2
4
6
8
```        
Išves:

Taip pat jei vietoje i rašome `_`, tai reiškia, kad mums nereikia ciklo numerio:

```python
for _ in range(3):
    print("Labas")
```
Išves:
```text
Labas
Labas
Labas
```


Jei žinai, kad komandų bus `n`, gali skaityti taip:

```python
for _ in range(n):
    vardas, taskai, pergales, bonusai, baudos, rungtys, disk = input().split()
```

Čia `_` reiškia, kad ciklo iteracijos numerio pačio savaime mums nereikia.

---

## 9. Kaip spręsti be `list` ir be `dictionary`

Čia svarbiausia vieta.

Nebūtina sukaupti visų komandų į sąrašą. Galima dirbti taip:

1. Perskaitai vieną komandą.
2. Iš karto apskaičiuoji jos reikšmes.
3. Iš karto atspausdini jos eilutę į `Bronzos_lyga` dalį.
4. Tuo pačiu atnaujini bendrus kintamuosius.

Tų bendrų kintamųjų pavyzdžiai:

- kiek yra finalistų;
- finalistų vardų eilutė;
- kiek komandų tiksliai ant ribos;
- kiek komandų tvarkingos;
- pirma komanda virš 90;
- kiek rizikos komandų;
- kiek komandų su bonusais;
- silpniausios aktyvios komandos vardas;
- silpniausios aktyvios komandos taškai.

Pseudokodo šablonas:

```text
nuskaityk pirma eilute

sukurk bendrus kintamuosius

isvesk "Bronzos_lyga:"

kartok n kartu:
    nuskaityk viena komanda
    paversk skaicius i int
    apskaiciuok reiksmes
    nustatyk medali
    isvesk viena eilute
    atnaujink bendrus rezultatus

po ciklo isvesk likusias dalis
```

---

## 10. Skaitikliai

Kai kažką skaičiuoji, pradedi nuo 0 ir didini.

```text
pradine_reiksme = 0

jei salyga teisinga:
    padidink skaitikli vienetu
```

Tas pats tinka:

- rizikos komandų skaičiui;
- bonusų komandų skaičiui;
- tvarkingų komandų skaičiui;
- treniruočių skaičiui.

Kitaip tariant, skaitiklis atsako į klausimą: kiek kartų įvyko tam tikra sąlyga?

---

## 11. Kaip kaupti vardus viename tekste

Jei dar nenaudoji sąrašų, finalistų vardus galima kaupti paprastame `string`.

Pseudokodo idėja:

```text
jei reikia prideti pirma varda:
    rezultato_tekstas = vardas
kitu atveju:
    rezultato_tekstas = senas_tekstas + tarpas + vardas
```

Kodėl taip:

- pirmas vardas įrašomas be tarpo priekyje;
- visi kiti pridedami su tarpu.

Jei gale `finalistai == ""`, reiškia finalistų nebuvo.

---

## 12. Kaip rasti pirmą atitinkantį elementą

Jei reikia rasti pirmą komandą, kuri surinko daugiau nei 90, labai patogu naudoti papildomą loginį kintamąjį.

```text
jei dar nieko neradai ir dabartine komanda tinka:
    issaugok jos varda
    pazymek kad jau radai
```

Radus pirmą tinkamą komandą, jos nebereikia perrašinėti kitomis vėliau rastomis.

---

## 13. Kaip rasti mažiausią reikšmę

Silpniausiai aktyviai komandai rasti reikia saugoti:

- ar jau radai bent vieną aktyvią komandą;
- mažiausius taškus;
- tos komandos vardą.

Pseudokodo šablonas:

```text
jei komanda aktyvi:
    jei tai pirma aktyvi komanda:
        issaugok jos varda ir taskus kaip geriausiai zinoma pradine reiksme
    kitu atveju jei jos taskai mazesni uz siuo metu issaugotus:
        atnaujink issaugota varda ir taskus
```

Čia svarbiausia idėja:

- pirmą tinkamą reikšmę pasiimi kaip pradinę;
- po to lygini visas kitas su ja.


---


## 14. `while` ciklas Boss level daliai


Verta pakartoti `while` ciklo sintaksę:

```python
while salyga:
    # veiksmai, kurie kartojasi, kol salyga teisinga
```
`while` ciklas kartojasi tol, kol sąlyga yra teisinga.  
Pavyzdys:

```python
x = 5
while x > 0:
    print(x)
    x = x - 1
```
Išves:
```text
5
4
3
2
1
```

Taip pat verta išmokti `break` ir `continue`:
- `break` nutraukia visą ciklą;
- `continue` nutraukia tik einamą iteraciją ir pereina prie kitos.
- Pavyzdys su `break`:

```python
x = 5
while x > 0:
    print(x)
    if x == 3:
        break
    x = x - 1
```
Išves:
```text
5
4
3
```

Kas čia vyksta:
- kai `x` tampa 3, `break` nutraukia ciklą;
- todėl 2 ir 1 nebeišvedami.

- Pavyzdys su `continue`:

```python
x = 5
while x > 0:
    x = x - 1
    if x == 3:
        continue
    print(x)
```
Išves:
```text
4
2
1
0
```

Kas čia vyksta:
- kai `x` tampa 3, `continue` nutraukia tą iteraciją;
- todėl 3 nebeišvedamas, bet ciklas tęsiasi toliau.
- Taip pat svarbu, kad `x = x - 1` yra prieš `continue`, todėl `x` vis tiek mažėja, net jei `continue` įvyksta.
- Jei `x = x - 1` būtų po `continue`, tuomet `x` niekada nesumažėtų, ir ciklas taptų begalinis.
- Pavyzdys su `continue` prieš `x = x - 1`:

```python
x = 5
while x > 0:
    if x == 3:
        continue
    x = x - 1
    print(x)
```

Šis kodas sukeltų begalinį ciklą, nes kai `x` tampa 3, `continue` nutraukia iteraciją prieš `x = x - 1`, todėl `x` niekada nesumažėja žemiau 3.


Taigi kai reikia kartoti veiksmą, kol kažko trūksta, tinka `while`.

Pseudokodo šablonas:

```text
apskaiciuok kiek tasku truksta
treniruociu skaicius pradžioje yra 0

kol vis dar truksta tasku:
    sumazink trukstamu tasku kieki
    padidink treniruociu skaiciu
```

Kas čia vyksta:

- kol trūksta taškų, ciklas sukasi;
- kiekvieną kartą sumažiname trūkstamų taškų kiekį;
- tuo pačiu suskaičiuojame, kiek kartų ciklas įvyko.

Jei komandai jau netrūksta taškų, `while` net neprasidės ir treniruočių bus 0.


Taip pat apskritai `while` galima naudoti su `True` ir `break`:

```python
while True:
    # veiksmai, kurie kartojasi be galo, kol nepasiekiame break
    if salyga:
        break

``` 
Čia `while True` reiškia, kad ciklas kartosis be galo, kol nebus pasiektas `break`.


---

## 15. Naudingi tarpiniai kintamieji

Tokiose užduotyse verta kurti trumpus, aiškius tarpinius kintamuosius:

```text
diskvalifikuota = ar komanda diskvalifikuota?
finale = ar komanda patenka i finala?
tvarkinga = ar komanda tvarkinga?
rizika = ar komanda rizikos grupeje?
su_bonusais = ar turi bent viena bonusa?
```

Tai padeda:

- lengviau skaityti kodą;
- mažiau kartoti tą pačią sąlygą;
- lengviau susigaudyti, ką tikrini.

Mintis tokia: vietoj ilgos sąlygos keliuose skirtinguose sakiniuose, vieną kartą pasidarai aiškų tarpinį atsakymą.

---

## 16. Galima darbo eiga

Vienas normalus planas būtų toks:

1. Nuskaityti `n`, `r`, `p`.
2. Iš karto atspausdinti `Bronzos_lyga:`.
3. Prieš ciklą susikurti visus bendrus kintamuosius su pradine reikšme.
4. Su `for` ciklu perskaityti kiekvieną komandą.
5. Ciklo viduje:
    - paversti reikšmes į skaičius;
    - apskaičiuoti vienos komandos rezultatus;
    - išspausdinti tai, kas priklauso pirmai daliai;
    - atnaujinti bendrus atsakymus vėlesnėms dalims.
6. Po `for` ciklo atspausdinti `Finalo_komisija` dalį.
7. Tada atspausdinti `Komandu_radaras` dalį.
8. Tada su `while` logika užbaigti `Boss_level` dalį.

Trumpas pseudokodo planas:

```text
1. nuskaityk bendra informacija
2. paruosk bendrus kintamuosius
3. apdorok komandas viena po kitos
4. po ciklo isvesk suvestines dalis
5. gale uzbaik boss level skaiciavima
```

---

## 17. Dažniausios klaidos

### 1. Nepaversti skaičių į `int`

Jei nepaversi, Python juos laikys tekstu.

### 2. Blogas formatas

Automatinis tikrintuvas labai jautrus:

- papildomiems tarpams;
- neteisingoms didžiosioms raidėms;
- papildomam tekstui;
- tuščioms eilutėms ne vietoje.

### 3. Netvarkinga `if / elif / else` tvarka

Jei aukščiausias ribas tikrinsi per vėlai, medalis bus blogas.

### 4. Pamirštas `:.2f`

Jei vietoj `17.00` išvesi `17.0` arba `17`, testas gali nepraeiti.

### 5. Pamiršti pradines reikšmes

Pvz., jeigu prieš ciklą nesukursi `finalistai = ""`, neturėsi kur kaupti vardų.

---

## 18. Pastaba

Šita užduotis atrodo didelė, bet ji sudėta iš mažų gabalų, kuriuos jau esame lietę:

- `input()`
- `int()`
- aritmetika
- `if / elif / else`
- `for`
- `while`
- `print(f"...")`

Gali atrodyt kad kažko nesame ėje ir trūksta žinių. Tačiau, čia ne nauja tema, o mokėjimas susidėti mažus gabalus į vieną ilgesnę programą. 



