from math import gcd, prod

def shared_digit(numerator: int, denomenator: int) -> int:
    """0 is not valid for this problem therfore 0 returned if no solution"""
    for digit in str(numerator):
        if digit in str(denomenator):
            return int(digit)
    return 0

def delete_shared_digits(numerator, denomenator):
    shared = shared_digit(numerator, denomenator)
    if shared:
        try:
            simplified_numerator = int(str(numerator).replace(str(shared), ""))
            simplified_denomenator = int(str(denomenator).replace(str(shared), ""))
            return [simplified_numerator, simplified_denomenator]
        except ValueError:
            return None

numes = []
denoms = []
for numerator in range(10, 99):
    for denomenator in range(numerator + 1, 100):
        try:
            simplified_numerator, simplified_denomenator = delete_shared_digits(numerator, denomenator)
            if numerator/denomenator == simplified_numerator/simplified_denomenator:
                print(f"{numerator}/{denomenator} == {simplified_numerator}/{simplified_denomenator}")
                numes.append(numerator)
                denoms.append(denomenator)
        except (TypeError, ZeroDivisionError):
            pass

nume = prod(numes)
denom = prod(denoms)
d = gcd(nume, denom)
ans = denom // d
print(ans)