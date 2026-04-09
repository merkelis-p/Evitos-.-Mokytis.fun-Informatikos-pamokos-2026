# Vidurkio skaiciavimo programa

# Ivedami skaiciai n ir m, patikriname ar n < m, jei ne, isvedame klaidos pranesima ir programa baigia darba
# Jei n < m, tada programa skaiciuoja vidurki nuo n iki m ir isveda rezultata (kiekviena reiksme nuo n iki m yra didejanti po 1)
# Programa turi buti implementuota naudojant for cikla ir if-else salygas
n = int(input('Įveskite skaičių n: '))
m = int(input('Įveskite skaičių m: '))
if n < m:
    sum = 0
    kiek = 0 # kiek skaiciu yra nuo n iki m, kad galetume apskaiciuoti vidurki
    i = 0 # jei i deklaruojame uz ciklo, tai galime ja isvesti po ciklo, kad pamatytume paskutine reiksme, kuri buvo priskirta i
    for i in range(n, m + 1):
        sum += i
        kiek += 1
    print(f"Suma: {sum}")

    print(f"Paskutinis i: {i}") # matome jog kiek sutaps su i, nes ciklas baigiasi kai i pasiekia m + 1 bet nepaliecia, tai paskutinis i yra lygus m
    print(f"Kiekis: {kiek}") # todel galime naudoti i arba kiek, nes jie abu yra lygus m - n + 1, nes skaiciuojame nuo n iki m, tai yra m - n + 1 skaiciu
    avg = sum / kiek
    print(f"Vidurkis nuo {n} iki {m} yra: {avg:.2f}") # :.2f - suapvalina rezultata iki 2 skaiciu po kablelio
    avg = sum / (m - n + 1) # taip pat galime apskaiciuoti kiek skaiciu yra nuo n iki m, tai yra m - n + 1, nes skaiciuojame nuo n iki m, tai yra m - n + 1 skaiciu
    print(f"Vidurkis skaičiuojant kaip suma / (m - n + 1) yra: {avg:.2f}") # :.2f - suapvalina rezultata iki 2 skaiciu po kablelio
    avg = sum / i
    print(f"Vidurkis skaičiuojant kaip suma / i yra: {avg:.2f}") 
    # apskritai tokia seka galime apskaciuoti kaip aritmetines progresijos suma, tai yra (n + m) * kiek / 2, 
    # nes skaiciuojame nuo n iki m, tai yra m - n + 1 skaiciu, tai yra (n + m) * (m - n + 1) / 2,
    # tai yra (n + m) * kiek / 2
    avg = (n + m) / 2 # taip pat galime apskaiciuoti vidurki kaip aritmetines progresijos vidurki, tai yra (n + m) / 2, nes skaiciuojame nuo n iki m, tai yra m - n + 1 skaiciu, tai yra (n + m) / 2
    print(f"Vidurkis skaičiuojant kaip aritmetines progresijos vidurkis nuo {n} iki {m} yra: {avg:.2f}") # :.2f - suapvalina rezultata iki 2 skaiciu po kablelio
else:
    print('Klaida: n turi būti mažesnis už m')