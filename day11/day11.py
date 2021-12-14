with open('day11/day11.in') as f:
    data = f.read().split('\n')

points = {}
for r in range(len(data)):
    for c in range(len(data[0])):
        points[(r, c)]= int(data[r][c])
def view_grid():
    for r in range(len(data)):
        for c in range(len(data[0])):
            print(points[(r, c)], end='')
        print()
def flash(point, flashed):
    flashed.add(point)
    r, c = point
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr != 0 or dc != 0:
                n = (r + dr, c + dc)
                if n in points:
                    points[n] += 1
                    if n not in flashed and \
                        points[n] > 9:
                        flash(n, flashed)

total = 0
finished = False
count = 0
while not finished:
    for point in points:
        points[point] += 1
    
    flashed = set()
    for point in points:
        if points[point] > 9 and point not in flashed:
            flash(point, flashed)
    for point in flashed:
        points[point] = 0
    total += len(flashed)
    if len(flashed) == len(data) * len(data[0]):
        finished = True
    count += 1
print(total)
print(count)