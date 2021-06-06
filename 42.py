triangular_nums = [(n*(n+1))/2 for n in range(1, 364)]

def get_value(word):
    total = 0
    for letter in word:
        total += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(letter) + 1
    return total 

def is_triangular(num):
    return num in triangular_nums

file = open('resources/words.txt')
words = file.readline().split(',')
words = [word.strip('"') for word in words]

tri_words = [word for word in words if is_triangular(get_value(word))]

print(len(tri_words))