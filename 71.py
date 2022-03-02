from fractions import Fraction

upper_bound = Fraction('3/7')
lower_bound = Fraction('2/5')

for denomenator in range(1, 1000001):
    for numerator in range(lower_bound.numerator, 1000001):
        current = Fraction(f'{numerator}/{denomenator}')
        if current < lower_bound:
            continue
        if current >= upper_bound:
            break
        lower_bound = current
    print(f'{lower_bound=}')

print(lower_bound)