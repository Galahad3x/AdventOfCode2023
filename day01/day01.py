def part_1():
    with open("input.txt", "r") as f:
        values = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            digit_arr = []
            for i, c in enumerate(l):
                if c.isdigit():
                    digit_arr.append(c)
            values.append(int(digit_arr[0] + digit_arr[-1]))
    return sum(values)


def part_2():
    with open("input.txt", "r") as f:
        values = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            digit_arr = []
            for i, c in enumerate(l):
                if c.isdigit():
                    digit_arr.append(c)
                else:
                    for digit, number in [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'),
                                          (6, 'six'),
                                          (7, 'seven'), (8, 'eight'), (9, 'nine')]:
                        if l[i:].startswith(number):
                            digit_arr.append(str(digit))
            values.append(int(digit_arr[0] + digit_arr[-1]))
    return sum(values)


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
