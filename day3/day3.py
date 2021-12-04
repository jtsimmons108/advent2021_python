with open('day3/day3.in') as f:
    data = f.read().split('\n')

gamma, epsilon = '', ''
for col in zip(*data):
    gamma += max(col, key=col.count)
    epsilon += min(col, key=col.count)
print('Part 1:', int(gamma, 2) * int(epsilon, 2))

first = data[:]
second = data[:]

index = 0
while len(first) > 1:
    els = list(zip(*first))[index]
    ones = els.count('1')
    zeros = els.count('0')
    common = '0' if zeros > ones else '1'
    first = [el for el in first if el[index] == common]
    index += 1

index = 0
while len(second) > 1:
    els = list(zip(*second))[index]
    ones = els.count('1')
    zeros = els.count('0')
    common = '0' if zeros <= ones else '1'
    second = [el for el in second if el[index] == common]
    index += 1

print('Part 2:', int(first[0],2) * int(second[0],2))
