from collections import defaultdict
with open('day12/day12.in') as f:
    data = f.read().split('\n')

def walk_grid(node, path):
    for n in grid[node]:
        if n == 'end':
            finished.add(path + ('end', ))
        elif n.isupper() or (n not in ('start', 'end') and path.count(n) < 2):
            new_path = path + (n, )
            lowers = [c for c in set(new_path) if c.islower() and new_path.count(c) == 2]
            if len(lowers) <= 1:
                walk_grid(n, new_path)

grid = defaultdict(list)
finished = set()
for line in data:
    a, b = line.split('-')
    grid[a].append(b)
    grid[b].append(a)

walk_grid('start', ('start',))
print(len(finished))