with open("input") as f:
    commands = [(c, int(a)) for c, a in [line.split() for line in f]]

pos, depth = 0, 0

for (direction, distance) in commands:
    match direction:
        case "forward":
            pos += distance
        case "down":
            depth += distance
        case "up":
            depth -= distance

print(f"part 1: {pos*depth}")

pos, depth, aim = 0, 0, 0

for (command, argument) in commands:
    match command:
        case "down":
            aim += argument
        case "up":
            aim -= argument
        case "forward":
            pos += argument
            depth += argument * aim

print(f"part 2: {pos*depth}")
