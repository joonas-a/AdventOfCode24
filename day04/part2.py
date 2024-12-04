with open("input.txt") as f:
    lines = f.read().splitlines()

min_x, max_x = 1, len(lines[0]) - 2
min_y, max_y = 1, len(lines) - 2

count = 0

for y, row in enumerate(lines):
    for x, char in enumerate(row):
        if x < min_x or x > max_x or y < min_y or y > max_y:
            continue
        matches = 0
        if char == "A":
            if lines[y - 1][x - 1] == "M" and lines[y + 1][x + 1] == "S":
                matches += 1
            elif lines[y + 1][x + 1] == "M" and lines[y - 1][x - 1] == "S":
                matches += 1
            if lines[y - 1][x + 1] == "M" and lines[y + 1][x - 1] == "S":
                matches += 1
            elif lines[y + 1][x - 1] == "M" and lines[y - 1][x + 1] == "S":
                matches += 1
        if matches == 2:
            count += 1

print(count)
