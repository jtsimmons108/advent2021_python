import re
with open('day17/day17.in') as f:
    data = f.read().strip()


def get_path(dx, dy):
    visited = set([(0, 0)])
    x, y = 0, 0
    while x <= x2 and y >= y1:
        x += dx
        y += dy
        visited.add((x, y))
        dx = max(dx - 1, 0)
        dy -= 1
    return visited

x1, x2, y1, y2 = map(int, re.findall("-?\d+", data))
highest = 0

target = set()
for x in range(x1, x2 + 1):
    for y in range(y1, y2 + 1):
        target.add((x, y))
highest = 0
all_paths = []
for dx in range(x2+1):
    for dy in range(y1, 300):
        path = get_path(dx, dy)
        if path & target:
            highest = max(highest, dy*(dy+1)//2)
            all_paths.append(path)

print(highest)
print(len(all_paths))


