from collections import defaultdict
with open('day14/day14.in') as f:
    start, _, *data = f.read().split('\n')

pairs = {}
for line in data:
    a, b = line.split(' -> ')
    pairs[a] = b

group = [''.join(p) for p in zip(start[:-1], start[1:])]
end = start[-1]

for times in [10, 40]:
    counts = defaultdict(int)
    for g in group:
        counts[g] += 1
    for _ in range(times):
        new_counts = defaultdict(int)
        for g, count in counts.items():
            mid = pairs[g]
            new_counts[g[0] + mid] += count
            new_counts[mid + g[1]] += count
        counts = new_counts
    
    totals = defaultdict(int)
    for g, count in counts.items():
        totals[g[0]] += count
    totals[end] += 1
    print(max(totals.values()) - min(totals.values()))