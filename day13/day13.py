with open('day13/day13.in') as f:
    points, folds = [groups.split('\n') for groups in f.read().split('\n\n')]

marks = set()
for point in points:
    x, y = map(int, point.split(','))
    marks.add((x, y))    

for i, fold in enumerate(folds):
    axis, val = fold.split()[-1].split('=')
    val = int(val)
    new_marks = set()
    for mark in marks:
        x, y = mark
        if axis == 'x' and x > val:
            x = val - (x - val)
        elif axis == 'y' and y > val:
            y = val - (y - val)
        new_marks.add((x, y))
    if i == 0:
        print(len(new_marks))
    marks = new_marks

rows = max(y for x, y in marks)
cols = max(x for x, y in marks)
for y in range(rows + 1):
    for x in range(cols + 1):
        if (x, y) in marks:
            print('#', end = '')
        else:
            print(' ', end = '')
    print()
    


