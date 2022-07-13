from collections import defaultdict


class Cave:
    def __init__(self, name):
        self.name = name
        self.children = set()

    def add_children(self, nodes, edges):
        if self.name == "end":
            return
        for edge in edges:
            if self.name == edge[0].name:
                self.children.add(edge[1])
            elif self.name == edge[1].name:
                self.children.add(edge[0])

    def __repr__(self):
        return f"Cave {self.name}"

    @property
    def big(self):
        return self.name.isupper()


def navigate(node, path, visited):
    if node.name != "end":
        npaths = 0
        paths = []
        for child in node.children:
            cpath = path.copy()
            cvisited = visited.copy()
            if child.name == "start":
                continue
            if child in cvisited and any(v > 1 for v in cvisited.values()):
                continue
            if not child.big:
                cvisited[child] += 1
            cpath.append(child)
            cpaths, cnpaths = navigate(child, cpath, cvisited)
            npaths += cnpaths
            paths.extend(cpaths)
    else:
        return [path.copy()], 1

    return paths, npaths


with open("input") as f:
    edges = [line.strip().split("-") for line in f.readlines()]

node_names = set(sum(edges, start=[]))
nodes = {node_name: Cave(node_name) for node_name in node_names}
edges = [[nodes[e[0]], nodes[e[1]]] for e in edges]

for cave in nodes.values():
    cave.add_children(nodes, edges)

root = nodes["start"]
npaths = 0

paths, npaths = navigate(root, [root], defaultdict(lambda: 0))

print(npaths)
