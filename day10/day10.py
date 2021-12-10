with open('day10/day10.in') as f:
    data = f.read().split('\n')

closing = {')': '(', ']': '[', '}': '{', '>': '<'}
opening = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
closing_scores = {'(': 1, '[': 2, '{': 3, '<': 4}
score = 0
incomplete = []

for line in data:
    stack = []
    for char in line:
        if char in closing:
            if stack[-1] == closing[char]:
                stack.pop()
            else:
                score += scores[char]
                break         
        else:
            stack.append(char)
    else:
        incomplete.append(stack)
           
print(score)
final = []
for line in incomplete:
    current = 0
    for char in line[::-1]:
        current = 5 * current + closing_scores[char]
    final.append(current)

print(sorted(final)[len(final)//2])
