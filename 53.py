from math import floor, factorial, ceil, log10

def over_a_million(n, r):
    return log10(factorial(n) / (factorial(r) * factorial(n-r))) >= 6

total = 0
for n in range(1, 101):
    for r in range(1, n + 1):
        if over_a_million(n, r):
            total += 1
print(total)