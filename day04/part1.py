with open("input.txt") as f:
    lines = f.read().splitlines()


max_x = len(lines[0]) - 1
max_y = len(lines) - 1


def horizontal(line: str, x):
    return line[x : x + 4] == "XMAS"


def horizontal_reverse(line: str, x):
    return line[x : x + 4] == "SAMX"


def vertical(lines, x, y):
    if y + 3 > max_y:
        return False
    return "".join([lines[y + i][x] for i in range(4)]) == "XMAS"


def vertical_reverse(lines, x, y):
    if y - 3 < 0:
        return False
    return "".join([lines[y - i][x] for i in range(4)]) == "XMAS"


def diagonal_SE(lines, x, y):
    if x + 3 > max_x or y + 3 > max_y:
        return False
    return "".join([lines[y + i][x + i] for i in range(4)]) == "XMAS"


def diagonal_SW(lines, x, y):
    if x - 3 < 0 or y + 3 > max_y:
        return False
    return "".join([lines[y + i][x - i] for i in range(4)]) == "XMAS"


def diagonal_NE(lines, x, y):
    if x + 3 > max_x or y - 3 < 0:
        return False
    return "".join([lines[y - i][x + i] for i in range(4)]) == "XMAS"


def diagonal_NW(lines, x, y):
    if x - 3 < 0 or y - 3 < 0:
        return False
    return "".join([lines[y - i][x - i] for i in range(4)]) == "XMAS"


count = 0
for y, row in enumerate(lines):
    for x, char in enumerate(row):
        if horizontal(row, x):
            count += 1
        if horizontal_reverse(row, x):
            count += 1
        if vertical(lines, x, y):
            count += 1
        if vertical_reverse(lines, x, y):
            count += 1
        if diagonal_SE(lines, x, y):
            count += 1
        if diagonal_SW(lines, x, y):
            count += 1
        if diagonal_NE(lines, x, y):
            count += 1
        if diagonal_NW(lines, x, y):
            count += 1

print(count)
