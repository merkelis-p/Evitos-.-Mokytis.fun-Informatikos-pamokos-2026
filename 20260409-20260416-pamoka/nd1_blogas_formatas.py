pirma_eilute = input().split()

n = int(pirma_eilute[0])
r = int(pirma_eilute[1])
p = int(pirma_eilute[2])

finalistu_skaicius = 0
finalistai = ""
tiksliai_ant_ribos = 0
tvarkingos_komandos = 0

pirma_virs_90 = "NERA"
rizikos_komandos = 0
bonusu_komandos = 0

radau_aktyvia = False
silpniausia_komanda = "NERA"
silpniausios_taskai = 0

print("Bronzos_lyga:")

for _ in range(n):
    vardas, taskai, pergales, bonusai, baudos, rungtys, disk = input().split()

    taskai = int(taskai)
    pergales = int(pergales)
    bonusai = int(bonusai)
    baudos = int(baudos)
    rungtys = int(rungtys)
    disk = int(disk)

    diskvalifikuota = disk == 1
    galutiniai = taskai + pergales ** 2 + bonusai * 2 - baudos
    vidurkis = galutiniai / rungtys
    desimtys = galutiniai // 10
    likutis = galutiniai % 10

    if diskvalifikuota:
        medalis = "Diskvalifikuota"
    elif galutiniai >= 100:
        medalis = "Auksas"
    elif galutiniai >= 80:
        medalis = "Sidabras"
    elif galutiniai >= 60:
        medalis = "Bronza"
    else:
        medalis = "Be_medalio"

    print(f"{vardas} {galutiniai} {vidurkis} {medalis} {desimtys} {likutis}")

    if galutiniai == r:
        tiksliai_ant_ribos += 1

    if pirma_virs_90 == "NERA" and galutiniai > 90:
        pirma_virs_90 = vardas

    if galutiniai < 50 or baudos > 20:
        rizikos_komandos += 1

    if bonusai != 0:
        bonusu_komandos += 1

    if diskvalifikuota:
        continue

    if baudos <= 10:
        tvarkingos_komandos += 1

    if galutiniai >= r:
        finalistu_skaicius += 1
        if finalistai == "":
            finalistai = vardas
        else:
            finalistai += " " + vardas

    if not radau_aktyvia:
        silpniausia_komanda = vardas
        silpniausios_taskai = galutiniai
        radau_aktyvia = True
    elif galutiniai < silpniausios_taskai:
        silpniausia_komanda = vardas
        silpniausios_taskai = galutiniai

print()
print("Finalo_komisija:")
print(f"Finalistu_skaicius: {finalistu_skaicius}")
if finalistai == "":
    print("Finalistai: NERA")
else:
    print(f"Finalistai: {finalistai}")
print(f"Tiksliai_ant_ribos: {tiksliai_ant_ribos}")
print(f"Tvarkingos_komandos: {tvarkingos_komandos}")

print()
print("Komandu_radaras:")
print(f"Pirma_virs_90: {pirma_virs_90}")
print(f"Rizikos_komandos: {rizikos_komandos}")
print(f"Bonusu_komandos: {bonusu_komandos}")

print()
print("Boss_level:")

if not radau_aktyvia:
    print("Silpniausia_komanda: NERA")
    print("Treniruociu_iki_finalo: 0")
else:
    truksta = r - silpniausios_taskai
    treniruotes = 0

    while True:
        if truksta <= 0:
            break
        truksta -= p
        treniruotes += 1

    print(f"Silpniausia_komanda: {silpniausia_komanda}")
    print(f"Treniruociu_iki_finalo: {treniruotes}")
