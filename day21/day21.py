from itertools import cycle
with open('day21/day21.test') as f:
    one, two = map(int, [line.split()[-1] for line in f.read().split('\n')])