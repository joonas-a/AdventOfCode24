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


def walk(space, x, y, d: Direction):
    visited = set()
    while x < MAX_X and x >= 0 and y < MAX_Y and y >= 0:
        new_x = x + d.value[0]
        new_y = y + d.value[1]
        if space[new_y][new_x] == "#":
            d = turn_right(d)
            continue

        x = new_x
        y = new_y
        visited.add((x, y))

    return len(visited)


def find_start(space):
    for y, row in enumerate(space):
        for x, cell in enumerate(row):
            if cell == "^":
                return x, y


x, y = find_start(lines)
print(walk(lines, x, y, Direction.UP))
