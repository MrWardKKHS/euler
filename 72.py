import fractions

combos = set()
num = 6000
for n in range(1, num):
    for d in range(n+1, num+1):
        combos.add(fractions.Fraction(n,d))
# print(combos)
print(len(combos))