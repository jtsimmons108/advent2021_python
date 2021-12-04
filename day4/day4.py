
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

winning = None
first = None
for call in calls:
    for board in boards:
        for row in board:
            if call in row:
                row[row.index(call)] = 'x'
                break
    for board in boards:
        if check_board(board):
            if winning == None:
                winning = board
                first = int(call)
            if len(boards) > 1:
                del boards[boards.index(board)]
    if len(boards) == 1 and check_board(boards[0]):
        last = int(call)
        break

winning_total = sum(map(lambda row: sum([int(el) for el in row if el.isdigit()]), winning))
print('Part 1:', winning_total * first)

losing_total = sum(map(lambda row: sum([int(el) for el in row if el.isdigit()]), boards[0]))
print('Part 2:', losing_total * last)


