def transpose(grid):
    new_grid = []
    for i in range(len(grid[0])):
        new_grid.append("".join([row[i] for row in grid]))
    return new_grid


def find_parallel_columns(mirrors):
    return find_parallel_rows(transpose(mirrors))


def find_parallel_rows(mirrors):
    for i in range(len(mirrors) - 1):
        top_rows = i + 1
        total_rows = min(i + 1, len(mirrors) - i - 1)
        for j in range(total_rows):
            if mirrors[i - j] != mirrors[i + 1 + j]:
                break
        else:
            return top_rows
    return 0


def find_parallel_columns_2(mirrors, previous):
    return find_parallel_rows_2(transpose(mirrors), previous)


def find_parallel_rows_2(mirrors, previous):
    for i in range(len(mirrors) - 1):
        top_rows = i + 1
        total_rows = min(i + 1, len(mirrors) - i - 1)
        for j in range(total_rows):
            if mirrors[i - j] != mirrors[i + 1 + j]:
                break
        else:
            if top_rows != previous:
                return top_rows
    return 0


def find_score(mirrors):
    return find_parallel_columns(mirrors) + 100 * find_parallel_rows(mirrors)


def flip_item(mirrors, rc, cc):
    new_mirrors = []
    for rc2, row in enumerate(mirrors):
        new_mirrors.append([])
        for cc2, elem in enumerate(row):
            if rc2 == rc and cc2 == cc:
                if elem == '#':
                    new_mirrors[-1].append('.')
                else:
                    new_mirrors[-1].append('#')
            else:
                new_mirrors[-1].append(elem)
    return new_mirrors


def find_score_2(mirrors):
    cols = find_parallel_columns(mirrors)
    rows = find_parallel_rows(mirrors)
    for rc, row in enumerate(mirrors):
        for cc, elem in enumerate(mirrors):
            flipped = flip_item(mirrors, rc, cc)
            new_cols = find_parallel_columns_2(flipped, cols)
            new_rows = find_parallel_rows_2(flipped, rows)
            score = new_cols + 100 * new_rows
            if score != 0:
                return score
    return 0


def part_1():
    number = 0
    with open("input.txt", "r") as f:
        mirrors = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            if l == "":
                number += find_score(mirrors)
                mirrors = []
            else:
                mirrors.append(l)
        if mirrors:
            number += find_score(mirrors)
    return number


def part_2():
    number = 0
    with open("input.txt", "r") as f:
        mirrors = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            if l == "":
                number += find_score_2(mirrors)
                mirrors = []
            else:
                mirrors.append(l)
        if mirrors:
            number += find_score_2(mirrors)
    return number


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
