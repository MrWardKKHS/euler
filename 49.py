import sympy

primes = list(sympy.primerange(1000, 9999))
prime_tripples = [] 

def perm(num1, num2):
    return all([k in str(num2) for k in str(num1)]) and all([k in str(num1) for k in str(num2)])

for i in range(len(primes)-2):
    for j in range(i+1, len(primes)-1):
        k = primes[j] + (primes[j]-primes[i])
        if k in primes and perm(primes[i], primes[j]):
                if perm(primes[i], k):
                    print(primes[i], primes[j], k)
print(prime_tripples)