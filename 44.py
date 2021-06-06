from functools import cache
from math import sqrt, floor
@cache
def pentagonal(n):
    return int(n * (3 * n - 1) / 2)

@cache
def is_pentagonal(num):
    return (-((-1/2) - sqrt(1/4-(6*-num)))/3)%1 == 0

def sum_and_difference_pentagonal(i,j):
    return is_pentagonal(pentagonal(i) + pentagonal(j)) and is_pentagonal(pentagonal(j) - pentagonal(i))

def solve():
    for j in range(4000):
        for i in range(1, j):
            if sum_and_difference_pentagonal(i, j):
                print(pentagonal(j) -pentagonal(i))
                return 

solve()