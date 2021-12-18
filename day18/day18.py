import json
from math import floor, ceil

def explode_left(left, num):
    i = len(left) - 1
    reg = True
    while i >= 0:
        if left[i].isdigit():
            begin = left.rindex('[', 0, i)
            alt = left.rfind(',',0, i)
            if alt > begin:
                begin = alt
            n = int(left[begin+1:i+1])
            n += num
            return left[:begin+1] + str(n) + left[i+1:]
        i -= 1
    return left

def explode_right(right, num):
    i = 0
    while i < len(right):
        if right[i].isdigit():
            end = right.index(']', i)
            comma = right.find(',', i)
            if comma != -1 and comma < end:
                end = comma
            n = int(right[i:end])
            n += num
            return right[:i] + str(n) + right[end:]
        i += 1
    return right
            

def reduce(num):
    i = 0
    depth = 0
    while i < len(num):
        if num[i] == '[':
            if depth >= 4:
                end = num.index(']', i)
                pair = num[i:end+1]
                if '[' not in pair[1:]:
                    ln, rn = map(int, pair[1:-1].split(','))
                    left = explode_left(num[:i], ln)
                    right = explode_right(num[end + 1:], rn)
                    return reduce(left + '0' + right)
            else:
                depth += 1
        elif num[i] == ']':
            depth -= 1
        i += 1
    i = 0
    while i < len(num):
        if num[i].isdigit():
            end = i + 1
            while num[end].isdigit():
                end += 1
            n = int(num[i:end])
            if  n >= 10:
                return reduce(num[:i] + f'[{floor(n/2)},{ceil(n/2)}]' + num[end:])
        i += 1
    return num

def get_magnitude(num):
    l, r = num[0], num[1]
    if type(l) == list:
        l = get_magnitude(l)
    if type(r) == list:
        r = get_magnitude(r)
    return 3 * l + 2 * r

def add(left, right):
    return reduce(f'[{left},{right}]')


with open('day18/day18.in') as f:
    data = f.read().split('\n')

nums = data[:]
val = data.pop(0)

while len(data):
    val = add(val, data.pop(0))

val = json.loads(val)
print(get_magnitude(val))

max_ = 0
for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums):
        if i != j:
            val = add(num1, num2)
            max_ = max(max_, get_magnitude(json.loads(val)))

print(max_)
