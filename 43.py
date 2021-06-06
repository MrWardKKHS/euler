from itertools import permutations

perms = [''.join(i) for i in permutations('0123456789')]

solutions = []

for num in perms:
    if all([
        int(num[1:4]) % 2 == 0,
        int(num[2:5]) % 3 == 0,
        int(num[3:6]) % 5 == 0,
        int(num[4:7]) % 7 == 0,
        int(num[5:8]) % 11 == 0,
        int(num[6:9]) % 13 == 0,
        int(num[7::]) % 17 == 0
    ]):
        solutions.append(int(num))

print(sum(solutions))
