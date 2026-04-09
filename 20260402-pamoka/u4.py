
x = 0 

while x < 5:
    print(x)
    x += 1


for i in range(5):
    print(i)


# Count down nuo 10 iki -1 su while loop

x = 10
while x >= -1:
    print(x)
    x -= 1

# pastebek, jog dabar x value yra -2, nes ciklas baigiasi kai x pasiekia -1,
# tai paskutinis isspausdintas x buvo lygus -1, o po ciklo x yra lygus -2
print(f"Paskutinis x: {x}")