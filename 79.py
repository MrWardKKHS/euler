file = open('resources/p079_keylog.txt')
nums_after = {}
for i in '01236789':
    nums_after[i] = []
for line in file.readlines():
    line = line.strip()
    for i in range(2):
        for j in range(i, 3):
            if line[j] not in nums_after[line[i]] and line[i] != line[j]:
                nums_after[line[i]].append(line[j])

print(nums_after)
73162890
