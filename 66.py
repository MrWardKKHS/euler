import math

def get_y(x, D):
    # print(f"error: {round(math.sqrt(x**2/D)) - math.sqrt(x**2/D)}")
    return round(math.sqrt(x**2/D))

def get_minimal_x(D):
    x = 2
    while True:
        y = get_y(x, D)
        if x**2 - D * y**2 == 1:
            # print(f"{x}**2 - {D} * {y} ** 2 == 1")
            return x
        x += 1
        if x > 10000000:
            print('bailed')
            return 0

def is_square(num):
    if math.sqrt(num) % 1 == 0:
        return True
    return False

highscore = 0

# print(get_minimal_x(61))

for D in range(2,1001):
    if is_square(D):
        continue
    score = get_minimal_x(D)
    if score > highscore:
        highscore = score
        winning_D = D
    print(D/10, '% complete')

print(winning_D, highscore)
