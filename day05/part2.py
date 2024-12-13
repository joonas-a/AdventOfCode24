from functools import cmp_to_key


with open("input.txt") as f:
    r, instructions = map(lambda x: x.splitlines(), tuple(f.read().split("\n\n")))
    rules = {}
    for row in r:
        k, v = map(int, row.split("|"))
        if k not in rules:
            rules[k] = set()
        rules[k].add(v)


def rule_cmp(a, b):
    if a in rules:
        if b in rules.get(a):
            return -1
    if b in rules:
        if a in rules.get(b):
            return 1
    return 0


def row_checker(row, include=False):
    seen = set()
    for x in row:
        if x in rules and len(rules[x].intersection(seen)) > 0:
            return row_checker(sorted(row, key=cmp_to_key(rule_cmp)), True)
        seen.add(x)

    return 0 if not include else row[len(row) // 2]


res = sum(row_checker(list(map(int, row.split(",")))) for row in instructions)
print(res)
