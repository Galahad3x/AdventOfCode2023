from itertools import combinations


def calculate_distance(mapa, galaxy1, galaxy2, expansion_factor=2):
    expansions_horizontal = 0
    for i in range(abs(galaxy1[1] - galaxy2[1])):
        if mapa[min(galaxy1[0], galaxy2[0])][min(galaxy1[1], galaxy2[1]) + i] == 'e':
            expansions_horizontal += 1
    expansions_vertical = 0
    for i in range(abs(galaxy1[0] - galaxy2[0])):
        if mapa[min(galaxy1[0], galaxy2[0]) + i][min(galaxy1[1], galaxy2[1])] == 'e':
            expansions_vertical += 1
    return abs(galaxy1[0] - galaxy2[0]) + abs(
        galaxy1[1] - galaxy2[1]) + expansions_horizontal * (expansion_factor - 1) + expansions_vertical * (
                expansion_factor - 1)


def part_1():
    mapa = []
    with open("mini.txt", "r") as f:
        for l in [line.rstrip('\n') for line in f.readlines()]:
            mapa.append(l)
    mapa2 = []
    for i, row in enumerate(mapa):
        must_expand = True
        for e in row:
            if e != '.':
                must_expand = False
                break
        if must_expand:
            mapa2.append('e' * len(row))
        else:
            mapa2.append(row)

    mapa = mapa2
    mapa2 = []
    width = len(mapa[0])
    for colc in range(width):
        all_p = True
        for i, row in enumerate(mapa):
            if row[colc] != '.' and row[colc] != 'e':
                all_p = False
                break
        if all_p:
            for i, row in enumerate(mapa):
                if colc == 0:
                    mapa2.append(['e'])
                else:
                    mapa2[i].append('e')
        else:
            for i, row in enumerate(mapa):
                if colc == 0:
                    mapa2.append([row[colc]])
                else:
                    mapa2[i].append(row[colc])

    mapa = mapa2
    galaxies = []
    for rowc, r in enumerate(mapa):
        for colc, e in enumerate(r):
            if e == '#':
                galaxies.append((rowc, colc))

    distances = 0
    for galaxy1, galaxy2 in combinations(galaxies, 2):
        distances += calculate_distance(mapa, galaxy1, galaxy2)

    return distances


def part_2():
    mapa = []
    with open("input.txt", "r") as f:
        for l in [line.rstrip('\n') for line in f.readlines()]:
            mapa.append(l)
    mapa2 = []
    for i, row in enumerate(mapa):
        must_expand = True
        for e in row:
            if e != '.':
                must_expand = False
                break
        if must_expand:
            mapa2.append('e' * len(row))
        else:
            mapa2.append(row)

    mapa = mapa2
    mapa2 = []
    width = len(mapa[0])
    for colc in range(width):
        all_p = True
        for i, row in enumerate(mapa):
            if row[colc] != '.' and row[colc] != 'e':
                all_p = False
                break
        if all_p:
            for i, row in enumerate(mapa):
                if colc == 0:
                    mapa2.append(['e'])
                else:
                    mapa2[i].append('e')
        else:
            for i, row in enumerate(mapa):
                if colc == 0:
                    mapa2.append([row[colc]])
                else:
                    mapa2[i].append(row[colc])

    mapa = mapa2
    galaxies = []
    for rowc, r in enumerate(mapa):
        for colc, e in enumerate(r):
            if e == '#':
                galaxies.append((rowc, colc))

    distances = 0
    for galaxy1, galaxy2 in combinations(galaxies, 2):
        distances += calculate_distance(mapa, galaxy1, galaxy2, expansion_factor=1000000)

    return distances


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
