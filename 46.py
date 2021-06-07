import sympy
from math import ceil, sqrt

def is_goldbach(num):
    for i in sympy.primerange(1, num):
        for j in range(1, ceil(sqrt(num))):
            if i + 2*j*j == num:
                return True
    return False

num = 1
while True:
    if not sympy.isprime(num) and not is_goldbach(num):
        print(num)
    num += 2

