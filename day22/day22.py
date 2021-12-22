from collections import defaultdict
import re

with open('day22/day22.in') as f:
    lines = f.read().split('\n')

lights = defaultdict(int)

for line in lines[:20]:
    state, nums = line.split(' ')
    x1, x2, y1, y2, z1, z2 = map(int, re.findall(r'-?\d+', nums))
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                lights[(x,y,z)] = state == 'on'

on = 0
for x in range(-50, 51):
    for y in range(-50, 51):
        for z in range(-50, 51):
            on += lights[(x, y, z)]
print(on)