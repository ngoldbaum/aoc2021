from collections import defaultdict

with open("input") as f:
    template, rules = f.read().split("\n\n")
    rules = dict([r.split(" -> ") for r in rules.strip().split("\n")])

atoms = set(template)
pairs = list(map(lambda p: p[0] + p[1], zip(template, template[1:])))
pair_occurances = defaultdict(lambda: 0)
for p in pairs:
    pair_occurances[p] += 1

for i in range(40):
    new_occurances = defaultdict(lambda: 0)
    for p, cnt in list(pair_occurances.items()):
        if p in rules:
            new_occurances[p[0] + rules[p]] += cnt
            new_occurances[rules[p] + p[1]] += cnt
    pair_occurances = new_occurances

counts = defaultdict(lambda: 0)
for p, o in pair_occurances.items():
    counts[p[0]] += o
    counts[p[1]] += o

counts[template[0]] += 1
counts[template[-1]] += 1

for k in counts:
    counts[k] //= 2

print(max(counts.values()) - min(counts.values()))
