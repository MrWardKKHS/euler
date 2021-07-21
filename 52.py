# first digit must be one
# must be a multiple of 3
# does it need to be even? 

def same_digits(x, y):
    sx = str(x)
    sy = str(y)
    return all([digit in sy for digit in sx]) and all([digit in sx for digit in sy])

def solve(magnitude):
    for i in range(10**magnitude+2, 10**(magnitude+1), 3):
        if not str(i)[0] == '1':
            break
        if all([same_digits(i, i*j) for j in range(2, 7)]):
            print("solution",i)
            break
        if not i % 1000000:
            print("done up to", i)

for i in range(9):
    solve(i)