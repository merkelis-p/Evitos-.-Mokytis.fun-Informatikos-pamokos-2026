# VS Code diegimo ir paruošimo gidas (macOS + Windows)

Šis dokumentas skirtas mokiniams, kurie jungiasi į nuotolines programavimo pamokas.  
Atnaujinta: **2026-03-26**.

## Turinys
1. [Ko reikės](#ko-reikės)
2. [Įžanga: VS Code, IDE ir terminalas](#įžanga-vs-code-ide-ir-terminalas)
3. [0 žingsnis: diegiame DEV tools](#0-žingsnis-diegiame-dev-tools)
4. [1 žingsnis: susikurkite GitHub paskyrą (rekomenduojama)](#1-žingsnis-susikurkite-github-paskyrą-rekomenduojama)
5. [2 žingsnis: įsidiekite VS Code](#2-žingsnis-įsidiekite-vs-code)
6. [3 žingsnis: įsidiekite Live Share ir prisijunkite](#3-žingsnis-įsidiekite-live-share-ir-prisijunkite)
7. [4 žingsnis: programavimo kalbos paruošimas (pasirinkite vieną)](#4-žingsnis-programavimo-kalbos-paruošimas-pasirinkite-vieną)
8. [Greitas pasiruošimo patikrinimas prieš pamoką](#greitas-pasiruošimo-patikrinimas-prieš-pamoką)
9. [Dažniausios problemos ir sprendimai](#dažniausios-problemos-ir-sprendimai)

## Ko reikės
- Kompiuterio su **Windows 10/11** arba **macOS**.
- Stabilaus interneto ryšio.
- El. pašto adreso (GitHub paskyrai).
- Administratoriaus teisių (ypač Windows atveju diegiant papildomus įrankius).

Naudingos oficialios nuorodos:
- VS Code atsisiuntimas: <https://code.visualstudio.com/Download>
- VS Code Windows diegimas: <https://code.visualstudio.com/docs/setup/windows>
- VS Code macOS diegimas: <https://code.visualstudio.com/docs/setup/mac>

### Kaip naudoti šį gidą
1. Jei niekada neįdiegėte programavimo įrankių, pradėkite nuo **0 žingsnio**.
2. Tada visi mokiniai eina per **1, 2 ir 3 žingsnius**.
3. **4 žingsnyje rinkitės tik vieną kalbą**: Python **arba** C++.


## Įžanga: VS Code, IDE ir terminalas

### Kas yra IDE?
**IDE** (*Integrated Development Environment*) yra programavimo aplinka, kurioje vienoje vietoje turite:
- kodo rašymą
- klaidų tikrinimą
- paleidimą ir derinimą (debug)
- terminalą ir plėtinius

### Kas yra VS Code?
**VS Code (Visual Studio Code)** yra lengvas kodo redaktorius, kuris su plėtiniais praktiškai tampa IDE aplinka. Kitas IDE pavyzdys yra **Code::Blocks** (daugiausia C++), bet mes pasirinkome VS Code dėl:  
- veikia ir `Windows`, ir `macOS`
- palaiko `Python`, `C++` ir daug kitų kalbų
- turi `Live Share` nuotoliniam bendradarbiavimui
- yra labai populiarus ir plačiai naudojamas industrijoje

### Kas yra terminalas?
Terminalas yra tekstinė programa, per kurią duodate komandas kompiuteriui.  
Pamokose jį naudosime:
- paleisti Python/C++ programas
- įdiegti reikalingus įrankius
- valdyti projekto failus (`cd`, `ls`, `mkdir`)
- naudoti Git komandas (vėliau, kai dirbsime su versijavimu)

### Kur rasti terminalą?
#### Windows
- Atidarykite `Start` ir įveskite `Windows Terminal` (arba `PowerShell`).
- VS Code viduje: meniu `Terminal` -> `New Terminal`.
- Shortcut VS Code viduje: ``Ctrl + ` `` (atidaryti / paslėpti terminalą).

#### macOS
- Atidarykite `Spotlight` (`Cmd + Space`) ir įveskite `Terminal`.
- VS Code viduje: meniu `Terminal` -> `New Terminal`.
- Shortcut VS Code viduje: ``Ctrl + ` `` (atidaryti / paslėpti terminalą).

### Windows terminalų žemėlapis
Windows sistemoje šiame gide minimi keli terminalai. Jie nėra tas pats:

| Terminalas | Kur jį naudoti šiame gide |
|---|---|
| `PowerShell` (arba `Windows Terminal` su PowerShell profiliu) | Bendroms komandoms: `python`, `py`, `git`, `winget`, `code` |
| `MSYS2 UCRT64` | Tik C++ su `MSYS2` keliu: `pacman`, `g++`, `gdb` diegimas ir naudojimas |
| `x64 Native Tools Command Prompt for VS` | Tik jei pasirinktas C++ `MSVC` kelias (`cl` kompiliatorius) |

Greita taisyklė:
1. Jei prie komandos parašyta `PowerShell`, vykdykite PowerShell lange.
2. Jei parašyta `MSYS2 UCRT64`, vykdykite būtent MSYS2 lange.
3. Jei parašyta `x64 Native Tools Command Prompt`, naudokite būtent tą Visual Studio terminalą.

Pastaba: VS Code integruotas terminalas Windows sistemoje dažniausiai atsidaro kaip `PowerShell`.

### Saugios komandos pasibandymui
Windows (PowerShell):
```powershell
whoami
Get-Date
pwd
ls
mkdir terminalo-testas
cd terminalo-testas
echo "Labas, terminale!"
```

macOS (Terminal):
```bash
whoami
date
pwd
ls
mkdir terminalo-testas
cd terminalo-testas
echo "Labas, terminale!"
```

Abiejose sistemose ekrano išvalymui:
```bash
clear
```

### VS Code: svarbiausi shortcut'ai
| Veiksmas | Windows/Linux | macOS |
|---|---|---|
| Command Palette | `Ctrl + Shift + P` | `Cmd + Shift + P` |
| Atidaryti failą pagal pavadinimą | `Ctrl + P` | `Cmd + P` |
| Extensions langas | `Ctrl + Shift + X` | `Cmd + Shift + X` |
| Explorer langas | `Ctrl + Shift + E` | `Cmd + Shift + E` |
| Naujas terminalas | ``Ctrl + Shift + ` `` | ``Ctrl + Shift + ` `` |
| Rodyti / slėpti terminalą | ``Ctrl + ` `` | ``Ctrl + ` `` |
| Išsaugoti failą | `Ctrl + S` | `Cmd + S` |
| Komentuoti eilutę | `Ctrl + /` | `Cmd + /` |
| Paleisti debug | `F5` | `F5` |
| Paleisti be debug | `Ctrl + F5` | `Ctrl + F5` |

Oficialūs shortcut PDF:
- Windows: <https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf>
- macOS: <https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf>

Pastaba: klavišas `` ` `` dažniausiai yra kairėje nuo skaičiaus `1` (šalia `Esc`). Ant macOS klaviatūros jis gali būti pažymėtas kaip `~` (tilde) arba `` ` `` (backtick) ir gali atsirasti prie Shift klavišo. Windows klaviatūrose jis dažniausiai yra vienas klavišas, o macOS gali būti du (tilde ir backtick). Pamokose naudosime tik backtick (`` ` ``) funkciją, kuri atidaro terminalą.


## 0 žingsnis: diegiame DEV tools

Jei kompiuteryje ankščiau nebuvo diegta jokių programavimo įrankių, rekomenduojama pradėti nuo jų įdiegimo.

### macOS: minimalus paruošimas
1. Visada rekomenduojama, bet nėra būtina: Atnaujinkite macOS (`System Settings` -> `General` -> `Software Update`).
2. Įsidiekite Apple Command Line Tools:
```bash
xcode-select --install
```
3. Patikrinkite, ar įsidiegė:
```bash
xcode-select -p
git --version
```
4. (Nebūtina, bet naudinga) įsidiekite Homebrew:
- Homebrew: <https://brew.sh/>
- Diegimo komanda:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
5. Jei reikia naujesnio Git:
```bash
brew install git
```

### Windows: minimalus paruošimas nuo nulio
1. Visada rekomenduojama, bet nėra būtina: Atnaujinkite Windows (`Settings` -> `Windows Update`).
2. Atidarykite `Windows Terminal` ir pasirinkite `PowerShell` profilį (arba atsidarykite atskirai `PowerShell`).
3. Patikrinkite `winget` (jei yra, diegti bus paprasčiau):
```powershell
winget --version
```
4. Jei reikia, įsidiekite Git:
- Oficiali nuoroda: <https://git-scm.com/install/windows>
- Arba per `winget`:
```powershell
winget install --id Git.Git -e --source winget
```
5. Jei mokysitės C++, iš karto įsidiekite `MSYS2` iš <https://www.msys2.org/>.
6. Po MSYS2 diegimo `Start` meniu atsiras `MSYS2 UCRT64` terminalas:
- jame veikia `pacman`
- jame diegsime C++ įrankius (`g++`, `gdb`)
- `PowerShell` lange `pacman` neveiks (tai normalu)
7. Jei C++ pasirinksite `MSVC` kelią, `Start` meniu ieškokite `x64 Native Tools Command Prompt for VS`.

Papildomos oficialios nuorodos startui:
- Homebrew diegimas: <https://docs.brew.sh/Installation>
- MSYS2 diegimas: <https://www.msys2.org/docs/installer/>


## 1 žingsnis: susikurkite GitHub paskyrą (rekomenduojama)

**Rekomendacija:** prieš diegiant Live Share susikurkite ir patvirtinkite GitHub paskyrą.  
Taip prisijungimas pamokos metu bus greitesnis ir sklandesnis. Taip pat turėsite prieigą prie daugybės naudingų įrankių ateityje (kodo saugyklos, bendradarbiavimas, atviro kodo projektai).

1. Atidarykite registraciją: <https://github.com/signup>
2. Užregistruokite paskyrą ir patvirtinkite el. paštą.
3. Jei reikia, vadovaukitės oficialiu gidu:  
   <https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github>

## 2 žingsnis: įsidiekite VS Code

### Windows
1. Eikite į <https://code.visualstudio.com/Download> ir atsisiųskite **Windows User Installer (x64)**.
2. Paleiskite diegimo failą.
3. Diegimo metu rekomenduojama pažymėti:
- Add to PATH
- Add "Open with Code" (File ir Directory context menu)
4. Užbaikite diegimą ir paleiskite VS Code.

Pastaba: pagal oficialią dokumentaciją dažniausiai rekomenduojamas **User setup** variantas (paprastesni atnaujinimai).

### macOS
1. Eikite į <https://code.visualstudio.com/Download> ir atsisiųskite **Mac Universal**.
2. Išarchyvuokite atsisiųstą failą.
3. Perkelkite `Visual Studio Code.app` į `Applications` aplanką.
4. Paleiskite VS Code iš `Applications`.
5. Kad veiktų komanda `code` terminale:
- Atidarykite Command Palette: `Cmd + Shift + P`
- Įveskite: `Shell Command: Install 'code' command in PATH`

## 3 žingsnis: įsidiekite Live Share ir prisijunkite

Live Share leidžia bendradarbiauti realiu laiku pamokoje.

Oficialios nuorodos:
- Live Share plėtinys: <https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare>
- Live Share diegimo dokumentacija: <https://learn.microsoft.com/en-us/visualstudio/liveshare/use/install-live-share-visual-studio-code>

### Diegimas per VS Code
1. VS Code atidarykite `Extensions` (`Ctrl+Shift+X` Windows, `Cmd+Shift+X` macOS).
2. Paieškoje įveskite **Live Share**.
3. Pasirinkite **Live Share (Microsoft)** ir spauskite **Install**.

### Prisijungimas (su GitHub rekomenduojama)
1. Atidarykite Command Palette (`Ctrl/Cmd + Shift + P`).
2. Paleiskite komandą: `Live Share: Sign In`.
3. Pasirinkite prisijungimą per **GitHub**.
4. Naršyklėje patvirtinkite prisijungimą.

### Sesijos paleidimas pamokai
1. Command Palette: `Live Share: Start Collaboration Session`.
2. Nukopijuokite sugeneruotą nuorodą.
3. Nusiųskite ją mokytojui arba mokiniams.

CLI alternatyva (jei naudojate `code` komandą):
```bash
code --install-extension MS-vsliveshare.vsliveshare
```

## 4 žingsnis: programavimo kalbos paruošimas (pasirinkite vieną)

Šiame etape mokinys renkasi tik **vieną** kelią:
- **A variantas:** Python
- **B variantas:** C++

### A variantas: Python paruošimas VS Code aplinkoje

Oficialios nuorodos:
- Python atsisiuntimas: <https://www.python.org/downloads/>
- VS Code Python tutorial: <https://code.visualstudio.com/docs/python/python-tutorial>
- Python plėtinys: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>

#### A.1 Įsidiekite Python
##### Windows
1. Atsisiųskite Python iš <https://www.python.org/downloads/>.
2. Diegimo lange būtinai pažymėkite **Add Python to PATH**.
3. Patikrinkite terminale:
```powershell
py --version
python --version
```

##### macOS
1. Atsisiųskite Python iš <https://www.python.org/downloads/>.
2. Įsidiekite pagal vedlį.
3. Patikrinkite terminale:
```bash
python3 --version
```

#### A.2 Įsidiekite Python plėtinį VS Code
1. Atidarykite `Extensions`.
2. Suraskite **Python (Microsoft)**.
3. Spauskite **Install**.

CLI alternatyva:
```bash
code --install-extension ms-python.python
```

#### A.3 Sukurkite projektą ir virtualią aplinką
1. Susikurkite projekto aplanką ir atidarykite VS Code:
```bash
mkdir hello-python
cd hello-python
code .
```

2. Sukurkite virtualią aplinką:

Windows (PowerShell):
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

3. VS Code pasirinkite teisingą interpreterį:
- `Ctrl/Cmd + Shift + P`
- `Python: Select Interpreter`
- Pasirinkite interpreterį iš `.venv`

4. Sukurkite `main.py`:
```python
print("Python veikia!")
```

5. Paleiskite:
- viršuje `Run Python File`
- arba terminale:
```bash
python main.py
```

### B variantas: C++ paruošimas VS Code aplinkoje

Oficialios nuorodos:
- C/C++ plėtinys: <https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools>
- C++ darbo aplinka VS Code: <https://code.visualstudio.com/docs/cpp/cpp-ide>
- C++ macOS (clang): <https://code.visualstudio.com/docs/cpp/config-clang-mac>
- C++ Windows (MinGW): <https://code.visualstudio.com/docs/cpp/config-mingw>
- C++ Windows (MSVC alternatyva): <https://code.visualstudio.com/docs/cpp/config-msvc>
- MSYS2 (Windows kompiliatoriui): <https://www.msys2.org/>

Windows naudotojams: rinkitės tik **vieną** C++ įrankių kelią:
- **Kelias 1 (rekomenduojamas pamokoms):** `MSYS2 + g++`
- **Kelias 2:** `MSVC + cl`

#### B.1 Įsidiekite C/C++ plėtinį
1. Atidarykite `Extensions`.
2. Suraskite **C/C++ (Microsoft)**.
3. Spauskite **Install**.

CLI alternatyva:
```bash
code --install-extension ms-vscode.cpptools
```

#### B.2 macOS: įsidiekite kompiliatorių (clang)
1. Terminale paleiskite:
```bash
xcode-select --install
```
2. Patikrinkite:
```bash
clang++ --version
```

#### B.3 Windows kelias 1: MSYS2 + g++ (rekomenduojama)
1. Įsidiekite MSYS2 iš <https://www.msys2.org/>.
2. Atidarykite **MSYS2 UCRT64** terminalą (ne PowerShell).
3. Atnaujinkite paketų bazę:
```bash
pacman -Syu
```
4. Jei prašo, uždarykite terminalą, atidarykite iš naujo ir tęskite:
```bash
pacman -Su
```
5. Įsidiekite C++ įrankius:
```bash
pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain
```
6. Į Windows `PATH` pridėkite:
```text
C:\msys64\ucrt64\bin
```
7. Patikrinkite PowerShell lange:
```powershell
g++ --version
gdb --version
```
8. Jei `pacman` komanda neveikia, reiškia atidarytas ne MSYS2 terminalas.

#### B.4 Windows kelias 2: MSVC + cl (alternatyva)
1. Įsidiekite Visual Studio Build Tools: <https://visualstudio.microsoft.com/downloads/>
2. Diegimo metu pasirinkite workload **Desktop development with C++**.
3. Atidarykite `x64 Native Tools Command Prompt for VS`.
4. Patikrinkite:
```bat
cl
```
5. VS Code derinimui rinkitės `C++ Windows: cl.exe build and debug active file`.

#### B.5 Pirmas C++ testas
1. Sukurkite `main.cpp`:
```cpp
#include <iostream>

int main() {
    std::cout << "C++ veikia!" << std::endl;
    return 0;
}
```

2. Kompiliavimas ir paleidimas:

macOS:
```bash
clang++ main.cpp -std=c++17 -Wall -Wextra -g -o main
./main
```

Windows su MSYS2 (MSYS2 UCRT64 terminale):
```bash
g++ main.cpp -std=c++17 -Wall -Wextra -g -o main.exe
./main.exe
```

Windows su MSYS2 (PowerShell, jei `C:\msys64\ucrt64\bin` pridėta į `PATH`):
```powershell
g++ main.cpp -std=c++17 -Wall -Wextra -g -o main.exe
.\main.exe
```

Windows su MSVC (x64 Native Tools Command Prompt):
```bat
cl /EHsc /std:c++17 main.cpp
main.exe
```

3. Derinimas VS Code:
- Atidarykite `main.cpp`
- Spauskite `F5`
- Pasirinkite:
- macOS: `C/C++: clang++ build and debug active file`
- Windows su MSYS2: `C/C++: g++.exe build and debug active file`
- Windows su MSVC: `C++ Windows: cl.exe build and debug active file`

## Greitas pasiruošimo patikrinimas prieš pamoką
1. VS Code atsidaro be klaidų.
2. Prisijungimas prie GitHub VS Code viduje pavyksta.
3. Live Share plėtinys įdiegtas ir galima sukurti sesijos nuorodą.
4. Jei pasirinktas Python kelias: `main.py` sėkmingai paleidžiamas.
5. Jei pasirinktas C++ kelias: `main.cpp` susikompiliuoja ir paleidžiamas (per `g++` arba `cl`).

## Dažniausios problemos ir sprendimai

### `code` komanda neveikia terminale
- macOS: paleiskite `Shell Command: Install 'code' command in PATH`.
- Windows: perkraukite terminalą arba kompiuterį po diegimo.

### `python` arba `py` neatpažįstama
- Windows: perinstaliuokite Python ir pažymėkite **Add Python to PATH**.
- macOS: naudokite `python3` komandą.

### `g++` neatpažįstama Windows sistemoje
- Jei dirbate su MSYS2 keliu, pirmiausia pabandykite `MSYS2 UCRT64` terminale.
- Jei norite naudoti PowerShell, patikrinkite, ar `C:\msys64\ucrt64\bin` tikrai pridėta į `PATH`.
- Uždarykite ir atidarykite terminalą iš naujo.

### Windows: komanda veikia viename terminale, bet neveikia kitame
- Tai dažna pradedančiųjų situacija ir dažniausiai yra normalu.
- `pacman` turi veikti tik `MSYS2 UCRT64` terminale.
- `cl` turi veikti tik `x64 Native Tools Command Prompt for VS`.
- `winget`, `py`, `python`, `git`, `code` dažniausiai naudojami `PowerShell`.

### Live Share neprisijungia
- Patikrinkite, ar VS Code esate prisijungę prie GitHub.
- Patikrinkite, ar ugniasienė / antivirusinė neblokuoja VS Code.
- Iš naujo paleiskite VS Code ir pakartokite `Live Share: Sign In`.

