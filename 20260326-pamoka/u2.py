# Skaiciuotuvas
# norime ivesti du sveikuosius skaicius (a, b) ir suzinoti tu dvieju skaiciu 
# suma, skirtuma, daugyba, dalyba, dalybos liekana, a^b, a/b (bet gauname tik sveikaja dali)


# + sudetis, - atimtis, * daugyba, / dalyba, % dalybos liekana, a^b -> a ** b, a // b;


a = int(input('įveskite skaičių a:'))
b = int(input('įveskite skaičių b:'))

print(f'Suma: {a + b}') # print("Suma: " + str(a + b))
print(f'Atimtis: {a - b}')
print(f'Daugyba: {a * b}')
print(f'Dalyba: {a / b}')
print(f'Liekana: {a % b}')
print(f'a pakelta b: {a ** b}')
print(f'Sveikoji dalis: {a // b}')