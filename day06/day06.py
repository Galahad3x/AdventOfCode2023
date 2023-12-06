import numpy as np
from tqdm import tqdm

times = [47, 98, 66, 98]
distances = [400, 1213, 1011, 1540]

timetotal = 47986698
distancetotal = 400121310111540


def part_1():
    list_of_valids = []
    for i in range(len(times)):
        valid_holds = 0
        for t in range(times[i]):
            if (times[i] - t) * t > distances[i]:
                valid_holds += 1
        list_of_valids.append(valid_holds)
    return np.prod(list_of_valids)


def part_2():
    valid_holds = 0
    for t in tqdm(range(timetotal)):
        if (timetotal - t) * t > distancetotal:
            valid_holds += 1
    return valid_holds


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
