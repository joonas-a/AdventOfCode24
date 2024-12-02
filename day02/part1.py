with open("input.txt") as f:
    lines = f.read().splitlines()


def check_diffs(line: list[int]):
    diffs = [b - a for a, b in zip(line, line[1:])]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)


print(sum(1 for line in lines if check_diffs(list(map(int, line.split())))))
