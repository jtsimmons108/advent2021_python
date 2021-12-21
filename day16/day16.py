from functools import reduce
with open('day16/day16.in') as f:
    data = f.read().strip()

binary = []

for char in data:
    binary.extend(f'{int(char, 16):04b}')

def pop_multiple(n, binary):
    r = ''
    for _ in range(n):
        r += binary.pop(0)
    return r

def get_value(packet):
    v, t, vals = packet
    if t == 0:
        print('calculating sum')
        ans = sum([get_value(pack) for pack in vals])
    elif t == 1:
        print('calculating prod')
        ans = reduce(lambda x, y: x * y, [get_value(pack) for pack in vals])
    elif t == 2:
        print('calculating min')
        ans = min([get_value(pack) for pack in vals])
    elif t == 3:
        print('calculating max')
        ans = max([get_value(pack) for pack in vals])
    elif t == 4:
        print('calculating value')
        ans = vals
    elif t == 5:
        print('calculating gt')
        ans = 1 if get_value(vals[0]) > get_value(vals[1]) else 0
    elif t == 6:
        print('calculating lt')
        ans = 1 if get_value(vals[0]) < get_value(vals[1]) else 0
    elif t == 7:
        print('calculating eq')
        ans = 1 if get_value(vals[0]) == get_value(vals[1]) else 0
    print(ans)
    return ans

packets = []
def process_packet(binary, subpackets = None):
    if binary.count('1') == 0: return False
    version = int(pop_multiple(3, binary), 2)
    type_ = int(pop_multiple(3, binary), 2)
    if type_ == 4:
        finished = False
        num = ''
        while not finished:
            current = pop_multiple(5, binary)
            if current[0] == '0':
                finished = True
            num += current[1:]
        num = int(num, 2)
        if subpackets != None:
            subpackets.append((version, type_, num))
    else:
        length_id = pop_multiple(1, binary)
        subs = []
        if length_id == '0':
            length = int(pop_multiple(15, binary), 2)
            current = len(binary)
            while current - len(binary) != length:
                process_packet(binary, subs)
            if subpackets == None:
                packets.append((version, type_, subs))
            else:
                subpackets.append((version, type_, subs))
        else:
            num = int(pop_multiple(11, binary), 2)
            for _ in range(num):
                process_packet(binary, subs)
            if subpackets == None:
                packets.append((version, type_, subs))
            else:
                subpackets.append((version, type_, subs))
process_packet(binary)
print(len(packets))
print(packets)
print(get_value(packets[0]))


