# --- DUOMENYS (NEKEISK!) ---
vilnius_taskai = 87
kaunas_taskai = 92
klaipeda_taskai = 78
siauliai_taskai = 92
panevezys_taskai = 65

max_imanomi_taskai = 100
dalyvaujanciq_komandu_skaicius = 5
pirmos_vietos_premija = 500
antros_vietos_premija = 300
treCios_vietos_premija = 150

klaipeda_diskvalifikuota = True

komandos = ["Vilnius", "Kaunas", "Klaipėda", "Šiauliai", "Panevėžys"]
visi_taskai = [87, 92, 78, 92, 65]
diskvalifikuotos = [False, False, True, False, False]

# 1 dalis
bendra_suma = vilnius_taskai + kaunas_taskai + klaipeda_taskai + siauliai_taskai + panevezys_taskai
print(f"1.1: {bendra_suma}")

vidurkis = bendra_suma / dalyvaujanciq_komandu_skaicius
print(f"1.2: {vidurkis}")

skirtumas = kaunas_taskai - panevezys_taskai
print(f"1.3: {skirtumas}")

vilnius_kvadratas = vilnius_taskai ** 2
print(f"1.4: {vilnius_kvadratas}")

kaunas_liekana = kaunas_taskai % 10
print(f"1.5: {kaunas_liekana}")

vilnius_sveikoji = vilnius_taskai // 10
print(f"1.6: {vilnius_sveikoji}")

premijų_suma = pirmos_vietos_premija + antros_vietos_premija + treCios_vietos_premija
premijų_suma -= 50
print(f"1.7: {premijų_suma}")

kaunas_procentas = (kaunas_taskai / max_imanomi_taskai) * 100
print(f"1.8: {kaunas_procentas}")

# 2 dalis
ar_lygus = (vilnius_taskai == kaunas_taskai)
print(f"2.1: {ar_lygus}")

ar_skirtingi = (vilnius_taskai != panevezys_taskai)
print(f"2.2: {ar_skirtingi}")

vilnius_finale = (vilnius_taskai >= 80) and (not False)
print(f"2.3: {vilnius_finale}")

klaipeda_finale = (klaipeda_taskai >= 80) and (not klaipeda_diskvalifikuota)
print(f"2.4: {klaipeda_finale}")

klaipeda_ne_diskvalifikuota = not klaipeda_diskvalifikuota
print(f"2.5: {klaipeda_ne_diskvalifikuota}")

panevezys_kraštutinumas = (panevezys_taskai < 70) or (panevezys_taskai > 90)
print(f"2.6: {panevezys_kraštutinumas}")

# 3 dalis
if vilnius_taskai >= 90:
    vilnius_medalis = "Auksas"
elif vilnius_taskai >= 80:
    vilnius_medalis = "Sidabras"
elif vilnius_taskai >= 70:
    vilnius_medalis = "Bronza"
else:
    vilnius_medalis = "Be medalio"
print(f"3.1: {vilnius_medalis}")

if klaipeda_diskvalifikuota:
    klaipeda_medalis = "Diskvalifikuota"
elif klaipeda_taskai >= 90:
    klaipeda_medalis = "Auksas"
elif klaipeda_taskai >= 80:
    klaipeda_medalis = "Sidabras"
elif klaipeda_taskai >= 70:
    klaipeda_medalis = "Bronza"
else:
    klaipeda_medalis = "Be medalio"
print(f"3.2: {klaipeda_medalis}")

if kaunas_taskai >= 90:
    kaunas_medalis = "Auksas"
elif kaunas_taskai >= 80:
    kaunas_medalis = "Sidabras"
elif kaunas_taskai >= 70:
    kaunas_medalis = "Bronza"
else:
    kaunas_medalis = "Be medalio"
print(f"3.3: {kaunas_medalis}")

if panevezys_taskai >= 90:
    panevezys_medalis = "Auksas"
elif panevezys_taskai >= 80:
    panevezys_medalis = "Sidabras"
elif panevezys_taskai >= 70:
    panevezys_medalis = "Bronza"
else:
    panevezys_medalis = "Be medalio"
print(f"3.4: {panevezys_medalis}")

# 4 dalis
for i in range(len(komandos)):
    print(f"4.1: {komandos[i]} - {visi_taskai[i]} taškų")

for_suma = 0
for t in visi_taskai:
    for_suma += t
print(f"4.2: {for_suma}")

for i in range(len(komandos)):
    if diskvalifikuotos[i]:
        continue
    if visi_taskai[i] >= 80:
        print(f"4.3: {komandos[i]}")

for i in range(len(komandos)):
    if visi_taskai[i] > 90:
        print(f"4.4: {komandos[i]}")
        break

# 5 dalis
rungtynes = 0
tasku_kiekis = 0
while tasku_kiekis < 50:
    tasku_kiekis += 7
    rungtynes += 1
print(f"5.1: {rungtynes}")

skaiciuoklis = 5
while skaiciuoklis >= 1:
    print(f"5.2: {skaiciuoklis}")
    skaiciuoklis -= 1
print("5.2: Start!")
