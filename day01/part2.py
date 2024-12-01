with open("input.txt") as f:
    lines = f.read().splitlines()

k = {}
xa = []

for line in lines:
    a, b = map(int, line.split())
    xa.append(a)
    k[b] = k.get(b, 0) + 1

print(sum(a * k.get(a, 0) for a in xa))
