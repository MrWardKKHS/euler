from math import sqrt

def triangulars():
    n = 286
    while True:
        yield int((n*(n+1))/2)
        n += 1

def is_pentagonal(num):
    return (-((-1/2) - sqrt(1/4-(6*-num)))/3)%1 == 0

def is_hexagonal(num):
    return ((1 + sqrt(1+8*num))/4) % 1 == 0

def both(num):
    return is_pentagonal(num) and is_hexagonal(num)

t = triangulars()
while True:
    num = next(t)
    if both(num):
        print(num)
        break