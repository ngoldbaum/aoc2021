with open("input") as f:
    lines = f.readlines()

depths = [int(line) for line in lines]

# part 1

tot = 0

for first, second in zip(depths, depths[1:]):
    if second > first:
        tot += 1

print(f"part 1: {tot}")

# part 2

tot = 0

sums = [
    sum([first, second, third])
    for first, second, third in zip(depths, depths[1:], depths[2:])
]


for first, second in zip(sums, sums[1:]):
    if second > first:
        tot += 1

print(f"part 2: {tot}")
