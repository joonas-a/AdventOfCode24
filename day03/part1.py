import re

with open("input.txt") as f:
    x = "".join(f.read().splitlines())


pattern = re.compile(r"mul\((\d+),(\d+)\)")

print(sum(int(match[0]) * int(match[1]) for match in pattern.findall(x)))
