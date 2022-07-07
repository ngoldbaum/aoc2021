with open("input") as f:
    fishes = list(map(int, f.read().split(",")))

num_fish = len(fishes)

fish_counts = [fishes.count(i) for i in range(9)]


def timestep(fish_counts):
    ret = [0] * 9
    for i in range(8, 0, -1):
        ret[i - 1] = fish_counts[i]
    ret[6] += fish_counts[0]
    ret[8] += fish_counts[0]
    return ret


for i in range(256):
    fish_counts = timestep(fish_counts)
    print(f"{i} {sum(fish_counts)}")

print(f"part 1: {sum(fish_counts)}")
