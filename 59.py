txt = open('resources\cypher.txt')
nums = [int(i) for i in txt.readline().split(',')]

def key_gen():
    alpha = 'abcdefghijklmnopqrstuvwxyx'
    for i in alpha:
        for j in alpha:
            for k in alpha:
                yield i + j + k

keys = key_gen()
print(str(int.from_bytes(next(keys).encode(), "big")).decode())