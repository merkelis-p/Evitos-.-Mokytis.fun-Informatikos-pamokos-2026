S = int(input())
P = int(input())

menesiai = 0

while S > 0:
    S -= P
    menesiai += 1

print(menesiai)
