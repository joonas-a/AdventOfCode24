with open("input.txt") as f:
    lines = f.read().splitlines()

xa, xb = zip(*[map(int, line.split()) for line in lines])

print(sum(abs(a - b) for a, b in zip(sorted(xa), sorted(xb))))
