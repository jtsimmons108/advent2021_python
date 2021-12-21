from collections import defaultdict

with open('day20/day20.in') as f:
    enhance, image = f.read().split('\n\n')

enhance = [1 if c == '#' else 0 for c in enhance]
image = image.split()



pixels = {}
for r in range(len(image)):
    for c in range(len(image[0])):
        pixels[(r, c)] = 1 if image[r][c] == '#' else 0

for it in range(50):
    new_pixels = {}
    for r in range(-1 * (it + 1), len(image) + 1 * (it + 1)):
        for c in range(-1 * (it + 1), len(image[0]) + 1 * (it + 1)):
            binary = ''
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    binary += str(pixels.get((r + dr, c + dc), it % 2))
            new_pixels[(r, c)] = enhance[int(binary, 2)]
    pixels = new_pixels
    if it == 1:
        print(sum(pixels.values()))

print(sum(pixels.values()))