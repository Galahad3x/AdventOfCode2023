def find_differences(values):
    diffs = []
    for i in range(len(values) - 1):
        diffs.append(values[i + 1] - values[i])
    return diffs


def is_all_zeros(values):
    for elem in values:
        if elem != 0:
            return False
    return True


def find_next_element(values):
    if is_all_zeros(values):
        return 0
    return values[-1] + find_next_element(find_differences(values))


def find_next_element_start(values):
    if is_all_zeros(values):
        return 0
    return values[0] - find_next_element_start(find_differences(values))


def part_1():
    with open("input.txt", "r") as f:
        values_sum = 0
        for l in [line.rstrip('\n') for line in f.readlines()]:
            values = [int(e) for e in l.split(" ")]
            values_sum += find_next_element(values)
    return values_sum


def part_2():
    with open("input.txt", "r") as f:
        values_sum = 0
        for l in [line.rstrip('\n') for line in f.readlines()]:
            values = [int(e) for e in l.split(" ")]
            elem = find_next_element_start(values)
            # print(elem)
            values_sum += elem
    return values_sum


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
