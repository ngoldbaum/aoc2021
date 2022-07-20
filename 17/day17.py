import re

with open("input") as f:
    bbox = f.read().strip()

(x0, x1), (y0, y1) = re.findall(r"[xy]=(-?\d{1,})..(-?\d{1,})", bbox)

x0, x1, y0, y1 = map(int, [x0, x1, y0, y1])

max_height = 0
nhits = 0

for vx in range(0, x1 + 1):
    for vy in range(-400, 400):
        velocity = [vx, vy]

        position = [0, 0]

        positions = []

        hit = False

        while position[0] < x1 and position[1] > y0:
            positions.append(position.copy())
            position[0] += velocity[0]
            position[1] += velocity[1]
            if velocity[0] > 0:
                velocity[0] -= 1
            elif velocity[0] < 0:
                velocity[0] += 1
            velocity[1] -= 1
            if x0 <= position[0] <= x1 and y0 <= position[1] <= y1:
                hit = True
                nhits += 1
                break

        positions.append(position.copy())
        if hit:
            this_max_height = max(positions, key=lambda x: x[1])[1]
            if this_max_height > max_height:
                max_height = this_max_height

print(max_height)
print(nhits)
