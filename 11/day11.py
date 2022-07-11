with open("input") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

height = len(grid)
width = len(grid[0])


def get_neighbors(i, j):
    neighbor_coords = list(
        filter(
            lambda x: x[0] >= 0 and x[0] < width and x[1] >= 0 and x[1] < height,
            [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ],
        ),
    )
    return neighbor_coords


num_timesteps = 100
num_flashes = 0


def timestep(grid):
    num_updated = 0
    num_flashes = 0
    for i in range(width):
        for j in range(height):
            grid[j][i] += 1
            num_updated += 1
    flashed_coords = set()
    while num_updated != 0:
        num_updated = 0
        for i in range(width):
            for j in range(height):
                if grid[j][i] > 9 and (i, j) not in flashed_coords:
                    num_flashes += 1
                    flashed_coords.add((i, j))
                    neighbor_coords = get_neighbors(i, j)
                    for coord in neighbor_coords:
                        grid[coord[1]][coord[0]] += 1
                        num_updated += 1
    for i in range(width):
        for j in range(height):
            if grid[j][i] > 9:
                grid[j][i] = 0
    return num_flashes


for n in range(num_timesteps):
    num_flashes += timestep(grid)

print(f"part 1: {num_flashes}")

n = num_timesteps

while num_flashes != width * height:
    num_flashes = timestep(grid)
    n += 1

print(f"part 2: {n}")
