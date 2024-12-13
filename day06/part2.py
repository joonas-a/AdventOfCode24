from enum import Enum

with open("input.txt") as f:
    lines = f.read().splitlines()

MAX_X = len(lines[0]) - 1
MAX_Y = len(lines) - 1


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


def turn_right(d: Direction):
    if d == Direction.UP:
        return Direction.RIGHT
    if d == Direction.RIGHT:
        return Direction.DOWN
    if d == Direction.DOWN:
        return Direction.LEFT
    if d == Direction.LEFT:
        return Direction.UP


def walk(space, x, y, opt, d: Direction):
    visited = set()
    obstacles = set()
    loop_finder = 0
    opt_x, opt_y = opt
    while x < MAX_X and x >= 0 and y < MAX_Y and y >= 0:
        if loop_finder == 4:
            return True

        new_x = x + d.value[0]
        new_y = y + d.value[1]

        if space[new_y][new_x] == "#" or new_x == opt_x and new_y == opt_y:
            d = turn_right(d)
            if (new_x, new_y) in obstacles:
                loop_finder += 1
            else:
                loop_finder = 0
            obstacles.add((new_x, new_y))
            continue

        x = new_x
        y = new_y
        visited.add((x, y))

    return False


def find_start(space):
    for y, row in enumerate(space):
        for x, cell in enumerate(row):
            if cell == "^":
                return x, y


def get_options(space):
    options = []
    for y, row in enumerate(space):
        for x, cell in enumerate(row):
            if cell == ".":
                options.append((x, y))
    return options


x, y = find_start(lines)
print(sum(1 for opt in get_options(lines) if walk(lines, x, y, opt, Direction.UP)))
