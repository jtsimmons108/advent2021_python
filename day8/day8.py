with open('day8/day8.in') as f:
    data = f.read().split('\n')

part1 = 0
part2 = 0

for line in data:
    in_wires, out_wires = [each.split() for each in line.split(' | ')]
    one, seven, four, *in_wires, eight = \
            [set(w) for w in sorted(in_wires, key = len)]
    
    for wire in in_wires[:3]:
        if len(wire & seven) == 3:
            three = wire
        elif len((four - one) & wire) == 2:
            five = wire
        else:
            two = wire
    
    for wire in in_wires[3:]:
        if len(wire & three) == 5:
            nine = wire
        elif len(wire & seven) == 3:
            zero  = wire
        else:
            six = wire

    wires = [zero, one, two, three, four, five, six, seven, eight, nine]
    wires = {''.join(sorted(wires[i])): str(i) for i in range(10)}
    
    num = ''
    for wire in out_wires:
        num += wires[''.join(sorted(wire))]

    part1 += sum([num.count(i) for i in '1478'])
    part2 += int(num)

print('Part 1:', part1)
print('Part 2:', part2)