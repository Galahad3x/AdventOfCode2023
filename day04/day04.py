from tqdm import tqdm


def part_1():
    with open("input.txt", "r") as f:
        sum_points = 0
        for l in [line.rstrip('\n') for line in f.readlines()]:
            nums = l.split(":")[1]
            winnings = [int(n) for n in nums.split("|")[0].split(" ") if n != ""]
            numbers = [int(n) for n in nums.split("|")[1].split(" ") if n != ""]
            c = 0
            for n in numbers:
                if n in winnings:
                    c += 1
            if c > 0:
                sum_points += 2 ** (c - 1)
    return sum_points


def part_2():
    with open("input.txt", "r") as f:
        cards = []
        card_winnings = []
        for i, l in enumerate([line.rstrip('\n') for line in f.readlines()]):
            nums = l.split(":")[1]
            winnings = [int(n) for n in nums.split("|")[0].split(" ") if n != ""]
            numbers = [int(n) for n in nums.split("|")[1].split(" ") if n != ""]
            cards.append((i, winnings, numbers))
            c = 0
            for n in numbers:
                if n in winnings:
                    c += 1
            card_winnings.append(c)

        total_cards = [1] * len(cards)
        for i in tqdm(range(len(card_winnings))):
            for j in range(1, card_winnings[i] + 1):
                if i + j < len(cards):
                    total_cards[i + j] += total_cards[i]

    return sum(total_cards)


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
