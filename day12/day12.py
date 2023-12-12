import itertools
from functools import cache

import tqdm


def get_config_from_spring(spring):
    return tuple([len(s) for s in spring.split(".") if len(s) != 0])


def apply_possible(springs, possible):
    new_spring = ""
    possible_c = 0
    for c in springs:
        if c == "?":
            new_spring += possible[possible_c]
            possible_c += 1
        else:
            new_spring += c
    return new_spring


def part_1():
    valid_configs = 0
    with open("input.txt", "r") as f:
        for l in tqdm.tqdm([line.rstrip('\n') for line in f.readlines()]):
            springs, config = l.split(" ")
            config = tuple([int(c) for c in config.split(",")])
            valid_configs += valid_bt(springs, tuple(config))
    return valid_configs


@cache
def valid_bt(spring, config):
    spring = spring.lstrip('.')
    if spring.count('?') == 0:
        return 1 if get_config_from_spring(spring) == config else 0
    if len(config) == 0:
        if spring.count('#') == 0:
            return 1
        else:
            return 0
    if spring == "" and config == ():
        return 1
    if spring[0] == '#':
        if len(spring) < config[0] or '.' in spring[:config[0]]:
            return 0  # impossible - not enough space for the spring
        elif len(spring) == config[0]:
            return int(len(config) == 1)  # single spring, right size
        elif spring[config[0]] == '#':
            return 0  # springs must be separated by '.' (or '?')
        else:
            return valid_bt(spring[config[0] + 1:], config[1:])  # one less spring
    next_index = spring.find('?')
    o1 = spring[:next_index] + '#' + spring[next_index + 1:]
    o2 = spring[:next_index] + '.' + spring[next_index + 1:]
    return valid_bt(o1, config) + valid_bt(o2, config)


def part_2():
    valid_configs = 0
    with open("input.txt", "r") as f:
        for l in tqdm.tqdm([line.rstrip('\n') for line in f.readlines()]):
            springs, config = l.split(" ")
            config = [int(c) for c in config.split(",")] * 5
            springs = '?'.join([springs] * 5)
            valid_configs += valid_bt(springs, tuple(config))
    return valid_configs


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
