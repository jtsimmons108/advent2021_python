with open('day19/day19.test') as f:
    data = [line.split('\n') for line in f.read().split('\n\n')]


class Scanner(object):
    def __init__(self, coords):
        self.beacons = [tuple(map(int, line.split(','))) for line in coords]
        self.distances = {}
        for i in range(len(self.beacons)):
            for j in range(i + 1, len(self.beacons)):
                d = sum([(a-b)**2 for a, b in zip(self.beacons[i], self.beacons[j])])**0.5
                self.distances[d] = (self.beacons[i], self.beacons[j])
        self.beacons = set(self.beacons)


scanners = []
for s in data:
    scanners.append(Scanner(s[1:]))

located = set()
for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        if len(scanners[i].distances.keys() & scanners[j].distances.keys()) == 66:
            print(i, j)
            located.add(i)
            located.add(j)

print(len(located))