"""
# Krepšinio Sezono Kronika

## Situacija

Tavo draugė Eglė veda savo krepšinio komandos statistiką. Ji užsirašo kiekvieno
mačo rezultatą: kiek taškų tame mače buvo pelnyta, kiek klaidų padaryta, kiek
baudų metimų pataikyta. Sezono pabaigoje ji nori gauti visą analizę.

Tavo programa turi:

1. apskaičiuoti kaupiamąją sumą — kiek taškų iš viso užpelnyta po kiekvieno mačo;
2. išvesti mačus atvirkštine tvarka (nuo paskutinio iki pirmojo);
3. rasti pirmą mačą, po kurio kaupiamoji suma viršijo s taškų;
4. rasti ilgiausią pergalių seriją iš eilės;
5. su while ciklu suskaičiuoti, kiek treniruočių reikia, kad komanda pasiektų
   sezono tikslą t (per treniruotę pelno p taškų);
6. rasti geriausią mačą (daugiausiai taškų) ir blogiausią (mažiausiai taškų);
7. surikiuoti mačus pagal taškus nuo didžiausio iki mažiausio — lyderių lentelė
   (naudojant rikiavimo algoritmą, be Python sort).

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

- n — mačų skaičius per sezoną;
- s — taškų riba, kurią peržengus komanda oficialiai dominuoja lygoje;
- t — sezono tikslas (bendras taškų skaičius, kurį norima pasiekti);
- p — kiek taškų komanda pelno per vieną papildomą treniruotę.

Toliau pateikiamos n eilučių. Kiekvienoje eilutėje yra:

- priešininko pavadinimas varzybos — vienas žodis;
- tame mače pelnytų taškų skaičius taskai;
- padarytų klaidų skaičius klaidos;
- pataikytų baudų metimų skaičius baudos;
- ar laimėjo laimejo, kur 1 reiškia pergalę, 0 — pralaimėjimą.

Visi duomenys vienoje eilutėje atskirti tarpais.

---

## Taisyklės

### Kaupiamoji suma

Po kiekvieno mačo suskaičiuok, kiek iš viso taškų užpelnyta nuo sezono pradžios
iki to mačo imtinai.

### Efektyvumas

Kiekvieno mačo efektyvumas = taškai − klaidos + baudos.
Efektyvumą išvesk dviem skaitmenimis po kablelio.

### Mačo įvertinimas

- jei efektyvumas >= 80 → Puikus
- jei efektyvumas >= 50 → Geras
- jei efektyvumas >= 20 → Vidutinis
- kitu atveju → Silpnas

### Lyderystės mačas

Rask pirmą mačą, po kurio kaupiamoji suma tapo griežtai didesnė nei s.
Jei to niekada neįvyko — spausdink NERA.
Naudok vėliavėlę (rasta = False), kaip mokėtės pamokoje.

### Ilgiausia pergalių serija

Pergalių serija — tai eilė iš eilės laimėtų mačų. Rask ilgiausią tokią eilę.

Pavyzdys: laimėjimai 1 0 1 1 1 0 1 1 → ilgiausia serija = 3.

Tau prireiks dviejų kintamųjų:
- dabartine — kiek laimėjimų dabar iš eilės
- ilgiausia — kiek daugiausia buvo iš eilės

### Treniruočių skaičiavimas

Jei bendras taškų skaičius (paskutinė kaupiamoji suma) jau pasiekė ar viršijo
tikslą t — treniruočių reikia 0.

Kitu atveju su while ciklu skaičiuok, kiek kartų reikia pridėti p taškų,
kol kaupiamoji suma pasieks arba viršys t.

### Geriausias ir blogiausias mačas

Rask mačą, kuriame buvo pelnyta daugiausiai taškų (taskai), ir mačą, kuriame
mažiausiai. Jei keli mačai turi vienodai taškų — imk pirmą tokį.

Šiuos gali rasti per pagrindinį for ciklą — lyginant su kintamuoju, kuriame
saugai dabartinį geriausią/blogiausią (kaip u2 uždavinyje).

### Lyderių lentelė (rikiavimas)

Surikiuok mačus pagal pelnytų taškų skaičių (taskai) nuo didžiausio iki
mažiausio. Tada išvesk juos sunumeruotus.

Naudok parinkimo rikiavimą (selection sort). Idėja:

- Eini per sąrašą. Kiekvienoje pozicijoje i randi, kuriame indekse (nuo i iki
  galo) yra DIDŽIAUSIAS taskai.
- Sukeiti tą elementą su elementu pozicijoje i.
- Po pirmo praėjimo — didžiausias taskai yra pozicijoje 0.
- Po antro — antras didžiausias yra pozicijoje 1. Ir t.t.

SVARBU: mačo pavadinimas ir taškų skaičius turi judėti kartu. Todėl turėk du
lygiagredžius sąrašus (macu_vardai ir macu_taskai) ir sukeidamas elementą vienoje
vietoje, sukeisk ir kitame sąraše.

Pavyzdys su taškais [70, 85, 60, 90] ir vardais [A, B, C, D]:

  i=0: maks indeksas nuo 0 iki 3 → indeksas 3 (reikšmė 90).
       Sukeičiam [0]↔[3]: taskai=[90,85,60,70], vardai=[D,B,C,A]
  i=1: maks indeksas nuo 1 iki 3 → indeksas 1 (reikšmė 85). Nieko nesikeičia.
  i=2: maks indeksas nuo 2 iki 3 → indeksas 3 (reikšmė 70).
       Sukeičiam [2]↔[3]: taskai=[90,85,70,60], vardai=[D,B,A,C]
  Rezultatas: D:90, B:85, A:70, C:60 ✓

---

## Išvestis

Pirmiausia:

    Macu_kronika:

Toliau — po vieną eilutę kiekvienam mačui ta pačia tvarka:

    varzybos taskai kaupiamoji efektyvumas ivertinimas

Po to palik vieną tuščią eilutę ir išvesk:

    Atvirkstine_tvarka:
    varzybos1 varzybos2 ...

(visi mačų pavadinimai vienoje eilutėje, nuo paskutinio iki pirmojo)

Po to palik vieną tuščią eilutę ir išvesk:

    Sezono_analize:
    Bendri_taskai: x
    Lyderystes_macas: varzybos
    Ilgiausia_serija: y
    Treniruociu_iki_tikslo: z
    Geriausias_macas: varzybos taskai
    Blogiausias_macas: varzybos taskai

Po to palik vieną tuščią eilutę ir išvesk surikiuotą lyderių lentelę:

    Lyderiu_lentele:
    1. varzybos taskai
    2. varzybos taskai
    ...

---

## Svarbios pastabos

1. Programa turi veikti su bet kokiais teisingais testais.
2. Efektyvumas spausdinamas dviem skaitmenimis po kablelio.
3. Atvirkstine_tvarka eilutėje — visi n mačų pavadinimai vienoje eilutėje,
   atskirti tarpais. Tam reikia sąrašo!
4. Kaupiamoji suma — tai bėganti suma, kuri nuolat auga su kiekvienu maču.
5. Ilgiausią seriją galima suskaičiuoti su dviem kintamaisiais cikle,
   tačiau mačų pavadinimams ir taškams saugoti sąrašai reikalingi.
6. Jei nei vienas mačas nelaimėtas — ilgiausia serija = 0.
7. Rikiavimui naudok du lygiagrečius sąrašus (macu_vardai ir macu_taskai).

---

## Ko čia tikrai prireiks

- append() ir sąrašo iteravimo;
- atvirkštinio iteravimo range(len(...) - 1, -1, -1);
- bėgančios sumos kaupimo kintamuoju;
- vėliavėlės (rasta = False) pirmam radiniui;
- dviejų kintamųjų (dabartine ir ilgiausia) serijai;
- while ciklo;
- min/max radimo lyginimo kintamuoju (kaip u2);
- dviejų lygiagrečių sąrašų rikiavimo su selection sort.

---

## Galima darbo eiga

1. Nuskaityti n, s, t, p.
2. Iš karto atspausdinti Macu_kronika:
3. Prieš ciklą: sukurti tuščius sąrašus macu_vardai ir macu_taskai, paruošti
   visus kintamuosius (kaupiamoji suma, vėliavėlė, serija, geriausias/blogiausias).
4. Su for ciklu perskaityti kiekvieną mačą:
   - apskaičiuoti efektyvumą, kaupiamąją sumą, įvertinimą;
   - pridėti pavadinimą į macu_vardai ir taškus į macu_taskai;
   - atspausdinti eilutę;
   - atnaujinti seriją, vėliavėlę, geriausią/blogiausią.
5. Po ciklo atspausdinti Atvirkstine_tvarka — macu_vardai atvirkščiai.
6. Atspausdinti Sezono_analize (įskaitant geriausią ir blogiausią).
7. Su while ciklu apskaičiuoti treniruočių skaičių.
8. Surikiuoti macu_vardai ir macu_taskai su selection sort, tada išvesti
   Lyderiu_lentele.

---

## Pavyzdžiai

Testas 1:

    Įvestis:
    4 200 400 15
    Zalgiris 85 5 10 1
    Rytas 70 8 5 0
    Wolves 90 3 12 1
    Neptuno 60 10 8 1

    Išvestis:
    Macu_kronika:
    Zalgiris 85 85 90.00 Puikus
    Rytas 70 155 67.00 Geras
    Wolves 90 245 99.00 Puikus
    Neptuno 60 305 58.00 Geras

    Atvirkstine_tvarka:
    Neptuno Wolves Rytas Zalgiris

    Sezono_analize:
    Bendri_taskai: 305
    Lyderystes_macas: Wolves
    Ilgiausia_serija: 2
    Treniruociu_iki_tikslo: 7
    Geriausias_macas: Wolves 90
    Blogiausias_macas: Neptuno 60

    Lyderiu_lentele:
    1. Wolves 90
    2. Zalgiris 85
    3. Rytas 70
    4. Neptuno 60

Testas 2:

    Įvestis:
    3 300 250 20
    Skycop 95 2 15 1
    Legia 80 10 5 1
    Barca 75 6 8 0

    Išvestis:
    Macu_kronika:
    Skycop 95 95 108.00 Puikus
    Legia 80 175 75.00 Geras
    Barca 75 250 77.00 Geras

    Atvirkstine_tvarka:
    Barca Legia Skycop

    Sezono_analize:
    Bendri_taskai: 250
    Lyderystes_macas: NERA
    Ilgiausia_serija: 2
    Treniruociu_iki_tikslo: 0
    Geriausias_macas: Skycop 95
    Blogiausias_macas: Barca 75

    Lyderiu_lentele:
    1. Skycop 95
    2. Legia 80
    3. Barca 75

Testas 3:

    Įvestis:
    5 500 600 10
    Kaunas 50 15 5 0
    Vilnius 60 10 8 0
    Klaipeda 70 5 12 1
    Siauliai 55 20 3 0
    Panevezys 80 8 10 1

    Išvestis:
    Macu_kronika:
    Kaunas 50 50 40.00 Geras
    Vilnius 60 110 58.00 Geras
    Klaipeda 70 180 77.00 Geras
    Siauliai 55 235 38.00 Geras
    Panevezys 80 315 82.00 Puikus

    Atvirkstine_tvarka:
    Panevezys Siauliai Klaipeda Vilnius Kaunas

    Sezono_analize:
    Bendri_taskai: 315
    Lyderystes_macas: NERA
    Ilgiausia_serija: 1
    Treniruociu_iki_tikslo: 29
    Geriausias_macas: Panevezys 80
    Blogiausias_macas: Kaunas 50

    Lyderiu_lentele:
    1. Panevezys 80
    2. Klaipeda 70
    3. Vilnius 60
    4. Siauliai 55
    5. Kaunas 50

---

## Kaip skaičiuojami 1 testo rezultatai

Zalgiris: taskai=85, klaidos=5, baudos=10, laimejo=1
  efektyvumas = 85 - 5 + 10 = 90.00 → Puikus
  kaupiamoji = 0 + 85 = 85
  serija: laimejo → dabartine=1, ilgiausia=1
  85 > 200? Ne → vėliavėlė dar nerasta
  geriausias=Zalgiris(85), blogiausias=Zalgiris(85) [pirmasis mačas]

Rytas: taskai=70, klaidos=8, baudos=5, laimejo=0
  efektyvumas = 70 - 8 + 5 = 67.00 → Geras
  kaupiamoji = 85 + 70 = 155
  serija: pralaimejo → dabartine=0, ilgiausia lieka 1
  155 > 200? Ne
  70 < 85 → blogiausias=Rytas(70)

Wolves: taskai=90, klaidos=3, baudos=12, laimejo=1
  efektyvumas = 90 - 3 + 12 = 99.00 → Puikus
  kaupiamoji = 155 + 90 = 245
  serija: laimejo → dabartine=1, ilgiausia=1
  245 > 200? Taip → lyderystes_macas = Wolves
  90 > 85 → geriausias=Wolves(90)

Neptuno: taskai=60, klaidos=10, baudos=8, laimejo=1
  efektyvumas = 60 - 10 + 8 = 58.00 → Geras
  kaupiamoji = 245 + 60 = 305
  serija: laimejo → dabartine=2, ilgiausia=2
  60 < 70 → blogiausias=Neptuno(60)

Treniruotės: 305 + 7×15 = 410 >= 400 → 7

Lyderių lentelė — macu_taskai = [85, 70, 90, 60], macu_vardai = [Zalgiris, Rytas, Wolves, Neptuno]

Selection sort (nuo didžiausio):
  i=0: maks ind=2 (90). Sukeičiam [0]↔[2]:
       taskai=[90,70,85,60], vardai=[Wolves,Rytas,Zalgiris,Neptuno]
  i=1: maks ind=2 (85). Sukeičiam [1]↔[2]:
       taskai=[90,85,70,60], vardai=[Wolves,Zalgiris,Rytas,Neptuno]
  i=2: maks ind=2 (70). Niekas nesikeičia.
  i=3: vienintelis likęs. Baigta.
  Rezultatas: Wolves:90, Zalgiris:85, Rytas:70, Neptuno:60 ✓

"""

# Tavo kodas žemiau:
