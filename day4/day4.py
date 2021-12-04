
with open('day4/day4.in') as f:
    data = [l for l in f.read().split('\n') if l != '']

calls = data[0].split(',')

boards = []
for i, line in enumerate(data[1:]):
    if i % 5 == 0:
        boards.append([])
    boards[-1].append(line.split())

def check_board(board):
    for row in board:
        if all(el == 'x' for el in row):
            return True  
    for col in zip(*board):
        if all(el == 'x' for el in col):
            return True
    return False

scores = []
for call in calls:
    for board in boards:
        for row in board:
            if call in row:
                row[row.index(call)] = 'x'
                break
    for i, board in enumerate(boards):
        if check_board(board):
            score = sum(map(lambda row: sum(map(int, filter(lambda e: e.isdigit(), row))), board))
            scores.append(score * int(call))
            boards.pop(i)

print('Part 1:', scores[0])
print('Part 2:', scores[-1])