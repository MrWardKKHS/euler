from functools import cache
from itertools import permutations
import numpy as np

@cache
def is_cube(num):
    root = num ** (1/3)
    return root % 1 == 0 or abs(1 - (root % 1)) < 0.000001

num = 345
while True:
    perms = {int("".join(digits)) for digits in permutations(str(num**3))}
    if len(perms) == 5:
        print("solution found", num, num**3)
        break
    num += 1
    if not num % 100:
        print("working... ", num, num ** 3)