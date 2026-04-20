# Pamokos uždaviniai: `while`, `for`, `continue`, `break`, ciklas cikle

---

## U1. Mokėjimų planas

Pirkėjas skolingas `S` eurų. Kas mėnesį jis moka po `P` eurų. Parašyk programą, kuri suskaičiuoja, po kiek mėnesių skola bus visiškai padengta.

**Įvestis:**

Dvi eilutės. Pirmoje — skola `S`, antroje — mėnesinis mokestis `P`. Abu sveikieji teigiami skaičiai, `P > 0`.

**Išvestis:**

Vienas sveikasis skaičius — mėnesių skaičius.

**Pavyzdžiai:**

| stdin | stdout |
|---|---|
| `100`<br>`30` | `4` |
| `60`<br>`20` | `3` |
| `1`<br>`100` | `1` |

---

## U2. Teigiamų filtras

Pateikiami `n` sveikųjų skaičių. Suskaičiuok tik teigiamų sumą. Nulius ir neigiamus praleisk — naudok `continue`.

**Įvestis:**

Pirmoje eilutėje — `n`. Toliau `n` eilučių, kiekvienoje vienas sveikasis skaičius.

**Išvestis:**

Dvi eilutės:

```
Suma: <suma>
Praleista: <praleistų skaičių kiekis>
```

**Pavyzdžiai:**

| stdin | stdout |
|---|---|
| `6`<br>`3`<br>`-2`<br>`5`<br>`0`<br>`4`<br>`-3` | `Suma: 12`<br>`Praleista: 3` |
| `3`<br>`-1`<br>`-5`<br>`-3` | `Suma: 0`<br>`Praleista: 3` |
| `4`<br>`10`<br>`20`<br>`30`<br>`40` | `Suma: 100`<br>`Praleista: 0` |

---

## U3. Pirmas tinkamas

Pateikiami `n` sveikųjų skaičių. Surask pirmą, kuris dalinasi iš 7. Išvesk jį. Jei tokio nėra — išvesk `Nerasta`. Kai tik randi — sustok, toliau neskaičiuok. Naudok `break`.

**Įvestis:**

Pirmoje eilutėje — `n`. Toliau `n` eilučių, kiekvienoje vienas sveikasis skaičius.

**Išvestis:**

Vienas skaičius arba žodis `Nerasta`.

**Pavyzdžiai:**

| stdin | stdout |
|---|---|
| `5`<br>`3`<br>`14`<br>`9`<br>`21`<br>`8` | `14` |
| `3`<br>`4`<br>`9`<br>`11` | `Nerasta` |
| `4`<br>`7`<br>`1`<br>`2`<br>`3` | `7` |

---

## U4. Daugybos lentelė

Pateikiami du sveikieji skaičiai `a` ir `b`. Išvesk daugybos lentelę: `a` eilučių, kiekvienoje `b` skaičių. `i`-oje eilutėje ir `j`-ame stulpelyje turi būti skaičius `i * j`. Skaičiai eilutėje atskiriami tarpais.

**Įvestis:**

Dvi eilutės — `a` ir `b`.

**Išvestis:**

`a` eilučių, kiekvienoje `b` skaičiai atskirti tarpais.

**Pavyzdžiai:**

| stdin | stdout |
|---|---|
| `3`<br>`4` | `1 2 3 4`<br>`2 4 6 8`<br>`3 6 9 12` |
| `2`<br>`2` | `1 2`<br>`2 4` |
| `1`<br>`5` | `1 2 3 4 5` |
