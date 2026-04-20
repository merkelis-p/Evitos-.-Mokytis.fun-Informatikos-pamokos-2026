"""

## Situacija

Miesto technologijų festivalyje vyksta „Robotų Arena“. Kiekviena komanda atveda savo robotą, kuris renka taškus, pergales, bonusus ir kartais gauna baudų. Tavo programa turi iš vieno turnyro duomenų:

- apskaičiuoti kiekvienos komandos galutinius taškus;
- nustatyti medalius;
- atrinkti finalistus;
- rasti rizikos komandas;
- sužaisti „Boss level“ etapą ir suskaičiuoti, kiek treniruočių reikia silpniausiai aktyviai komandai pasiekti finalo ribą.

Šią užduotį galima pilnai išspręsti ir be `list`, ir be `dictionary`. Galima skaityti komandas po vieną, iš karto apskaičiuoti jų eilutę `Bronzos_lyga` daliai ir tuo pačiu atsinaujinti bendrus skaitiklius, vardus bei tarpinius atsakymus.

---

## Etapai

### 1. Bronzos lyga

Kiekvienai komandai reikia apskaičiuoti jos galutinius taškus, taškų vidurkį per rungtį, medalį ir taškų „kodą“ iš dešimčių bei liekanos.

### 2. Finalo komisija

Reikia nustatyti, kurios komandos patenka į finalą, kiek komandų tiksliai pasiekė finalo ribą ir kiek komandų laikomos tvarkingomis.

### 3. Komandų radaras

Reikia rasti pirmą komandą, kuri surinko daugiau nei 90 taškų, suskaičiuoti rizikos komandas ir komandas, kurios gavo bent vieną bonusą.

### 4. Boss level

Reikia rasti silpniausią aktyvią komandą ir su `while` ciklu suskaičiuoti, kiek treniruočių jai reikia, kad pasiektų finalo ribą.

---

## Įvestis

Pirmoje eilutėje pateikiami trys sveikieji skaičiai:

- `n` – komandų skaičius;
- `r` – finalo riba;
- `p` – kiek taškų komanda gauna per vieną treniruotę Boss level etape.

Toliau pateikiamos `n` eilučių. Kiekvienoje eilutėje yra:

- komandos pavadinimas `vardas`;
- baziniai taškai `taskai`;
- pergalių skaičius `pergales`;
- bonusų skaičius `bonusai`;
- baudų skaičius `baudos`;
- rungčių skaičius `rungtys`;
- diskvalifikacijos požymis `disk`, kur `0` reiškia ne diskvalifikuota, o `1` reiškia diskvalifikuota.

Visi duomenys vienoje eilutėje atskirti tarpais.

---

## Taisyklės

### Galutiniai taškai

Komandos galutiniai taškai apskaičiuojami taip:

- prie bazinių taškų pridedamas pergalių skaičiaus kvadratas;
- pridedama po 2 taškus už kiekvieną bonusą;
- atimamos baudos.

### Vidurkis

Vidurkis yra galutinių taškų ir rungčių skaičiaus santykis.

Vidurkį išvesk tiksliai dviem skaitmenimis po kablelio. Pavyzdžiui, jei gauni 17, turi būti spausdinama `17.00`, o jei gauni 29 ir trečdalį, turi būti spausdinama `29.33`.

### Taškų kodas

Kiekvienai komandai reikia rasti:

- kiek pilnų dešimčių telpa jos galutiniuose taškuose;
- kokia liekana lieka padalijus galutinius taškus iš 10.

### Medaliai

- jei komanda diskvalifikuota, ji negauna įprasto medalio ir turi būti pažymėta kaip `Diskvalifikuota`;
- jei komanda nėra diskvalifikuota ir surinko bent 100 taškų, ji gauna `Auksas`;
- jei komanda nėra diskvalifikuota ir surinko bent 80 taškų, ji gauna `Sidabras`;
- jei komanda nėra diskvalifikuota ir surinko bent 60 taškų, ji gauna `Bronza`;
- kitu atveju spausdink `Be_medalio`.

### Finalistai

Į finalą patenka tik tos komandos, kurios:

- nėra diskvalifikuotos;
- surinko ne mažiau taškų negu finalo riba `r`.

### Tvarkinga komanda

Komanda laikoma tvarkinga, jei ji nėra diskvalifikuota ir turi ne daugiau kaip 10 baudų.

### Rizikos komanda

Komanda laikoma rizikos komanda, jei jos galutiniai taškai mažesni už 50 arba ji turi daugiau nei 20 baudų.

### Bonusų komanda

Komanda laikoma bonusų komanda, jei gavo bent vieną bonusą.

### Boss level

Rask silpniausią aktyvią komandą, tai yra komandą su mažiausiu galutinių taškų skaičiumi tarp tų, kurios nėra diskvalifikuotos.

Jei tokių komandų nėra, išvesk:

```text
Silpniausia_komanda: NERA
Treniruociu_iki_finalo: 0
```

Jei tokia komanda yra, suskaičiuok, kiek treniruočių reikia, kad ji pasiektų bent finalo ribą. Per vieną treniruotę ji gauna `p` taškų. Čia tikimasi `while` ciklo.

---

## Išvestis

Programa turi išvesti **tiksliai** tokį formatą.

Pirmiausia:

```text
Bronzos_lyga:
```

Toliau – po vieną eilutę kiekvienai komandai ta pačia tvarka, kaip jos pateiktos įvestyje:

```text
vardas galutiniai vidurkis medalis desimtys likutis
```

Po to palik vieną tuščią eilutę ir išvesk:

```text
Finalo_komisija:
Finalistu_skaicius: x
Finalistai: vardas1 vardas2 ...
Tiksliai_ant_ribos: y
Tvarkingos_komandos: z
```

Jei finalistų nėra, vietoje vardų spausdink `NERA`.

Po to palik vieną tuščią eilutę ir išvesk:

```text
Komandu_radaras:
Pirma_virs_90: vardas
Rizikos_komandos: a
Bonusu_komandos: b
```

Jei nėra nė vienos komandos, surinkusios daugiau nei 90 taškų, spausdink `NERA`.

Po to palik vieną tuščią eilutę ir išvesk:

```text
Boss_level:
Silpniausia_komanda: vardas
Treniruociu_iki_finalo: c
```

---

## Svarbios pastabos

1. Programa turi veikti su **bet kokiais teisingais testais**, ne tik su pavyzdžiu.
2. Neprirašyk papildomo teksto, kurio nėra aprašyme.
3. Komandų pavadinimai yra iš vieno žodžio.
4. Testai bus įvairūs, todėl negalima sprendimo pririšti prie konkrečių reikšmių.
5. Testai sudaryti taip, kad `galutiniai` bus neneigiami.
6. `Bronzos_lyga` dalyje vidurkis turi būti spausdinamas dviem skaitmenimis po kablelio.
7. `Finalistai` eilutėje komandas spausdink ta pačia tvarka, kaip jos buvo įvestos.
8. Užduotyje sąmoningai neparašytos beveik gatavos Python formulės. Idėja tokia, kad pati paverstum taisykles į kodą.
9. Jei dar nesimokėte sąrašų ir žodynų, tai nėra kliūtis šiai užduočiai.
10. Užtenka mokėti dirbti su paprastais kintamaisiais, `for`, `while`, `if`, skaitikliais ir teksto spausdinimu.

---

## Ko čia tikrai prireiks

- veiksmų su skaičiais;
- loginių patikrinimų;
- šakotų sąlygų;
- bent vieno `for` ciklo;
- bent vieno `while` ciklo;
- tikslaus spausdinimo formato.

---

## Pavyzdžiai

| Testas | stdin | stdout |
|---|---|---|
| 1 | `3 80 8`<br>`Aidas 70 4 1 0 3 0`<br>`Beta 45 2 1 0 3 0`<br>`Cyra 78 4 4 0 3 0` | `Bronzos_lyga:`<br>`Aidas 88 29.33 Sidabras 8 8`<br>`Beta 51 17.00 Be_medalio 5 1`<br>`Cyra 102 34.00 Auksas 10 2`<br><br>`Finalo_komisija:`<br>`Finalistu_skaicius: 2`<br>`Finalistai: Aidas Cyra`<br>`Tiksliai_ant_ribos: 0`<br>`Tvarkingos_komandos: 3`<br><br>`Komandu_radaras:`<br>`Pirma_virs_90: Cyra`<br>`Rizikos_komandos: 0`<br>`Bonusu_komandos: 3`<br><br>`Boss_level:`<br>`Silpniausia_komanda: Beta`<br>`Treniruociu_iki_finalo: 4` |
| 2 | `4 75 5`<br>`Nova 60 3 0 5 2 0`<br>`Orka 72 2 4 0 4 1`<br>`Pulsar 73 1 1 0 3 0`<br>`Rytas 74 4 0 25 4 0` | `Bronzos_lyga:`<br>`Nova 64 32.00 Bronza 6 4`<br>`Orka 84 21.00 Diskvalifikuota 8 4`<br>`Pulsar 76 25.33 Bronza 7 6`<br>`Rytas 65 16.25 Bronza 6 5`<br><br>`Finalo_komisija:`<br>`Finalistu_skaicius: 1`<br>`Finalistai: Pulsar`<br>`Tiksliai_ant_ribos: 0`<br>`Tvarkingos_komandos: 2`<br><br>`Komandu_radaras:`<br>`Pirma_virs_90: NERA`<br>`Rizikos_komandos: 1`<br>`Bonusu_komandos: 2`<br><br>`Boss_level:`<br>`Silpniausia_komanda: Nova`<br>`Treniruociu_iki_finalo: 3` |
| 3 | `2 80 10`<br>`Zen 80 0 0 0 4 1`<br>`Yra 50 0 0 0 5 1` | `Bronzos_lyga:`<br>`Zen 80 20.00 Diskvalifikuota 8 0`<br>`Yra 50 10.00 Diskvalifikuota 5 0`<br><br>`Finalo_komisija:`<br>`Finalistu_skaicius: 0`<br>`Finalistai: NERA`<br>`Tiksliai_ant_ribos: 1`<br>`Tvarkingos_komandos: 0`<br><br>`Komandu_radaras:`<br>`Pirma_virs_90: NERA`<br>`Rizikos_komandos: 0`<br>`Bonusu_komandos: 0`<br><br>`Boss_level:`<br>`Silpniausia_komanda: NERA`<br>`Treniruociu_iki_finalo: 0` |




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








- komandos pavadinimas `vardas`;
- baziniai taškai `taskai`;
- pergalių skaičius `pergales`;
- bonusų skaičius `bonusai`;
- baudų skaičius `baudos`;
- rungčių skaičius `rungtys`;
- diskvalifikacijos požymis `disk`, kur `0` reiškia ne diskvalifikuota, o `1` reiškia diskvalifikuota.


### Galutiniai taškai

Komandos galutiniai taškai apskaičiuojami taip:

- prie bazinių taškų pridedamas pergalių skaičiaus kvadratas;
- pridedama po 2 taškus už kiekvieną bonusą;
- atimamos baudos.








### Vidurkis

Vidurkis yra galutinių taškų ir rungčių skaičiaus santykis.

Vidurkį išvesk tiksliai dviem skaitmenimis po kablelio. Pavyzdžiui, jei gauni 17, turi būti spausdinama `17.00`, o jei gauni 29 ir trečdalį, turi būti spausdinama `29.33`.




### Taškų kodas

Kiekvienai komandai reikia rasti:

- kiek pilnų dešimčių telpa jos galutiniuose taškuose;
- kokia liekana lieka padalijus galutinius taškus iš 10.




Input:
3 80 8
Aidas 70 4 1 0 3 0
Beta 45 2 1 0 3 0
Cyra 78 4 4 0 3 0

Output:

Bronzos_lyga:
Aidas 88 29.33 Sidabras 8 8
Beta 51 17.00 Be_medalio 5 1
Cyra 102 34.00 Auksas 10 2

Finalo_komisija:
Finalistu_skaicius: 2
Finalistai: Aidas Cyra
Tiksliai_ant_ribos: 0
Tvarkingos_komandos: 3

Komandu_radaras:
Pirma_virs_90: Cyra
Rizikos_komandos: 0
Bonusu_komandos: 3

Boss_level:
Silpniausia_komanda: Beta
Treniruociu_iki_finalo: 4






"""
# Duomenu nuskaitymas

