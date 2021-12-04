with open('day1/day1.in') as f:
    data = [int(n) for n in f.read().split('\n')]

print('Part 1:', sum(a < b for a, b in zip(data[:-1], data[1:])))

sums = [sum(data[i:i+3]) for i in range(len(data) - 2)]
print('Part 2:', sum(a < b for a, b in zip(sums[:-1], sums[1:])))