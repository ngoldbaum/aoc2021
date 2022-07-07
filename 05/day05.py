from collections import namedtuple, defaultdict

Point = namedtuple("Point", ["x", "y"])

with open("input") as f:
    lines = list(
        map(
            lambda x: list(
                map(lambda y: Point(*map(int, y.split(","))), x.strip().split(" -> "))
            ),
            f.readlines(),
        )
    )


data = defaultdict(lambda: 0)


def get_range(ex):
    if ex[0] < ex[1]:
        return range(ex[0], ex[1] + 1)
    else:
        return range(ex[0], ex[1] - 1, -1)


for line in lines:
    if line[0].x == line[1].x:
        yrange = get_range((line[0].y, line[1].y))
        xrange = [line[0].x] * len(yrange)
    elif line[0].y == line[1].y:
        xrange = get_range((line[0].x, line[1].x))
        yrange = [line[0].y] * len(xrange)
    else:
        xrange = get_range((line[0].x, line[1].x))
        yrange = get_range((line[0].y, line[1].y))
    points = [Point(x, y) for (x, y) in zip(xrange, yrange)]
    for p in points:
        data[p] += 1

nbad = sum(map(lambda val: 1 if val > 1 else 0, data.values()))
print(nbad)
