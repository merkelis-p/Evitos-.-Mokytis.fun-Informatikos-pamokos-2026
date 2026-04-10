"""
ND2 — Kvadratų statistika

Įvestis:
- pirmoje eilutėje n
- toliau n eilučių su sveikaisiais skaičiais

Išvestis:
- Suma: x
- Kvadratu_suma: y
- Dalinasi_is_3: z
- Vidurkis: w




Duota `n` sveikųjų skaičių. Tavo programa turi:

- apskaičiuoti visų skaičių sumą;
- apskaičiuoti jų kvadratų sumą;
- suskaičiuoti, kiek skaičių dalinasi iš `3`;
- apskaičiuoti skaičių vidurkį.

### Įvestis

Pirmoje eilutėje pateikiamas sveikasis skaičius `n`.

Toliau pateikiamos `n` eilutės. Kiekvienoje eilutėje yra vienas sveikasis skaičius.

### Išvestis

Išvesk tiksliai tokį formatą:

```text
Suma: x
Kvadratu_suma: y
Dalinasi_is_3: z
Vidurkis: w
```

Vidurkį išvesk dviem skaitmenimis po kablelio.

### Pavyzdys

| stdin | stdout |
|---|---|
| `4`<br>`2`<br>`-3`<br>`5`<br>`6` | `Suma: 10`<br>`Kvadratu_suma: 74`<br>`Dalinasi_is_3: 2`<br>`Vidurkis: 2.50` |



"""

n = int(input())
x = 0 # suma
y = 0 # kvadratu suma
z = 0 # dalijasi is 3 kiekis
w = 0 # vidurkis
for _ in range(n):
    tmp = int(input())
    x += tmp
    y += tmp * tmp
    if tmp % 3 == 0:
        z += 1

w = x / n

print(f"Suma: {x}")
print(f"Kvadratu_suma: {y}")
print(f"Dalinasi_is_3: {z}")
print(f"Vidurkis: {w:.2f}")


