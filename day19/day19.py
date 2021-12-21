from collections import defaultdict
from itertools import permutations
from math import pi, sin, cos
with open('day19/day19.test') as f:
    data = [line.split('\n') for line in f.read().split('\n\n')]


class Scanner(object):

    def __init__(self, coords):
        self.beacons = [tuple(map(int, line.split(','))) for line in coords]
        self.pairs = {}
        self.distances = defaultdict(list)
        for i in range(len(self.beacons)):
            for j in range(i + 1, len(self.beacons)):
                first = self.beacons[i]
                second = self.beacons[j]
                d = sum([(a-b)**2 for a, b in zip(first, second)])**.5
                self.pairs[d] = (first, second)
                self.distances[first].append(d)
                self.distances[second].append(d)
        self.beacons = set(self.beacons)
        self.orientations = defaultdict(list)
        self.build_orientations()
        for point in self.distances:
            self.distances[point] = sorted(self.distances[point])

        
    def build_orientations(self):
        for point in self.beacons:
            self.orientations[point].extend(permutations(point))
            for angle in (pi / 2, pi, 3* pi / 2):
                for i in range(6):
                    x, y, z = self.orientations[point][i]
                    print(x, y, z)
                    n = (int(round(x*cos(angle) + y * sin(angle), 0)), int(round(-x * sin(angle) + y * cos(angle), 0)), z)
                    self.orientations[point].append(n)

scanners = []
for group in data:
    scanners.append(Scanner(group[1:]))

connected = defaultdict(list)
for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        if len(scanners[i].pairs.keys() & scanners[j].pairs.keys()) == 66:
            connected[i].append(j)

first = set()
second = set()
for d in (scanners[0].pairs.keys() & scanners[1].pairs.keys()):
    first.update(scanners[0].pairs[d])
    second.update(scanners[1].pairs[d])

print(first)
print(second)
pairs = []
for point1 in first:
    for point2 in second:
        if len(set(scanners[0].distances[point1]) & set(scanners[1].distances[point2])) == 11:
            pairs.append((point1, point2))

for o in range(24):
    offs = set()
    for p1, p2 in pairs:
        curr = scanners[1].orientations[p2][o]
        x1, y1, z1 = p1
        x2, y2, z2 = curr
        print(x2 - x1, y2 - y1, z2 - z1)          
