from dataclasses import dataclass


@dataclass
class Lens:
    label: str
    focal_length: int


def determine_hash(step):
    hashval = 0
    for c in step:
        hashval += ord(c)
        hashval *= 17
        hashval = hashval % 256
    return hashval


def part_1():
    with open("input.txt", "r") as f:
        value = 0
        for l in [line.rstrip('\n') for line in f.readlines()]:
            for step in l.split(","):
                value += determine_hash(step)
    return value


def print_boxes(boxes):
    for i, box in enumerate(boxes):
        if len(box) == 0:
            continue
        print(f"[Box {i}]:", end=" ")
        for lens in box:
            print(f"[{lens.label} {lens.focal_length}]", end=" ")
        print()
    print()


def focusing_power(boxes):
    total = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            total += (i + 1) * (j + 1) * lens.focal_length
    return total


def part_2():
    with open("input.txt", "r") as f:
        for l in [line.rstrip('\n') for line in f.readlines()]:
            boxes = []
            for _ in range(256):
                boxes.append([])

            for step in l.split(","):
                if "=" in step:
                    label = step.split("=")[0]
                    box_index = determine_hash(label)
                    focal_length = int(step.split("=")[1])
                    lens = Lens(label, focal_length)
                    if label in [l.label for l in boxes[box_index]]:
                        i = 0
                        for _ in range(len(boxes[box_index])):
                            if boxes[box_index][i].label == label:
                                break
                            i += 1
                        boxes[box_index][i] = lens
                    else:
                        boxes[box_index].append(lens)
                elif "-" in step:
                    label = step[:-1]
                    box_index = determine_hash(label)
                    if label in [l.label for l in boxes[box_index]]:
                        i = 0
                        for _ in range(len(boxes[box_index])):
                            if boxes[box_index][i].label == label:
                                break
                            i += 1
                        boxes[box_index].pop(i)
                # print_boxes(boxes)
    return focusing_power(boxes)


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
