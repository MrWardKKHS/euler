from functools import lru_cache

# def search(remaining_value, prev_values):
#     global count
#     global answers
#     if remaining_value == 0 and sorted(prev_values) not in answers and len(prev_values) > 1:
#         count += 1
#         answers.append(sorted(prev_values))
#         return 
#     else:
#         for i in range(1, remaining_value + 1): # indroduces an off by one error
#             new_remainder = remaining_value - i
#             new_values = prev_values[:]
#             new_values.append(i)
#             search(new_remainder, new_values)

# search(21, [])
# print(count)
# print(f"{sorted(answers, key=lambda x: x[0])=}, {len(answers)=}")

# @lru_cache
# def search_v2(n):
#     global count
#     if n == 1:
#         return 1
#     return sum([search_v2(m) for m in range(1, n)]) 

# print(search_v2(21))
    
@lru_cache
def search_v3(n):
    if n == 1:
        return [[1]]
    perms = []
    for i in range(1, n):
        for combo in search_v3(i):
            temp = combo[:]
            if n-i >= temp[-1]:
                temp.append(n-i)
                perms.append(temp)
    return perms

res = search_v3(20)
# print(res)
print(len(res))

