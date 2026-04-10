n ="""
ND1 — Dalumo lentelė

Įvestis:
- vienas sveikasis skaičius n

Išvestis:
- po vieną eilutę kiekvienam skaičiui nuo 1 iki n:
  skaicius zyme

Žymės:
- dalijasi_2_ir_3
- dalijasi_2
- dalijasi_3
- nesidalija





## ND1 — Dalumo lentelė

Failas: `nd1.py`

Tavo programa turi pereiti per visus skaičius nuo `1` iki `n` ir kiekvienam skaičiui parašyti, kaip jis dalinasi iš `2` ir `3`.

### Taisyklės

- jei skaičius dalinasi ir iš `2`, ir iš `3`, išvesk `dalijasi_2_ir_3`;
- jei dalinasi tik iš `2`, išvesk `dalijasi_2`;
- jei dalinasi tik iš `3`, išvesk `dalijasi_3`;
- kitu atveju išvesk `nesidalija`.

### Įvestis

Vienas sveikasis skaičius `n`.

### Išvestis

Po vieną eilutę kiekvienam skaičiui nuo `1` iki `n`:

```text
skaicius zyme
```

### Pavyzdys

| stdin | stdout |
|---|---|
| `6` | `1 nesidalija`<br>`2 dalijasi_2`<br>`3 dalijasi_3`<br>`4 dalijasi_2`<br>`5 nesidalija`<br>`6 dalijasi_2_ir_3` |


"""

n = int(input())

for i in range(1, n + 1):
  if i % 2 == 0 and i % 3 == 0:
    print(f"{i} dalijasi_2_ir_3")
  elif i % 2 == 0:
    print(f"{i} dalijasi_2")
  elif i % 3 == 0:
    print(f"{i} dalijasi_3")
  else:
    print(f"{i} nesidalija")
