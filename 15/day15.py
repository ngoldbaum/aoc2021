from collections import defaultdict
from math import inf
import heapq


def get_neighbors(i, j, width, height):
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
    return neighbor_coords


with open("input") as f:
    risk_map = [list(map(int, line.strip())) for line in f.readlines()]

height = len(risk_map) * 5
width = len(risk_map[0]) * 5

full_risk_map = []

for j in range(height):
    full_risk_map.append([])
    for i in range(width):
        orig = risk_map[j % (height // 5)][i % (width // 5)]
        offset = i // (width // 5) + j // (height // 5)
        risk = orig + offset
        if risk > 9:
            risk = risk % 9
        full_risk_map[j].append(risk)


distance = defaultdict(lambda: inf)

distance[(0, 0)] = 0

target = (width - 1, height - 1)

pq = [(0, (0, 0))]

while pq:
    current_distance, current_vertex = heapq.heappop(pq)

    if current_distance > distance[current_vertex]:
        continue

    neighbors = get_neighbors(current_vertex[0], current_vertex[1], width, height)
    for neighbor in neighbors:
        dist = distance[current_vertex] + full_risk_map[neighbor[1]][neighbor[0]]
        if dist < distance[neighbor]:
            distance[neighbor] = dist
            heapq.heappush(pq, (dist, neighbor))

print(distance[target])
