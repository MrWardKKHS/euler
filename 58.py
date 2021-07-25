from sympy import isprime

corners = 5
primes = 3
n = 1

def num_primes(n):
    m = 2*n
    side_length = m+1
    bottom_left = side_length **2
    return sum([isprime(bottom_left - m),
                isprime(bottom_left - 2*m),
                isprime(bottom_left - 3*m)
                ])

while primes / corners > 0.1:
    n += 1
    primes += num_primes(n)
    corners += 4
    
print(2*n + 1)