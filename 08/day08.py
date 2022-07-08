with open("input") as f:
    lines = [
        [term.split() for term in line.strip().split(" | ")] for line in f.readlines()
    ]
    inputs = [list(map(lambda x: "".join(sorted(x)), line[0])) for line in lines]
    outputs = [list(map(lambda x: "".join(sorted(x)), line[1])) for line in lines]

num_digits = 0

for output in outputs:
    for code in output:
        if len(code) in [2, 3, 4, 7]:
            num_digits += 1

print(f"part 1: {num_digits}")

output_total = 0

for input, output in zip(inputs, outputs):
    digit_map = {}
    for code in sorted(input, key=lambda x: len(x)):
        match len(code):
            case 2:
                digit_map[1] = code
            case 3:
                digit_map[7] = code
            case 4:
                digit_map[4] = code
            case 5:
                # either 2, 3, or 5
                if all([c in code for c in list(digit_map[7])]):
                    digit_map[3] = code
                elif sum([1 if c in code else 0 for c in list(digit_map[4])]) == 3:
                    digit_map[5] = code
                else:
                    digit_map[2] = code
            case 6:
                # either 0, 6, or 9
                if all([c in code for c in list(digit_map[4])]):
                    digit_map[9] = code
                elif all([c in code for c in list(digit_map[7])]):
                    digit_map[0] = code
                else:
                    digit_map[6] = code
            case 7:
                digit_map[8] = code
    digit_map_inv = {v: k for k, v in digit_map.items()}
    output_total += int("".join([str(digit_map_inv[code]) for code in output]))

print(f"part 2: {output_total}")
