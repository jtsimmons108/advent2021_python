from collections import defaultdict
with open('day5/day5.in') as f:
    data = f.read().split('\n')


total = 0
p1_points = defaultdict(int)
points = defaultdict(int)
for line in data:
    first, second = line.split(' -> ')
    x1, y1 = map(int, first.split(','))
    x2, y2 = map(int, second.split(','))
    
    if x1 == x2 or y1 == y2:
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                points[(x, y)] += 1
                p1_points[(x, y)] += 1
    else:
        x, y = x1, y1
        while x != x2:
            points[(x, y)] += 1
            x += 1 if x1 < x2 else -1
            y += 1 if y1 < y2 else -1
        points[(x2, y2)] += 1


print(sum(n > 1 for n in p1_points.values()))
print(sum(n > 1 for n in points.values()))