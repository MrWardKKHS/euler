from sympy import prime, primerange, isprime

#### The below code is much slower than expected
#### too slow to even bother speeding it up 100x would still be too slow
#### finding an alternate algorithm instead

# primes = primerange(1, 1000000)

# def get_consecutive_primes(target):
#     for i in range(1, target):
#         if prime(i) > target/2:
#             return []
#         step = 1
#         total = [prime(i), prime(i + step)]
#         while sum(total) <= target:
#             if sum(total) == target:
#                 return total
#             step += 1
#             total.append(prime(i+step))
#     return []

# highscore = 0
# for i in primes:
#     if score := len(get_consecutive_primes(i)) > highscore:
#         highscore = score
#         winner = i
#         print(winner, get_consecutive_primes(winner))
# print(winner)
# print(get_consecutive_primes(winner))

primes = primerange(1, 1000000)
highscore = 0
for start in range(1, 1000):
    i = start
    total = 0
    while total < 1000000:
        total += prime(i)
        if isprime(total):
            if i - start > highscore:
                highscore = i - start
                print(f"sum range {prime(start)} to {prime(i)} is", total, "highscore", highscore)
        i += 1