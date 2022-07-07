with open("input") as f:
    positions = list(map(int, f.read().split(",")))

fuels = []

for i in range(len(positions)):
    tot_fuel = 0
    for pos in positions:
        dist = abs(pos - i)
        tot_fuel += int(dist * (dist + 1) / 2)
    fuels.append(tot_fuel)

print(min(fuels))
