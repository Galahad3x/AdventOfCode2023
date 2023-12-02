def extract_digits(input_string):
    result = ''.join(char for char in input_string if char.isdigit())
    return result


def part_1():
    with open("input.txt", "r") as f:
        red_cubes = 12
        green_cubes = 13
        blue_cubes = 14
        sum_of_ids = 0
        for l in [line.rstrip('\n') for line in f.readlines()]:
            game_id = int(l[len("Game "):l.find(":")])
            game_valid = True
            for play in [p.strip(" ") for p in l[l.find(":") + 1:].split(";")]:
                for cubes in play.split(","):
                    if "red" in cubes:
                        if int(extract_digits(cubes)) > red_cubes:
                            game_valid = False
                            break
                    elif "green" in cubes:
                        if int(extract_digits(cubes)) > green_cubes:
                            game_valid = False
                            break
                    elif "blue" in cubes:
                        if int(extract_digits(cubes)) > blue_cubes:
                            game_valid = False
                            break
                if not game_valid:
                    break
            if game_valid:
                sum_of_ids += game_id
    return sum_of_ids


def part_2():
    with open("input.txt", "r") as f:
        power_sum = 0
        for l in [line.rstrip('\n') for line in f.readlines()]:
            min_red = 0
            min_green = 0
            min_blue = 0
            for play in [p.strip(" ") for p in l[l.find(":") + 1:].split(";")]:
                for cubes in play.split(","):
                    if "red" in cubes:
                        if int(extract_digits(cubes)) > min_red:
                            min_red = int(extract_digits(cubes))
                    elif "green" in cubes:
                        if int(extract_digits(cubes)) > min_green:
                            min_green = int(extract_digits(cubes))
                    elif "blue" in cubes:
                        if int(extract_digits(cubes)) > min_blue:
                            min_blue = int(extract_digits(cubes))
            power_sum += (min_red * min_blue * min_green)
    return power_sum


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
