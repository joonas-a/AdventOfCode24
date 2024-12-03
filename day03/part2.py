import re

with open("input.txt") as f:
    x = "".join(f.read().splitlines())


start = re.escape("don't()")
end = re.escape("do()")
strip_pattern = re.compile(f"{start}.*?(?:{end}|$)")
stripped = strip_pattern.sub("", x)

pattern = re.compile(r"mul\((\d+),(\d+)\)")

print(sum(int(match[0]) * int(match[1]) for match in pattern.findall(stripped)))
