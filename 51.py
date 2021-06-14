from sympy import prime
from sympy.ntheory.generate import primerange
from itertools import combinations
# Below code is slow and intractable once numberis hit 8 digits
# def has_two_same_digits(num):
#     for i in range(len(str(prime)) - 1):
#         for j in range(i+1, len(str(prime))):
#             if str(prime)[i] == str(prime)[j]:
#                 return True
#     return False  

# def get_digit_count(prime):
#     digit_count = {}
#     for digit in str(prime):
#         digit_count[digit] = str(prime).count(digit)
#     return digit_count

# def get_master_dict(arr):
#     doubles_dict = {}
#     for i in '0123456789':
#         doubles_dict[i] = []
#     for num in arr:
#         digits = get_digit_count(num)
#         for i in digits.keys():
#             if digits[i] >= 2:
#                 doubles_dict[i].append(num)
#     return doubles_dict

# def find(s, ch):
#     return [i for i, ltr in enumerate(s) if ltr == ch]

# def is_solution(num):
#     num_digit_count = get_digit_count(num)
#     for i in num_digit_count.keys():
#         if num_digit_count[i] >= 2:
#             location_pairs = list(combinations(find(str(num), i), 2))
#             for locations in location_pairs:
#                 solutions = 0
#                 wrong = 0
#                 for digit in '0123456789':
#                     check_num = str(num)
#                     for j in list(locations):
#                         check_num = check_num[0:j] + digit + check_num[j+1:]
#                     if int(check_num) in master_dict[digit]:
#                         solutions += 1
#                     else:
#                         wrong += 1
#                         if wrong >= 3:
#                             break
#                 if solutions >= 8:
#                     return True
#     return False

# primes = primerange(10000000, 100000000)
# possible_starting_primes = []

# for prime in primes:
#     if has_two_same_digits(prime):
#         possible_starting_primes.append(prime)

# master_dict = get_master_dict(possible_starting_primes)
# count = 0 
# for num in possible_starting_primes:
#     if is_solution(num):
#         print(num)
#         break
#     count+=1
#     if not count % 100:
#         print('not under', num)

#### New plan ############
# Go through the prime list
# identify which primes have double digits
# make a key with *s to store in a honking dictionary i.e. 56**3
# go through the dictionary to see which key has a list of 8 or more values
# this should be close to O(n)

###### attempt 2 #########

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def has_two_same_digits(num):
    prime = str(num)
    for i in range(len(prime) - 1):
        for j in range(i+1, len(prime)):
            if prime[i] == prime[j]:
                return True
    return False

def get_digit_count(prime):
    digit_count = {}
    for digit in str(prime):
        digit_count[digit] = str(prime).count(digit)
    return digit_count



def solve():
    primes = primerange(100000000, 1000000000)
    starred_primes = {}
    count = 0
    for prime in primes:
        num_digit_count = get_digit_count(prime)
        for key in num_digit_count.keys():
            if num_digit_count[key] >= 2:
                location_pairs = list(combinations(find(str(prime), key), 2))
                for loc0, loc1 in location_pairs:
                    annoying_list = list(str(prime))
                    annoying_list[loc0] = '*'
                    annoying_list[loc1] = '*'
                    starred_prime = "".join(annoying_list)
                    try:
                        starred_primes[starred_prime].append(prime)
                        if len(starred_primes[starred_prime]) >= 8:
                            return starred_primes[starred_prime]
                    except KeyError:
                        starred_primes[starred_prime] = [prime]
        count += 1
        if not count % 10000:
            print(prime, "processed")

print(solve())
