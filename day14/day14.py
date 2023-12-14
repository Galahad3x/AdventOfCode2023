from tqdm import tqdm


def tilt_north(dish):
    for rowc in range(1, len(dish)):
        for i in range(len((dish[rowc]))):
            current = rowc
            landing = rowc - 1
            while landing >= 0:
                if dish[landing][i] == '.' and dish[current][i] == 'O':
                    dish[current][i] = '.'
                    dish[landing][i] = 'O'
                    current -= 1
                    landing -= 1
                else:
                    break
    return dish


def tilt_west(dish):
    for rowc in range(len(dish)):
        for i in range(1, len(dish[rowc])):
            current = i
            landing = i - 1
            while landing >= 0:
                if dish[rowc][landing] == '.' and dish[rowc][current] == 'O':
                    dish[rowc][current] = '.'
                    dish[rowc][landing] = 'O'
                    current -= 1
                    landing -= 1
                else:
                    break
    return dish


def tilt_south(dish):
    for rowc in range(len(dish) - 1, -1, -1):
        for i in range(len((dish[rowc]))):
            current = rowc
            landing = rowc + 1
            while landing < len(dish):
                if dish[landing][i] == '.' and dish[current][i] == 'O':
                    dish[current][i] = '.'
                    dish[landing][i] = 'O'
                    current += 1
                    landing += 1
                else:
                    break
    return dish


def tilt_east(dish):
    for rowc in range(len(dish)):
        for i in range(len(dish[rowc]) - 2, -1, -1):
            current = i
            landing = i + 1
            while landing < len(dish[rowc]):
                if dish[rowc][landing] == '.' and dish[rowc][current] == 'O':
                    dish[rowc][current] = '.'
                    dish[rowc][landing] = 'O'
                    current += 1
                    landing += 1
                else:
                    break
    return dish


def calculate_load(dish):
    load = 0
    for c, row in enumerate(dish):
        load += row.count('O') * (len(dish) - c)
    return load


def perform_cycle(dish):
    dish = tilt_north(dish)
    dish = tilt_west(dish)
    dish = tilt_south(dish)
    dish = tilt_east(dish)
    return dish


def part_1():
    with open("mini.txt", "r") as f:
        dish = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            dish.append([c for c in l])
        tilted = tilt_north(dish)
    return calculate_load(tilted)


def part_2():
    with open("input.txt", "r") as f:
        dish = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            dish.append([c for c in l])

    cycle_story = []
    load_story = []
    objective = 1000000000
    for i in tqdm(range(objective)):
        state = ''.join([''.join(r) for r in dish])
        if state in cycle_story:
            loop_start = cycle_story.index(state)
            loop_finish = i
            loop_size = loop_finish - loop_start
            def_index = ((objective - loop_start) % loop_size) + loop_start
            return load_story[def_index]
        else:
            cycle_story.append(state)
            load_story.append(calculate_load(dish))

        dish = perform_cycle(dish)

    return calculate_load(dish)


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
