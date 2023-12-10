from dataclasses import dataclass


@dataclass
class Node:
    row: int
    col: int

    tile_type: str

    distance: int

    is_main_loop: bool = False
    is_inside: bool = False


def fill_distances_and_get_max(mapa, start_r, start_c):
    visited = []
    queue = [(start_r, start_c)]

    mapa[start_r][start_c].distance = 0

    max_distance = 0

    while len(queue) > 0:
        rowc, colc = queue.pop(0)
        if (rowc, colc) in visited:
            continue
        visited.append((rowc, colc))
        if mapa[rowc][colc].tile_type == "|":
            north_node = (rowc - 1, colc)
            if north_node not in visited and north_node not in queue:
                mapa[north_node[0]][north_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(north_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)

            south_node = (rowc + 1, colc)
            if south_node not in visited and south_node not in queue:
                mapa[south_node[0]][south_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(south_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)
        elif mapa[rowc][colc].tile_type == "-":
            east_node = (rowc, colc + 1)
            if east_node not in visited and east_node not in queue:
                mapa[east_node[0]][east_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(east_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)

            west_node = (rowc, colc - 1)
            if west_node not in visited and west_node not in queue:
                mapa[west_node[0]][west_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(west_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)
        elif mapa[rowc][colc].tile_type == "L":
            north_node = (rowc - 1, colc)
            if north_node not in visited and north_node not in queue:
                mapa[north_node[0]][north_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(north_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)

            east_node = (rowc, colc + 1)
            if east_node not in visited and east_node not in queue:
                mapa[east_node[0]][east_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(east_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)
        elif mapa[rowc][colc].tile_type == "J":
            west_node = (rowc, colc - 1)
            if west_node not in visited and west_node not in queue:
                mapa[west_node[0]][west_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(west_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)

            north_node = (rowc - 1, colc)
            if north_node not in visited and north_node not in queue:
                mapa[north_node[0]][north_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(north_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)
        elif mapa[rowc][colc].tile_type == "7":
            west_node = (rowc, colc - 1)
            if west_node not in visited and west_node not in queue:
                mapa[west_node[0]][west_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(west_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)

            south_node = (rowc + 1, colc)
            if south_node not in visited and south_node not in queue:
                mapa[south_node[0]][south_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(south_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)
        elif mapa[rowc][colc].tile_type == "F":
            south_node = (rowc + 1, colc)
            if south_node not in visited and south_node not in queue:
                mapa[south_node[0]][south_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(south_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)

            east_node = (rowc, colc + 1)
            if east_node not in visited and east_node not in queue:
                mapa[east_node[0]][east_node[1]].distance = mapa[rowc][colc].distance + 1
                queue.append(east_node)
                max_distance = max(max_distance, mapa[rowc][colc].distance + 1)
    return max_distance


def mark_main_loop(mapa, start_r, start_c):
    visited = []
    queue = [(start_r, start_c)]

    mapa[start_r][start_c].distance = 0

    max_distance = 0

    while len(queue) > 0:
        rowc, colc = queue.pop(len(queue) - 1)
        mapa[rowc][colc].is_main_loop = True
        if (rowc, colc) in visited:
            return visited
        visited.append((rowc, colc))
        if mapa[rowc][colc].tile_type == "|":
            north_node = (rowc - 1, colc)
            if north_node not in visited and north_node not in queue:
                queue.append(north_node)

            south_node = (rowc + 1, colc)
            if south_node not in visited and south_node not in queue:
                queue.append(south_node)
        elif mapa[rowc][colc].tile_type == "-":
            east_node = (rowc, colc + 1)
            if east_node not in visited and east_node not in queue:
                queue.append(east_node)

            west_node = (rowc, colc - 1)
            if west_node not in visited and west_node not in queue:
                queue.append(west_node)
        elif mapa[rowc][colc].tile_type == "L":
            north_node = (rowc - 1, colc)
            if north_node not in visited and north_node not in queue:
                queue.append(north_node)

            east_node = (rowc, colc + 1)
            if east_node not in visited and east_node not in queue:
                queue.append(east_node)
        elif mapa[rowc][colc].tile_type == "J":
            west_node = (rowc, colc - 1)
            if west_node not in visited and west_node not in queue:
                queue.append(west_node)

            north_node = (rowc - 1, colc)
            if north_node not in visited and north_node not in queue:
                queue.append(north_node)
        elif mapa[rowc][colc].tile_type == "7":
            west_node = (rowc, colc - 1)
            if west_node not in visited and west_node not in queue:
                queue.append(west_node)

            south_node = (rowc + 1, colc)
            if south_node not in visited and south_node not in queue:
                queue.append(south_node)
        elif mapa[rowc][colc].tile_type == "F":
            south_node = (rowc + 1, colc)
            if south_node not in visited and south_node not in queue:
                queue.append(south_node)

            east_node = (rowc, colc + 1)
            if east_node not in visited and east_node not in queue:
                queue.append(east_node)
    return visited


def part_1():
    with open("input.txt", "r") as f:
        mapa = []
        start_row, start_col = 0, 0
        row_c = 0
        for l in [line.rstrip('\n') for line in f.readlines()]:
            row = []
            col_c = 0
            for char in l:
                if char == "S":
                    start_row, start_col = row_c, col_c
                nd = Node(row_c, col_c, char, 0)
                col_c += 1
                row.append(nd)
            mapa.append(row)
            row_c += 1

    mapa[start_row][start_col].tile_type = "L"

    value = fill_distances_and_get_max(mapa, start_row, start_col)
    for row in mapa:
        for elem in row:
            print(elem.distance, end=" ")
        print("")
    return value


def part_2():
    with open("input.txt", "r") as f:
        mapa = []
        start_row, start_col = 0, 0
        row_c = 0
        for l in [line.rstrip('\n') for line in f.readlines()]:
            row = []
            col_c = 0
            for char in l:
                if char == "S":
                    start_row, start_col = row_c, col_c
                nd = Node(row_c, col_c, char, 0)
                col_c += 1
                row.append(nd)
            mapa.append(row)
            row_c += 1

    mapa[start_row][start_col].tile_type = "L"

    path = mark_main_loop(mapa, start_row, start_col)

    inside_tiles = 0
    winding_number = 0
    for rowc, row in enumerate(mapa[:-1]):
        for colc, elem in enumerate(row):
            if elem.is_main_loop:
                if mapa[rowc + 1][colc].is_main_loop:
                    if path.index((rowc, colc)) == (path.index((rowc + 1, colc)) + 1) % len(path):
                        winding_number += 1
                    if path.index((rowc, colc)) == (path.index((rowc + 1, colc)) - 1) % len(path):
                        winding_number -= 1
            elif winding_number != 0:
                inside_tiles += 1
                elem.is_inside = True
    for row in mapa:
        for elem in row:
            if elem.is_main_loop:
                print("#", end="")
            elif elem.is_inside:
                print("I", end="")
            else:
                print("O", end="")
        print("")
    return inside_tiles


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
