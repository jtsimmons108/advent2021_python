with open('day6/day6.in') as f:
    data = f.read().split(',')
    data = [int(n) for n in data]

fishes = [0] + [data.count(i) for i in range(8)]

while len(fishes) < 256 + 1:
    fishes.append(fishes[-7] + fishes[-9])


print('Part 1:', sum(fishes[:81]))
print('Part 2:', sum(fishes[:257]))