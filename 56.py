def digit_sum(num):
    return sum([int(i) for i in str(num)])

highscore = 0
for a in range(100, 0, -1):
    for b in range(100, 0, -1):
        score = digit_sum(a**b)
        if score > highscore:
            highscore = score
            print(score)