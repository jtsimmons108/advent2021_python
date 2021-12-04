with open('day2/day2.in') as f:
    data = f.read().split('\n')
    
h1, v1 = 0, 0
h2, v2 = 0, 0
aim = 0
for line in data:
    move, amt = line.split()
    amt = int(amt)
    if move == 'down':
        v1 += amt
        aim += amt
    elif move == 'up':
         v1 -= amt
         aim -= amt
    else:
        h1 += amt
        h2 += amt
        v2 += aim * amt

print(h1 * v1)
print(h2 * v2)

