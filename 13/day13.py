def get_map(points):
    maxx = max(p[0] for p in points)
    maxy = max(p[1] for p in points)

    data = [["." for _ in range(maxx + 1)] for _ in range(maxy + 1)]

    for p in points:
        data[p[1]][p[0]] = "#"

    return data


with open("input") as f:
    points, folds = f.read().split("\n\n")
    points = {tuple(map(int, p.split(","))) for p in points.split("\n")}
    folds = [f[(f.find("=") - 1) :].split("=") for f in folds.strip().split("\n")]
    folds = [(f[0], int(f[1])) for f in folds]

for f in folds:
    newpoints = set()
    for p in points:
        if f[0] == "x" and p[0] > f[1]:
            newpoints.add((p[0] - 2 * abs(f[1] - p[0]), p[1]))
        elif f[0] == "y" and p[1] > f[1]:
            newpoints.add((p[0], p[1] - 2 * abs(f[1] - p[1])))
        else:
            newpoints.add(p)
    points = newpoints

data = get_map(points)
dstring = "\n".join(["".join(d) for d in data])

print(dstring)
print(sum(c == "#" for c in dstring))
