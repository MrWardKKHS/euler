from sympy import factorint

def unique_factors(num1, num2):
    if len(factorint(num1)) != 4 or len(factorint(num2)) != 4:
        return False
    for i in factorint(num1).keys():
        try:
            if factorint(num2)[i] == factorint(num1)[i]:
                return False
        except KeyError:
            pass
    return True

num = 1
while True:
    if (unique_factors(num, num+1) and
    unique_factors(num, num+2) and
    unique_factors(num, num+3) and
    unique_factors(num+1, num+2) and
    unique_factors(num+1, num+3) and
    unique_factors(num+2, num+3)):
        print(num)
        break
    num += 1
