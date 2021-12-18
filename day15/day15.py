
with open('day15/day15.in') as f:
    grid = [list(map(int, line)) for line in f.read().split('\n')]

costs = []

for row in grid: 
    costs.append(row)
    for _ in range(4):
        row = [r + 1 if r < 9 else 1 for r in row]
        costs[-1].extend(row)

for _ in range(4):
    for row in costs[-len(grid):]:
        row = [r + 1 if r < 9 else 1 for r in row]
        costs.append(row)


R = len(costs)
C = len(costs[0])
print(R, C)
costs[0][0] = 0
for r in range(R):
    for c in range(C):
        prev = 0
        if r >= 1:
            prev = costs[r-1][c]
        if c >= 1:
            val = costs[r][c-1]
            prev = val if prev == 0 else min(prev, val)

        costs[r][c] += prev



