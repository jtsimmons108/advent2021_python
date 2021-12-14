
from functools import reduce
with open('day9/day9.in') as f:
    data = [list(map(int, l)) for l in f.read().split('\n')]

def is_in_grid(r, c):
    return 0 <= r < rows and 0 <= c < cols

def find_basin(r, c, vals):
    if data[r][c] != 9:
        vals[(r, c)] = data[r][c]
        for dr, dc in deltas:
            if is_in_grid(r+dr, c+dc) and (r+dr, c+dc) not in vals:
                find_basin(r+dr, c+dc, vals)

rows, cols = len(data), len(data[0])
deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
total = 0
basins = []

for r in range(rows):
    for c in range(cols):
        low = True
        for dr, dc in deltas:
            if is_in_grid(r + dr, c + dc) and data[r+dr][c+dc] <= data[r][c]:
                low = False
        if low:
            total += data[r][c] + 1
            basin = {}
            find_basin(r, c, basin)
            basins.append(len(basin.values()))
            
basins = sorted(basins, reverse=True)

print(total)
print(reduce(lambda x, y: x * y, basins[:3]))