pirma_eilute = input().split()

n = int(pirma_eilute[0])
r = int(pirma_eilute[1])
p = int(pirma_eilute[2])

finalistu_skaicius = 0
finalistai = ""
tvarkingos_komandos = 0


print("Bronzos_lyga:")



for i in range(n):
    eilute = input().split()
    vardas = eilute[0]
    taskai = int(eilute[1])
    pergales = int(eilute[2])
    bonusai = int(eilute[3])
    baudos = int(eilute[4])
    rungtys = int(eilute[5])

    if int(eilute[6]) == 0:
        disk = False
    else:
        disk = True


    galutiniai_taskai = taskai + pergales ** 2 + bonusai * 2 - baudos
    vidurkis = galutiniai_taskai / rungtys
    
    desimtys = galutiniai_taskai // 10
    liekana = galutiniai_taskai % 10


    """
    ### Medaliai
        - jei komanda diskvalifikuota, ji negauna įprasto medalio ir turi būti pažymėta kaip `Diskvalifikuota`;
        - jei komanda nėra diskvalifikuota ir surinko bent 100 taškų, ji gauna `Auksas`;
        - jei komanda nėra diskvalifikuota ir surinko bent 80 taškų, ji gauna `Sidabras`;
        - jei komanda nėra diskvalifikuota ir surinko bent 60 taškų, ji gauna `Bronza`;
        - kitu atveju spausdink `Be_medalio`.
    
    """

    if disk == True:
        medalis = "Be_medalio"
    elif galutiniai_taskai >= 100:
        medalis = "Auksas"
    elif galutiniai_taskai >= 80:
        medalis = "Sidabras"
    elif galutiniai_taskai >= 60:
        medalis = "Bronza"
    else:
        medalis = "Be_medalio"


    # vardas galutiniai vidurkis medalis desimtys likutis
    print(f"{vardas} {galutiniai_taskai} {vidurkis} {medalis} {desimtys} {liekana}")



    if disk == True:
        continue
     
    

    """
    Į finalą patenka tik tos komandos, kurios:

        - nėra diskvalifikuotos;
        - surinko ne mažiau taškų negu finalo riba `r`.
    
    """
    
    if galutiniai_taskai >= r:
        if finalistu_skaicius == 0:
            finalistai = vardas
        else:
            finalistai = finalistai + " " + vardas
        finalistu_skaicius += 1

    if baudos <= 10:
        tvarkingos_komandos += 1

        
    

 
    