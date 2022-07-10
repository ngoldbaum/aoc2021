with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

brackets = {"}": "{", ")": "(", "]": "[", ">": "<"}
brackets_inv = {v: k for k, v in brackets.items()}
openers = brackets.values()

illegal_characters = []
incomplete_closings = []

for line in lines:
    stack = []
    for char in line:
        if char in openers:
            stack.append(char)
        elif brackets[char] != stack.pop():
            illegal_characters.append(char)
            break
    else:
        incomplete_closings.append(
            list(map(lambda x: brackets_inv[x], reversed(stack)))
        )


def get_score(char):
    match char:
        case ")":
            return 3
        case "]":
            return 57
        case "}":
            return 1197
        case ">":
            return 25137


score = sum(map(get_score, illegal_characters))

print(f"part 1: {score}")

scores = []

closing_values = {")": 1, "]": 2, "}": 3, ">": 4}

for closing in incomplete_closings:
    score = 0
    for char in closing:
        score *= 5
        score += closing_values[char]
    scores.append(score)

print(sorted(scores)[len(scores) // 2])
