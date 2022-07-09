from math import prod

with open("input") as f:
    data = [[int(c) for c in l.strip()] for l in f.readlines()]

height = len(data)
width = len(data[0])


def get_neighbors(i, j, data):
    neighbor_coords = list(
        filter(
            lambda x: x[0] >= 0 and x[0] < width and x[1] >= 0 and x[1] < height,
            [
                (i - 1, j),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j),
            ],
        ),
    )
    neighbors = [data[c[1]][c[0]] for c in neighbor_coords]
    return neighbor_coords, neighbors


risk_level = []
minima_coords = []

for j in range(height):
    for i in range(width):
        _, neighbors = get_neighbors(i, j, data)
        here = data[j][i]
        if all([n > here for n in neighbors]):
            risk_level.append(here + 1)
            minima_coords.append((i, j))

print(f"part 1: {sum(risk_level)}")

sizes = []

for m_c in minima_coords:
    size = 0
    seen_coords = set()
    search_coords = set(get_neighbors(m_c[0], m_c[1], data)[0])
    while len(search_coords) > 0:
        new_coords = set()
        for c in search_coords:
            if c in seen_coords:
                continue
            seen_coords.add(c)
            if data[c[1]][c[0]] == 9:
                continue
            size += 1
            new_coords |= set(get_neighbors(c[0], c[1], data)[0])
        search_coords = new_coords - seen_coords
    sizes.append(size)

print(f"part 2: {prod(sorted(sizes)[-3:])}")
