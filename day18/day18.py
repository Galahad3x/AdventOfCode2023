from dataclasses import dataclass

from tqdm import tqdm


@dataclass
class Step:
    direction: str
    meters: int


def transform_to_mapa(trenchmap):
    min_row = min([t[0] for t in trenchmap])
    min_col = min([t[1] for t in trenchmap])
    max_row = max([t[0] for t in trenchmap])
    max_col = max([t[1] for t in trenchmap])
    row_size = max_row - min_row + 1
    col_size = max_col - min_col + 1

    mapa = []
    for colc in range(row_size):
        mapa.append([])
        for rowc in range(col_size):
            mapa[-1].append('.')

    adapted_trenchmap = []
    for t in trenchmap:
        adapted_trenchmap.append((t[0] - min_row, t[1] - min_col))
        mapa[t[0] - min_row][t[1] - min_col] = '#'
    return mapa, adapted_trenchmap


def adapt(trenchmap):
    min_row = min([t[0] for t in trenchmap])
    min_col = min([t[1] for t in trenchmap])
    max_row = max([t[0] for t in trenchmap])
    max_col = max([t[1] for t in trenchmap])
    col_size = max_row - min_row + 1
    row_size = max_col - min_col + 1

    adapted_trenchmap = []
    for t in trenchmap:
        adapted_trenchmap.append((t[0] - min_row, t[1] - min_col))
    return adapted_trenchmap, row_size, col_size


def part_1():
    with open("mini.txt", "r") as f:
        steps = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            direction, meters, _ = l.split(" ")
            steps.append(Step(direction, int(meters)))

    trenchmap = []
    rowc, colc = 0, 0
    # trenchmap.append((rowc, colc))
    for step in steps:
        for i in range(step.meters):
            if step.direction == 'U':
                rowc -= 1
            elif step.direction == 'D':
                rowc += 1
            elif step.direction == 'L':
                colc -= 1
            elif step.direction == 'R':
                colc += 1
            trenchmap.append((rowc, colc))

    trench_arr, trenchmap = transform_to_mapa(trenchmap)
    for row in trench_arr:
        print(''.join(row))
    print()

    winding_number = 0
    for rowc, row in enumerate(trench_arr[:-1]):
        for colc, elem in enumerate(row):
            if elem == '#':
                if trench_arr[rowc + 1][colc] == '#':
                    if trenchmap.index((rowc, colc)) == (trenchmap.index((rowc + 1, colc)) + 1) % len(trenchmap):
                        winding_number += 1
                    if trenchmap.index((rowc, colc)) == (trenchmap.index((rowc + 1, colc)) - 1) % len(trenchmap):
                        winding_number -= 1
            elif winding_number != 0:
                trench_arr[rowc][colc] = '#'

    for row in trench_arr:
        print(''.join(row))

    return sum([''.join(r).count('#') for r in trench_arr])


def calculate_perimeter(trenchmap):
    perimeter = 0
    rowc, colc = trenchmap[0]
    for vertex in trenchmap[1:]:
        vrow, vcol = vertex
        perimeter += abs(rowc - vrow) + abs(colc - vcol)
        rowc, colc = vertex
    return perimeter


def calculate_area(trenchmap):
    double_area = 0
    rowc, colc = trenchmap[0]
    for vertex in trenchmap[1:]:
        vrow, vcol = vertex
        double_area += rowc * vcol - colc * vrow
        rowc, colc = vertex
    return abs(double_area // 2)


def part_2():
    with open("input.txt", "r") as f:
        steps = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            _, _, color = l.split(" ")
            hexnum = color[2:-1]
            direction_encoded = int(hexnum[-1])
            meters = int(hexnum[:-1], 16)
            direction = ['R', 'D', 'L', 'U'][direction_encoded]
            steps.append(Step(direction, int(meters)))

    trenchmap = []
    rowc, colc = 0, 0
    trenchmap.append((rowc, colc))
    for step in steps:
        if step.direction == 'U':
            rowc -= step.meters
        elif step.direction == 'D':
            rowc += step.meters
        elif step.direction == 'L':
            colc -= step.meters
        elif step.direction == 'R':
            colc += step.meters
        trenchmap.append((rowc, colc))

    trenchmap, row_size, col_size = adapt(trenchmap)
    print(len(trenchmap))

    perimeter = calculate_perimeter(trenchmap)
    area = calculate_area(trenchmap)

    print(perimeter)
    print(area)

    i = area + 1 - perimeter / 2
    return int(i + perimeter)


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
