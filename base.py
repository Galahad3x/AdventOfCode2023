def part_1():
    with open("input.txt", "r") as f:
        for l in [line.rstrip('\n') for line in f.readlines()]:
            pass


def part_2():
    with open("input.txt", "r") as f:
        for l in [line.rstrip('\n') for line in f.readlines()]:
            pass


if __name__ in "__main__":
    print("PART 1:".center(__width=30, __fillchar="="))
    print(str(part_1()).center(__width=30))
    print("=".center(30))
    print("PART 2:".center(__width=30, __fillchar="="))
    print(str(part_2()).center(__width=30))
    print("=".center(30))
