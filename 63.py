count = 0

for power in range(0, 25):
    for i in range(1, 11):
        if len(str(abs(i**power))) == power:
            count += 1
    print(f"{power=} {count=}")

print(count)
