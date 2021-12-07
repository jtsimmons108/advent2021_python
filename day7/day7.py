with open('day7/day7.in') as f:
    data = f.read().split(',')
    data = [int(n) for n in data]

print(min(map(lambda i: sum([abs(x - i) for x in data]), range(len(data)))))
print(min(map(lambda i: sum([abs(x - i)*(abs(x-i) + 1) // 2 for x in data]), range(len(data)))))