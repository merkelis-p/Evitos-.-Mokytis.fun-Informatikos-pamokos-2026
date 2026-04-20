# Git ir GitHub pradedančiojo gidas

Šis dokumentas skirtas mokiniams, kurie pradeda dirbti su GitHub ir nori išmokti klonuoti repozitoriją, suprasti Git pagrindus ir įkelti savo kodą per terminalą.

Šios pamokos metu repozitorija dar bus **public**, todėl pradžiai naudosime paprastesnį kelią. Iki `SSH` dalies šiame gide yra visa informacija, kurios reikia pradėti darbą: susikurti GitHub, įsidiegti Git, nusiklonuoti repozitoriją ir išmokti bazinį ciklą `clone -> status -> add -> commit -> push -> pull`.

Kai žemiau prasidės `SSH` dalis, ten jau bus papildomas žingsnis vėlesniam etapui. Iki tos vietos perskaičius toliau skaityti nebūtina.

Atnaujinta: **2026-04-05**.

## Turinys
- [Git ir GitHub pradedančiojo gidas](#git-ir-github-pradedančiojo-gidas)
  - [Turinys](#turinys)
  - [1. Kas yra Git ir GitHub](#1-kas-yra-git-ir-github)
    - [Kas yra Git?](#kas-yra-git)
    - [Kas yra GitHub?](#kas-yra-github)
  - [2. Kam reikalingas versijavimas](#2-kam-reikalingas-versijavimas)
  - [3. Pirma dalis: ko užtenka dabar](#3-pirma-dalis-ko-užtenka-dabar)
  - [3a. Terminalas ir navigacija](#3a-terminalas-ir-navigacija)
  - [4. 1 žingsnis: susikurkite GitHub paskyrą](#4-1-žingsnis-susikurkite-github-paskyrą)
  - [5. 2 žingsnis: įsidiekite Git](#5-2-žingsnis-įsidiekite-git)
    - [macOS](#macos)
    - [Windows](#windows)
      - [Variantas A: per oficialų diegiklį](#variantas-a-per-oficialų-diegiklį)
      - [Variantas B: per `winget`](#variantas-b-per-winget)
  - [6. 3 žingsnis: pirmas Git paruošimas kompiuteryje](#6-3-žingsnis-pirmas-git-paruošimas-kompiuteryje)
  - [7. 4 žingsnis: atsiųskite savo GitHub vardą](#7-4-žingsnis-atsiųskite-savo-github-vardą)
  - [8. 5 žingsnis: klonuokite repozitoriją](#8-5-žingsnis-klonuokite-repozitoriją)
    - [Kas yra `git clone`](#kas-yra-git-clone)
    - [Klonavimas šiai pamokai](#klonavimas-šiai-pamokai)
  - [9. 6 žingsnis: pagrindinės Git komandos](#9-6-žingsnis-pagrindinės-git-komandos)
    - [`git status`](#git-status)
    - [`git add`](#git-add)
    - [`git commit`](#git-commit)
    - [`git push`](#git-push)
    - [`git pull`](#git-pull)
    - [`git log`](#git-log)
  - [10. 7 žingsnis: kaip sukelti pakoregavimus](#10-7-žingsnis-kaip-sukelti-pakoregavimus)
  - [11. Ar dabar reikia branchų](#11-ar-dabar-reikia-branchų)
    - [Kas yra branch labai trumpai](#kas-yra-branch-labai-trumpai)
  - [12. Kas yra merge conflict](#12-kas-yra-merge-conflict)
  - [13. Kur galima sustoti po pirmos dalies](#13-kur-galima-sustoti-po-pirmos-dalies)
  - [14. Antra dalis: SSH ir private repo](#14-antra-dalis-ssh-ir-private-repo)
  - [15. 8 žingsnis: susigeneruokite SSH raktą](#15-8-žingsnis-susigeneruokite-ssh-raktą)
    - [macOS ir Windows](#macos-ir-windows)
    - [Kur išsisaugo raktai](#kur-išsisaugo-raktai)
      - [macOS](#macos-1)
      - [Windows](#windows-1)
  - [16. 9 žingsnis: pridėkite SSH raktą prie GitHub](#16-9-žingsnis-pridėkite-ssh-raktą-prie-github)
    - [1. Nukopijuokite viešąjį raktą](#1-nukopijuokite-viešąjį-raktą)
      - [macOS](#macos-2)
      - [Windows PowerShell](#windows-powershell)
    - [2. Įkelkite raktą į GitHub](#2-įkelkite-raktą-į-github)
    - [3. Patikrinkite ryšį](#3-patikrinkite-ryšį)
  - [17. Dažniausios problemos](#17-dažniausios-problemos)
    - [`git` komanda neveikia](#git-komanda-neveikia)
    - [`Permission denied (publickey)`](#permission-denied-publickey)
    - [Repozitoriją atsisiunčiau kaip `.zip`](#repozitoriją-atsisiunčiau-kaip-zip)
    - [`git push` prašo teisių arba neveikia](#git-push-prašo-teisių-arba-neveikia)
    - [Kaip pamatyti, prie kokios nuotolinės repozitorijos esate prijungti](#kaip-pamatyti-prie-kokios-nuotolinės-repozitorijos-esate-prijungti)
  - [Svarbiausia mintis pabaigai](#svarbiausia-mintis-pabaigai)

## 1. Kas yra Git ir GitHub

### Kas yra Git?

**Git** yra versijavimo įrankis. Jis leidžia sekti, kas pasikeitė tavo failuose per laiką.

Su Git galima:

- išsisaugoti darbo būsenas;
- matyti, kokie failai pasikeitė;
- grįžti prie ankstesnių versijų;
- dirbti komandoje, kai keli žmonės keičia tą patį projektą.

### Kas yra GitHub?

**GitHub** yra internetinė platforma, kurioje laikomos Git repozitorijos.

Labai supaprastintai:

- `Git` yra įrankis kompiuteryje;
- `GitHub` yra vieta internete, kur laikai projektą ir daliniesi juo su kitais.

---

## 2. Kam reikalingas versijavimas

Versijavimas reikalingas tam, kad nereikėtų laikyti tokių failų:

- `projektas_galutinis.py`
- `projektas_galutinis2.py`
- `projektas_tikras_galutinis.py`
- `projektas_tikras_galutinis_paskutinis.py`

Git leidžia normaliai dirbti su viena projekto versija ir išsisaugoti pakeitimus tvarkingai.

Galima galvoti taip:

- **failas** yra tavo dabartinis darbas;
- **commit** yra išsaugotas darbo taškas su trumpu paaiškinimu;
- **Git istorija** yra tavo projekto laiko juosta.

Pavyzdžiui:

1. Sukūrei pirmą programos versiją.
2. Išsaugojai commit: `Sukurtas pirmas programos variantas`.
3. Vėliau pridėjai `if` sąlygas.
4. Išsaugojai commit: `Pridėtos sąlygos`.

Jei po to ką nors sugadini, gali matyti, kur kas pasikeitė, ir daug lengviau atsistatyti.

---

## 3. Pirma dalis: ko užtenka dabar

Jei tikslas yra jau dabar pradėti dirbti su pamokų repozitorija ir kelti namų darbus, pradžiai užtenka šitų dalykų:

- GitHub paskyros;
- įdiegto `Git` kompiuteryje;
- terminalo;
- nuorodos į repozitoriją;
- GitHub username, kurį atsiųsite mokytojui.

Šitai yra dabartinis prioritetas:

- susikurti paskyrą;
- įsidiegti `Git`;
- atsiųsti savo GitHub username;
- išmokti `git clone`;
- suprasti, kaip po pakeitimų naudoti `status`, `add`, `commit`, `push` ir `pull`.

Jei dar nesate įsidiegę įrankių, naudokitės šiuo gidu:

[VS_CODE_SETUP_GUIDE.md](./VS_CODE_SETUP_GUIDE.md)

Ypač svarbios dalys:

- `0 žingsnis: diegiame DEV tools`
- `1 žingsnis: susikurkite GitHub paskyrą`
- `2 žingsnis: įsidiekite VS Code`

---

## 3a. Terminalas ir navigacija

Prieš naudojant Git, reikia mokėti atidaryti terminalą ir eiti į teisingą aplanką. Jei to nežinai — perskaityk šitą dalį atidžiai.

---

### Kas yra terminalas?

Terminalas — tai langas, kuriame galima vesti **tekstines komandas**. Dažnai sakoma: „paleisk terminale", „įvesk komandą terminale" arba „atidaryk terminalą".

Terminalas **nėra** VS Code. Terminalas **nėra** naršyklė. Tai atskiras langas, į kurį rašai komandas ir spaudžiai `Enter`.

---

### Kaip atidaryti terminalą (Windows)

Naudojame **PowerShell** arba **Command Prompt** (`cmd`). Paprasčiausias būdas:

1. Spausk klavišus `Win` + `R` (arba dešinį pelės klavišą ant „Start" mygtuko).
2. Įvesk `powershell` ir spausk `Enter`.

Arba:

1. Spausk mygtuką „Start" (apatinis kairys kampas).
2. Įvesk `powershell` paieškos laukelyje.
3. Spausk `Enter` arba spauski ant „Windows PowerShell".

Atsidarys **mėlynas (arba juodas) langas** su tekstu. Ten galima rašyti komandas.

> Jei naudoji VS Code — yra ir integruotas terminalas: meniu viršuje `Terminal → New Terminal`. Tačiau patikimiau pradžioje dirbti atskirame PowerShell lange.

---

### pwd — kur esu?

`pwd` parodo, **kuriame aplanke šiuo metu esi**.

```
pwd
```

Pavyzdys — gautas atsakymas:

```
C:\Users\evita
```

Tai reiškia, kad dabar esi `evita` vartotojo aplanke. Prieš dirbant su Git, reikia **eiti į repozitorijos aplanką** (žiūrėk `cd` žemiau).

---

### ls / dir — kas yra šiame aplanke?

`ls` arba `dir` parodo, **kokie failai ir aplankai yra toje vietoje, kur esi**.

PowerShell:

```
ls
```

Command Prompt (cmd):

```
dir
```

Tai naudinga, kai nori patikrinti — ar tikrai esi ten, kur manai, ir ar yra reikiami failai.

---

### cd — eiti į aplanką

`cd` (change directory) keičia, **kuriame aplanke esi**.

```
cd PavadinImas
```

Pavyzdys — eiti į aplanką `20260409-20260416-pamoka`:

```
cd 20260409-20260416-pamoka
```

Po to `pwd` parodys:

```
C:\Users\evita\Evitos-.-Mokytis.fun-Informatikos-pamokos-2026\20260409-20260416-pamoka
```

---

### cd .. — grįžti atgal vienu lygiu

`cd ..` grįžta **vienu lygiu aukščiau** — tai yra į aplanką, kuriame yra dabartinis aplankas.

```
cd ..
```

Pavyzdys:

```
cd 20260409-20260416-pamoka   # eini į pamokos aplanką
cd ..                          # grįžti atgal į repozitorijos šaknį
```

---

### Praktinis pavyzdys: kaip eiti į repozitorijos aplanką

Kai atidarai **naują terminalą**, dažniausiai esi `C:\Users\evita\` arba panašioje vietoje.

Reikia eiti į repozitorijos aplanką. Tai daroma su pilnu keliu:

```
cd C:\Users\evita\Evitos-.-Mokytis.fun-Informatikos-pamokos-2026
```

Patikrinimui:

```
pwd
```

Turėtų parodyti:

```
C:\Users\evita\Evitos-.-Mokytis.fun-Informatikos-pamokos-2026
```

Ir:

```
ls
```

Turėtų parodyti aplankus kaip `20260409-20260416-pamoka`, `20260402-pamoka`, `docs`, `README.md` ir t.t.

**Tik tada** galima naudoti `git pull`, `git add`, `git commit`, `git push`.

---

### Dažna klaida: git komandos rašomos ne ten

Jei matai klaidas kaip:

```
fatal: not a git repository
```

Tai reiškia, kad esi **ne tame aplanke**. Reikia grįžti į repozitorijos aplanką:

```
cd C:\Users\evita\Evitos-.-Mokytis.fun-Informatikos-pamokos-2026
```

Ir bandyti iš naujo.

---

## 4. 1 žingsnis: susikurkite GitHub paskyrą

1. Atidarykite:
<https://github.com/signup>
2. Susikurkite paskyrą.
3. Patvirtinkite el. paštą.
4. Prisijunkite prie GitHub naršyklėje.

Rekomendacija:

- naudokite tvarkingą naudotojo vardą;
- geriausia be keistų simbolių;
- vardą, kurį galima bus normaliai naudoti pamokose ir projektuose.

Pavyzdys:

- `evita-programuoja`
- `evitak123`

Blogesni pavyzdžiai:

- `xx_dark_princess_xx_999`
- `kazkaslol`

---

## 5. 2 žingsnis: įsidiekite Git

### macOS

Jei dar neįdiegta, terminale paleiskite:

```bash
xcode-select --install
```

Po to patikrinkite:

```bash
git --version
```

### Windows

Galimi du keliai.

#### Variantas A: per oficialų diegiklį

1. Atsisiųskite iš:
<https://git-scm.com/install/windows>
2. Įdiekite pagal vedlį.

#### Variantas B: per `winget`

PowerShell lange:

```powershell
winget install --id Git.Git -e --source winget
```

Po diegimo patikrinkite:

```powershell
git --version
```

Jei `git --version` neveikia, uždarykite terminalą ir atidarykite iš naujo.

---

## 6. 3 žingsnis: pirmas Git paruošimas kompiuteryje

Git reikia pasakyti, kas jūs esate.

Terminale paleiskite:

```bash
git config --global user.name "Jūsų Vardas"
git config --global user.email "jusu.elpastas@example.com"
```

Pavyzdys:

```bash
git config --global user.name "Evita"
git config --global user.email "evita@example.com"
```

Patikrinimui:

```bash
git config --global --list
```

Ten turėtumėte matyti bent:

- `user.name=...`
- `user.email=...`

Svarbu:

- `user.name` nėra GitHub username;
- tai vardas, kuris bus rodomas commit istorijoje.

---

## 7. 4 žingsnis: atsiųskite savo GitHub vardą

Kai jau turite GitHub paskyrą, atsiųskite savo **GitHub username** mokytojui.

Reikia siųsti būtent username, pavyzdžiui:

- `evitak123`
- `evita-programuoja`

Nereikia siųsti:

- slaptažodžio;
- SSH rakto;
- el. pašto slaptažodžio;
- privataus rakto failo.

Kam to reikia:

- kad jus būtų galima pridėti prie pamokų repozitorijos;
- kad vėliau turėtumėte prieigą prie privačių projektų;
- kad kitose pamokose galėtumėte normaliai naudoti `pull` ir `push`.

---

## 8. 5 žingsnis: klonuokite repozitoriją

Šitai yra pagrindinis šios pamokos praktinis žingsnis.

Kadangi repozitorija kol kas bus **public**, pradžiai naudosime paprastesnį variantą ir tiesiog ją nusiklonuosime. Taip iš karto turėsite realų projektą savo kompiuteryje ir galėsite praktiškai pamatyti, kaip veikia Git.

Svarbi taisyklė:

> Repozitorijos nesisiunčiame kaip `.zip`, o klonuojame su `git clone`.

Kodėl ne `.zip`:

- `.zip` neturi Git istorijos;
- `.zip` neturi normalaus ryšio su GitHub;
- iš `.zip` negalėsite normaliai daryti `pull` ir `push`.

### Kas yra `git clone`

`git clone` sukuria pilną projekto kopiją jūsų kompiuteryje kartu su Git istorija.

Tai reiškia, kad gaunate:

- visus projekto failus;
- ryšį su GitHub repozitorija;
- galimybę daryti `pull`, `commit`, `push`.

### Klonavimas šiai pamokai

GitHub repozitorijoje spauskite `Code` ir nukopijuokite klonavimo nuorodą.

Pradžiai naudosime paprastą variantą, nes repo viešas.

Pavyzdys:

```bash
git clone https://github.com/merkelis-p/Evitos-.-Mokytis.fun-Informatikos-pamokos-2026.git
```

Po to:

```bash
cd Evitos-.-Mokytis.fun-Informatikos-pamokos-2026
git status
```

Jei viskas gerai, pamatysite, kad repozitorija sėkmingai nuklonuota.

Trumpai:

- dabar: `public repo` ir paprastas `git clone`;
- vėliau: `private repo`, `SSH` raktas ir pilnas darbas per `SSH`.

---

## 9. 6 žingsnis: pagrindinės Git komandos

Kol kas svarbiausios komandos yra šitos:

### `git status`

Parodo, kas pasikeitė.

```bash
git status
```

### `git add`

Paruošia failus commitui.

Vienas failas:

```bash
git add nd1.py
```

Visi pakeitimai:

```bash
git add .
```

### `git commit`

Išsaugo pakeitimus istorijoje.

```bash
git commit -m "Pridėtas nd1 sprendimas"
```

### `git push`

Išsiunčia commitus į GitHub.

```bash
git push
```

### `git pull`

Parsisiunčia naujausius pakeitimus iš GitHub.

```bash
git pull
```

### `git log`

Parodo commit istoriją.

```bash
git log --oneline
```

---

## 10. 7 žingsnis: kaip sukelti pakoregavimus

Kai jau būsite nusiklonavę repozitoriją ir ką nors pakoreguosite, kėlimas vyksta taip:

1. Atsidarykite terminalą repozitorijos aplanke.
2. Pasižiūrėkite, kas pasikeitė:

```bash
git status
```

3. Pridėkite pakeitimus:

```bash
git add .
```

4. Sukurkite commit su trumpu paaiškinimu:

```bash
git commit -m "Atnaujinti namu darbai"
```

5. Išsiųskite pakeitimus:

```bash
git push
```

Jei prieš tai kažkas jau įkėlė naujesnius pakeitimus, pirmiau gali reikėti:

```bash
git pull
```

Trumpa kasdienė seka:

```bash
git status
git add .
git commit -m "Trumpas komentaras"
git push
```

Jei `git push` nepavyksta dėl teisių ar prisijungimo, nebandykite spėlioti. Tada pereikite prie `SSH` dalies arba kreipkitės pagalbos.

---

## 11. Ar dabar reikia branchų

Trumpas atsakymas:

> Kol kas ne.

Pradžioje daug svarbiau suprasti:

- kas yra repozitorija;
- kas yra commit;
- kaip veikia `clone`;
- kaip naudoti `pull` ir `push`;
- kaip nepamesti pakeitimų.

### Kas yra branch labai trumpai

Branch yra atskira darbo šaka.

Ji naudinga, kai:

- keli žmonės daro skirtingus darbus;
- nori eksperimentuoti nesugadindamas pagrindinės versijos;
- dirbi didesniuose projektuose.

Bet pradedančiajam per anksti viską krauti iš karto.

Todėl kol kas dirbsime taip:

- `clone`
- `pull`
- `add`
- `commit`
- `push`

Branchus galima įtraukti vėliau, kai šitas ciklas taps natūralus.

---

## 12. Kas yra merge conflict

`Merge conflict` atsiranda tada, kai Git nebežino, kuri failo versija yra teisinga.

Dažniausiai taip nutinka, kai:

- jūs pakeitėte failą;
- kitas žmogus tuo pačiu metu pakeitė tą pačią vietą;
- po to bandote daryti `pull` arba `merge`.

Pradžioje svarbiausia ne „išmokti konfliktus idealiai spręsti“, o suprasti, kodėl jie atsiranda.

Saugiausia taisyklė pradžiai:

1. Prieš darbą daryti `git pull`.
2. Dirbti tvarkingai ir dažnai commitinti.
3. Jei atsiranda konfliktas, neskubėti ir kviestis pagalbos.

---

## 13. Kur galima sustoti po pirmos dalies

Jei perskaitėte iki čia, tai jau turite viską, ko reikia pradėti darbą:

1. Susikurti GitHub.
2. Įsidiegti `Git`.
3. Atsiųsti savo GitHub username.
4. Nusiklonuoti repozitoriją.
5. Pakoreguoti failus.
6. Naudoti `git status`, `git add`, `git commit`, `git push`, `git pull`.

Tai yra vieta, kur galima sustoti. Toliau esanti dalis jau skirta kitam žingsniui, kai repo bus privatus arba kai norėsite saugaus prisijungimo per `SSH`.

---

## 14. Antra dalis: SSH ir private repo

Nuo šitos vietos skaityti reikia tik tada, kai:

- repozitorija jau tapo privati;
- `git push` prašo papildomo prisijungimo;
- norite prisijungti prie GitHub patikimiau ir patogiau.

SSH raktas reikalingas tam, kad kompiuteris galėtų saugiai jungtis prie GitHub be slaptažodžio kiekvieną kartą.

Tai ypač patogu dirbant su:

- privačiomis repozitorijomis;
- `git clone`;
- `git push`;
- `git pull`.

---

## 15. 8 žingsnis: susigeneruokite SSH raktą

### macOS ir Windows

Komanda abiejose sistemose praktiškai ta pati:

```bash
ssh-keygen -t ed25519 -C "jusu.elpastas@example.com"
```

Pavyzdys:

```bash
ssh-keygen -t ed25519 -C "evita@example.com"
```

Toliau pamatysite maždaug tokius klausimus:

```text
Enter file in which to save the key (...):
```

Dažniausiai tiesiog spauskite `Enter`.

Po to klaus:

```text
Enter passphrase:
```

Galite:

- įvesti slaptafrazę, jei norite daugiau saugumo;
- arba spausti `Enter`, jei kol kas norite paprasčiau.

### Kur išsisaugo raktai

#### macOS

Dažniausiai čia:

```text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

#### Windows

Dažniausiai čia:

```text
C:\Users\JusuVardas\.ssh\id_ed25519
C:\Users\JusuVardas\.ssh\id_ed25519.pub
```

Svarbu:

- `id_ed25519` yra **privatus** raktas, jo niekam nesiųskite;
- `id_ed25519.pub` yra **viešasis** raktas, būtent jį reikės įkelti į GitHub.

---

## 16. 9 žingsnis: pridėkite SSH raktą prie GitHub

### 1. Nukopijuokite viešąjį raktą

#### macOS

```bash
cat ~/.ssh/id_ed25519.pub
```

Nukopijuokite visą išvestą eilutę.

Jei norite iš karto į clipboard:

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

#### Windows PowerShell

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
```

Arba nukopijavimui į clipboard:

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard
```

### 2. Įkelkite raktą į GitHub

1. Atidarykite GitHub.
2. Eikite į:
<https://github.com/settings/keys>
3. Spauskite `New SSH key`.
4. Į lauką `Title` įrašykite, pvz.:
   - `MacBook Evita`
   - `Windows laptop`
5. Į lauką `Key` įklijuokite viešąjį raktą.
6. Spauskite `Add SSH key`.

### 3. Patikrinkite ryšį

Terminale paleiskite:

```bash
ssh -T git@github.com
```

Pirmą kartą gali paklausti:

```text
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Rašykite:

```text
yes
```

Jei viskas gerai, pamatysite maždaug tokią žinutę:

```text
Hi username! You've successfully authenticated...
```

---

## 17. Dažniausios problemos

### `git` komanda neveikia

Patikrinkite:

```bash
git --version
```

Jei neveikia, Git neįdiegtas arba terminalas neatnaujintas.

### `Permission denied (publickey)`

Dažniausiai reiškia:

- nėra SSH rakto;
- SSH raktas nepridėtas į GitHub;
- klonuojate per SSH, bet autentikacija nesuveikė.

Patikrinkite:

```bash
ssh -T git@github.com
```

### Repozitoriją atsisiunčiau kaip `.zip`

Tai neteisingas kelias darbui su Git.

Sprendimas:

1. Ištrinti `.zip` kopiją arba bent jos nenaudoti Git darbui.
2. Klonuoti iš naujo su:

```bash
git clone https://github.com/owner/repozitorija.git
```

### `git push` prašo teisių arba neveikia

Dažniausios priežastys:

- nesate pridėti prie repozitorijos;
- naudojate blogą nuorodą;
- SSH raktas nepridėtas;
- bandote pushinti ten, kur neturite leidimo.

### Kaip pamatyti, prie kokios nuotolinės repozitorijos esate prijungti

```bash
git remote -v
```

---

## Svarbiausia mintis pabaigai

Pradžioje nereikia bandyti išmokti viso Git iš karto.

Šios pamokos tikslui pakanka suprasti šitą seką:

1. Turėti GitHub paskyrą.
2. Turėti Git kompiuteryje.
3. Atsiųsti savo GitHub username.
4. Gauti nuorodą į repozitoriją.
5. Naudoti `git clone`, ne `.zip`.
6. Mokėti po pakeitimų naudoti `git status`, `git add`, `git commit`, `git push` ir `git pull`.

Kitos pamokos tikslas jau bus šitas:

1. Susitvarkyti SSH raktą.
2. Prisijungti prie privačios repozitorijos.
3. Dirbti ciklu:

```bash
git pull
git add .
git commit -m "Trumpas komentaras"
git push
```

Kai šita dalis taps natūrali, tada bus labai lengva mokytis:

- branchų;
- pull requestų;
- merge conflict sprendimo;
- normalesnio komandinio darbo.







