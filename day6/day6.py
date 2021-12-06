with open('day6/day6.in') as f:
    data = [int(n) for n in f.read().split(',')]

added = [data.count(i) for i in range(8)]
original = sum(added)

while len(added) < 256:
    added.append(added[-7] + (added[-9] if len(added) >= 9 else 0))

print('Part 1:',sum(added[:80]) + original)
print('Part 2:',sum(added[:256]) + original)