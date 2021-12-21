from functools import reduce
import numpy as np
max_int = np.iinfo(np.int32).max

with open('day15/day15.in') as f:
    grid1 = np.array([list(map(int, x)) for x in f.read().splitlines()])

n1 = len(grid1)
grid2 = np.tile(grid1, (5,5))
for i in range(5):
    for j in range(5):
        if i == j == 0:
            continue
        tile = grid2[i*n1:(i+1)*n1, j*n1:(j+1)*n1]
        tile += i+j
        tile %= 10
        tile[tile < i+j+1] += 1

def find_lowest_risk(grid):
    n = len(grid)
    risks = np.ones_like(grid)*max_int

    node = (0, 0) # start
    not_visited = {node}
    risks[node] = 0
    while node != (n-1, n-1): # to end
        x, y = node
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xdx, ydy = x+dx, y+dy
            if not (0 <= xdx < n and 0 <= ydy < n):
                continue
            if risks[xdx, ydy] == max_int:
                not_visited.add((xdx, ydy))
            risks[xdx, ydy] = min(risks[node]+grid[xdx, ydy], risks[xdx, ydy])
        not_visited.remove(node)
        node = reduce(lambda a,b: a if risks[a] < risks[b] else b, not_visited)

    return risks[node]

answer1 = find_lowest_risk(grid1)
answer2 = find_lowest_risk(grid2)

print(answer1, answer2)