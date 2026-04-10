"""
ND3 — Intervalo analizė

Įvestis:
- pirmoje eilutėje a
- antroje eilutėje b

Išvestis:
- Suma: x
- Lyginiu_suma: y
- Dalijasi_3_bet_ne_5: z
- Dalijasi_2_arba_7: w




Failas: `nd3.py`

Duoti du sveikieji skaičiai `a` ir `b`. Reikia išnagrinėti visus skaičius intervale nuo `a` iki `b` imtinai.

Tavo programa turi:

- apskaičiuoti visų intervalo skaičių sumą;
- apskaičiuoti lyginių intervalo skaičių sumą;
- suskaičiuoti, kiek skaičių dalinasi iš `3`, bet nesidalina iš `5`;
- suskaičiuoti, kiek skaičių dalinasi iš `2` arba iš `7`.

### Įvestis

Pirmoje eilutėje pateikiamas sveikasis skaičius `a`.

Antroje eilutėje pateikiamas sveikasis skaičius `b`.

Galima laikyti, kad visada `a <= b`.

### Išvestis

Išvesk tiksliai tokį formatą:

```text
Suma: x
Lyginiu_suma: y
Dalijasi_3_bet_ne_5: z
Dalijasi_2_arba_7: w
```

### Pavyzdys

| stdin | stdout |
|---|---|
| `3`<br>`9` | `Suma: 42`<br>`Lyginiu_suma: 18`<br>`Dalijasi_3_bet_ne_5: 3`<br>`Dalijasi_2_arba_7: 4` |


"""

a = int(input())
b = int(input())

suma = 0
lyg_suma = 0
x = 0
z = 0

for i in range(a, b + 1):
    suma += i
    if i % 2 == 0:
        lyg_suma += i
        
    if i % 3 == 0 and i % 5 != 0:
        x += 1
    if i % 2 == 0 or i % 7 == 0:
        z += 1
    
print(f"Suma: {suma}")
print(f"Lyginiu_suma: {lyg_suma}")
print(f"Dalijasi_3_bet_ne_5: {x}")
print(f"Dalijasi_2_arba_7: {z}")