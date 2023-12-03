from dataclasses import dataclass

from tqdm import tqdm


@dataclass
class Node:
    value: str
    neighbours: []
    used: bool = False


def part_1():
    with open("input.txt", "r") as f:
        matrix = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            matrix.append(l)
        nodes = []
        for y, l in enumerate(matrix):
            for x, c in enumerate(l):
                if c.isdigit():
                    if x > 0 and l[x - 1].isdigit():
                        continue
                neighbours = []
                if x > 0:
                    if y > 0:
                        neighbours.append(matrix[y - 1][x - 1])
                    neighbours.append(matrix[y][x - 1])
                    if y + 1 < len(matrix):
                        neighbours.append(matrix[y + 1][x - 1])
                pointer = x
                if c.isdigit():
                    number_str = ''
                    while pointer < len(l) and l[pointer].isdigit():
                        number_str += l[pointer]
                        if y > 0:
                            neighbours.append(matrix[y - 1][pointer])
                        if y + 1 < len(matrix):
                            neighbours.append(matrix[y + 1][pointer])
                        pointer += 1
                    if pointer + 1 < len(l):
                        if y > 0:
                            neighbours.append(matrix[y - 1][pointer])
                        neighbours.append(matrix[y][pointer])
                        if y + 1 < len(matrix):
                            neighbours.append(matrix[y + 1][pointer])
                else:
                    if y > 0:
                        neighbours.append(matrix[y - 1][x])
                    if y + 1 < len(matrix):
                        neighbours.append(matrix[y + 1][x])

                if c.isdigit():
                    nd = Node(number_str, neighbours)
                else:
                    nd = Node(c, neighbours)
                nodes.append(nd)

        parts_sum = 0
        for node in nodes:
            if node.value != '.' and node.value.isnumeric():
                for neighbour in node.neighbours:
                    if neighbour != '.' and not neighbour.isnumeric():
                        parts_sum += int(node.value)
                        break
        return parts_sum


def check_stars(stars, matrix, x, y, value):
    new_stars = stars
    if matrix[y][x] == '*':
        for star in stars:
            if (star[0], star[1]) == (x, y):
                star[2].append(value)
                break
        else:
            new_stars.append((x, y, [value]))
    return new_stars


def part_2():
    with open("input.txt", "r") as f:
        matrix = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            matrix.append(l)
        stars = []
        for y, l in enumerate(matrix):
            for x, c in enumerate(l):
                if c.isdigit():
                    if x > 0 and l[x - 1].isdigit():
                        continue
                if not c.isdigit() and c != '*':
                    continue
                pointer = x
                if c.isdigit():
                    number_str = ''
                    while pointer < len(l) and l[pointer].isdigit():
                        number_str += l[pointer]
                        pointer += 1
                pointer = x
                if c.isdigit():
                    while pointer < len(l) and l[pointer].isdigit():
                        if y > 0:
                            stars = check_stars(stars, matrix, pointer, y - 1, int(number_str))
                        if y + 1 < len(matrix):
                            stars = check_stars(stars, matrix, pointer, y + 1, int(number_str))
                        pointer += 1
                    if pointer + 1 < len(l):
                        if y > 0:
                            stars = check_stars(stars, matrix, pointer, y - 1, int(number_str))
                        stars = check_stars(stars, matrix, pointer, y, int(number_str))
                        if y + 1 < len(matrix):
                            stars = check_stars(stars, matrix, pointer, y + 1, int(number_str))
                if x > 0:
                    if y > 0:
                        stars = check_stars(stars, matrix, x - 1, y - 1, int(number_str))
                    stars = check_stars(stars, matrix, x - 1, y, int(number_str))
                    if y + 1 < len(matrix):
                        stars = check_stars(stars, matrix, x - 1, y + 1, int(number_str))
                else:
                    if y > 0:
                        stars = check_stars(stars, matrix, x, y - 1, int(number_str))
                    if y + 1 < len(matrix):
                        stars = check_stars(stars, matrix, x, y + 1, int(number_str))

        sum_ratio = 0
        for star in stars:
            if len(star[2]) == 2:
                sum_ratio += star[2][0] * star[2][1]
        return sum_ratio


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
