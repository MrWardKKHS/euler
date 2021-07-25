def is_pallendrome(word):
    if isinstance(word, int):
        word = str(word)
    return "".join(list(reversed(word))) == word

def pallendrome_sum(num):
    return num + int("".join(list(reversed(str(num)))))

def is_lychrel(num):
    count = 0
    num = pallendrome_sum(num)
    while count <= 50:
        if is_pallendrome(num):
            return False
        num = pallendrome_sum(num)
        count += 1

    return True

print(is_lychrel(196))

count = 0
for i in range(1, 10000):
    if is_lychrel(i):
        count += 1
print(count)