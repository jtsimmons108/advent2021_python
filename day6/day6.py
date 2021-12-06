with open('day6/day6.in') as f:
    data = [int(n) for n in f.read().split(',')]


days = [data.count(i) for i in range(8)]
original = sum(days)

while len(days) < 256:
    days.append(days[-7] + (days[-9] if len(days) >= 9 else 0))

print('Part 1:',sum(days[:80]) + original)
print('Part 2:',sum(days[:256]) + original)