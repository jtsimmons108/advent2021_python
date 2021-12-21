import heapq
with open('day15/day15.in') as f:
    data = [[int(n) for n in line] for line in f.read().split('\n')]

grid = []
for row in data:
    grid.append(row)
    for _ in range(4):
        row = [r + 1 if r < 9 else 1 for r in row]
        grid[-1].extend(row)

for _ in range(4):
    for row in grid[-len(data):]:
        row = [r + 1 if r < 9 else 1 for r in row]
        grid.append(row)

R = len(grid)
C = len(grid[0])
q = [(0, 0, 0)]

risks = [[-1]*C for _ in range(R)]
risks[0][0] = 0
q = [(0, 0, 0)]
while risks[-1][-1] == -1:
    risk, r, c = heapq.heappop(q)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and risks[nr][nc] == -1:
            risks[nr][nc] = risk + grid[nr][nc]
            heapq.heappush(q, (risks[nr][nc], nr, nc))

print(risks[-1][-1])