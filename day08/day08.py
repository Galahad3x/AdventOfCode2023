input_path = "LRRLRRLLRRRLRRLRLRRRLRRLRRRLRLLRRRLRRRLRLRRRLRRLRRLRLRLLLRRRLRRRLRRLRRLRLRRRLRRLLRRLRRLRLLRLRLRRLRLLRLRLRRRLRRLRLLRLRLLRRLRLRRLLLRLRRLRRRLLLRRLRLRRRLLRRLLLRRRLRRRLLLRRLLRLRRLRLRRLLLRLRRLLLLRRLLRRRLRRLRRLRLRLLRLRRRLLRRLLRRLRRLRRLRRLRLLRRLRRRLRLRLLLRRRLLRRRLRRLRRLLLLRRRR"
mini_path = "LR"
medium_path = "LLR"
from math import gcd


def part_1():
    path = input_path
    with open("input.txt", "r") as f:
        mapa = {}
        for l in [line.rstrip('\n') for line in f.readlines()]:
            start_node = l.split(" = ")[0]
            paths = l.split(" = ")[1].replace("(", "").replace(" ", "").replace(")", "").split(",")
            left = paths[0]
            right = paths[1]
            mapa[start_node] = {
                'L': left,
                'R': right
            }
        steps = 0
        current_node = "AAA"
        while current_node != "ZZZ":
            current_node = mapa[current_node][path[steps % len(path)]]
            steps += 1
    return steps


def all_end_in_z(nodes):
    for n in nodes:
        if n[-1] != 'Z':
            return False
    return True


def lcm(x, y):
    """Calculate the least common multiple of x and y."""
    return x * y // gcd(x, y)

def lcm_of_list(numbers):
    """Calculate the least common multiple of a list of numbers."""
    result = 1
    for number in numbers:
        result = lcm(result, number)
    return result

def part_2():
    path = input_path
    with open("input.txt", "r") as f:
        mapa = {}
        for l in [line.rstrip('\n') for line in f.readlines()]:
            start_node = l.split(" = ")[0]
            paths = l.split(" = ")[1].replace("(", "").replace(" ", "").replace(")", "").split(",")
            left = paths[0]
            right = paths[1]
            mapa[start_node] = {
                'L': left,
                'R': right
            }
        total_steps = []
        current_nodes = [n for n in mapa.keys() if n[-1] == "A"]
        for node in current_nodes:
            steps = 0
            while node[-1] != "Z":
                node = mapa[node][path[steps % len(path)]]
                steps += 1
            total_steps.append(steps)
    return lcm_of_list(total_steps)


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
