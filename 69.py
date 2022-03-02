from sympy import prime

def prime_gen():
    n = 1
    while True:
        yield prime(n)
        n += 1

total = 1
primes = prime_gen()
while total < 10**6:
    total *= next(primes)
    print(total)
