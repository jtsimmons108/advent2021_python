with open('day6/day6.in') as f:
    data = f.read().split(',')
    data = [int(n) for n in data]

for target in [80, 256]:
    counts = {i: data.count(i) for i in range(9)}
    for _ in range(target):
        next_ = {i: 0 for i in range(9)}
        for day, count in counts.items():
            if day == 0:
                next_[8] = count
                next_[6] += count
            else:
                next_[day - 1] += count
        counts = next_

    print('Day', target, ':', sum(counts.values()))