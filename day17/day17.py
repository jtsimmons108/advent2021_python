import re
with open('day17/day17.in') as f:
    data = f.read()

def get_path(dx, dy):
    visited = set()
    x, y = 0, 0
    while x < x2 and y > y1:
        x += dx
        y += dy
        visited.add((x, y))
        dx = max(dx - 1, 0)
        dy -= 1

    return visited
    

x1, x2, y1, y2 = map(int, re.findall(r'-?\d+', data))

target = set()
for x in range(x1, x2+1):
    for y in range(y1, y2+1):
        target.add((x, y))

highest = 0
count = 0
for dx in range(75):
    for dy in range(y1,300):
        path = get_path(dx, dy)
        if path & target:
            highest = max(highest, max([y for x, y in path]))
            count += 1
print(highest)
print(count)