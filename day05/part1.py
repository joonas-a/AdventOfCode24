with open("input.txt") as f:
    r, instructions = map(lambda x: x.splitlines(), tuple(f.read().split("\n\n")))
    rules = {}
    for row in r:
        k, v = map(int, row.split("|"))
        if k not in rules:
            rules[k] = set()
        rules[k].add(v)


def row_checker(row):
    seen = set()
    for x in row:
        if x in rules and len(rules[x].intersection(seen)) > 0:
            return 0
        seen.add(x)

    return row[len(row) // 2]


print(sum(row_checker(list(map(int, row.split(",")))) for row in instructions))
