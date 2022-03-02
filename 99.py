import math
line = 0
with open('resources/p099_base_exp.txt') as file:

    data = file.readlines()
    highest = 0
    nums = ()
    for datum in data:
        line += 1
        base, exp = [int(i) for i in datum.split(',')]
        ans = math.log(base) * exp
        if ans > highest:
            highest = ans
            nums = (base, exp, line)
    print(f'{highest=} {nums=}')
