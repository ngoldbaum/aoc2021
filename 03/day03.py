with open("input") as f:
    numbers = [tuple(map(int, line.strip())) for line in f.readlines()]


def count_digits(numbers):
    length = len(numbers[0])
    num_ones = [0] * length
    num_zeros = [0] * length

    for number in numbers:
        for i in range(length):
            d = number[i]
            match d:
                case 0:
                    num_zeros[i] += 1
                case 1:
                    num_ones[i] += 1

    return num_zeros, num_ones


num_zeros, num_ones = count_digits(numbers)

gamma = []
epsilon = []

for no, nz in zip(num_zeros, num_ones):
    if no > nz:
        gamma.append(1)
        epsilon.append(0)
    elif no < nz:
        gamma.append(0)
        epsilon.append(1)
    else:
        raise RuntimeError

epsilon = int("".join(map(str, epsilon)), 2)
gamma = int("".join(map(str, gamma)), 2)

print(f"part 1: {gamma*epsilon}")


def rating(numbers, criteria):
    length = len(numbers[0])
    numbers = set(numbers)
    ret = numbers.copy()
    for i in range(length):
        if len(ret) == 1:
            break
        numbers = ret.copy()
        num_zeros, num_ones = count_digits(list(numbers))
        for number in numbers:
            if criteria == "o2":
                if num_ones[i] >= num_zeros[i] and number[i] == 1:
                    continue
                elif num_zeros[i] > num_ones[i] and number[i] == 0:
                    continue
            if criteria == "co2":
                if num_zeros[i] <= num_ones[i] and number[i] == 0:
                    continue
                elif num_ones[i] < num_zeros[i] and number[i] == 1:
                    continue
            ret.discard(number)
    return ret.pop()


o2_rating = int("".join(map(str, rating(numbers.copy(), criteria="o2"))), 2)
co2_rating = int("".join(map(str, rating(numbers.copy(), criteria="co2"))), 2)

print(f"part 2: {o2_rating * co2_rating}")
