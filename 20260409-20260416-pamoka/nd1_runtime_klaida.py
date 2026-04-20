pirma_eilute = input().split()

n = int(pirma_eilute[0])
r = int(pirma_eilute[1])
p = int(pirma_eilute[2])

print("Bronzos_lyga:")

for _ in range(n):
    vardas, taskai, pergales, bonusai, baudos, rungtys, disk = input().split()

    taskai = int(taskai)
    pergales = int(pergales)
    bonusai = int(bonusai)
    baudos = int(baudos)
    disk = int(disk)

    galutiniai = taskai + pergales ** 2 + bonusai * 2 - baudos
    vidurkis = galutiniai / rungtys
    print(f"{vardas} {vidurkis:.2f}")