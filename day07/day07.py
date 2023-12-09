import sys


def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    char_tuples = list(char_count.items())
    return char_tuples


def card_type(hand):
    chars1 = count_characters(hand)
    if max([c[1] for c in chars1]) == 5:
        # hand1 es five
        return 7
    elif max([c[1] for c in chars1]) == 4:
        # hand1 es four
        return 6
    elif max([c[1] for c in chars1]) == 3 and 2 in [c[1] for c in chars1]:
        # full house
        return 5
    elif max([c[1] for c in chars1]) == 3:
        # three
        return 4
    elif max([c[1] for c in chars1]) == 2 and [c[1] for c in chars1].count(2) == 2:
        # twopair
        return 3
    elif max([c[1] for c in chars1]) == 2:
        # onepair
        return 2
    else:
        # highcard
        return 1


def card_type_2(hand):
    hand2 = [c for c in hand if c != 'J']
    chars1 = count_characters(hand2)
    numbers = [c[1] for c in chars1]
    numbers.sort(reverse=True)
    numbers = [0] if len(numbers) == 0 else numbers
    numbers[0] += hand.count('J')
    if max(numbers) == 5:
        # hand1 es five
        return 7
    elif max(numbers) == 4:
        # hand1 es four
        return 6
    elif max(numbers) == 3 and 2 in numbers:
        # full house
        return 5
    elif max(numbers) == 3:
        # three
        return 4
    elif max(numbers) == 2 and numbers.count(2) == 2:
        # twopair
        return 3
    elif max(numbers) == 2:
        # onepair
        return 2
    else:
        # highcard
        return 1


def compare_hands(hand1, hand2):
    cards_in_order = "AKQJT98765432"
    if card_type(hand1) > card_type(hand2):
        return True
    elif card_type(hand1) < card_type(hand2):
        return False
    else:
        for i in range(len(hand1)):
            if cards_in_order.index(hand1[i]) < cards_in_order.index(hand2[i]):
                return True
            elif cards_in_order.index(hand1[i]) > cards_in_order.index(hand2[i]):
                return False
        return None


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare_hands(arr[j][0], arr[j + 1][0]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def compare_hands_2(hand1, hand2):
    cards_in_order = "AKQT98765432J"
    if card_type_2(hand1) > card_type_2(hand2):
        return True
    elif card_type_2(hand1) < card_type_2(hand2):
        return False
    else:
        for i in range(len(hand1)):
            if cards_in_order.index(hand1[i]) < cards_in_order.index(hand2[i]):
                return True
            elif cards_in_order.index(hand1[i]) > cards_in_order.index(hand2[i]):
                return False
        return None


def bubble_sort_2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare_hands_2(arr[j][0], arr[j + 1][0]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def part_1():
    hands = []
    with open("input.txt", "r") as f:
        for l in [line.rstrip('\n') for line in f.readlines()]:
            hand = l.split(" ")[0]
            bid = int(l.split(" ")[1])
            hands.append((hand, bid))
    bubble_sort(hands)
    result = 0
    for i in range(len(hands)):
        result += (hands[i][1] * (i + 1))
    return result


def part_2():
    hands = []
    with open("input.txt", "r") as f:
        for l in [line.rstrip('\n') for line in f.readlines()]:
            hand = l.split(" ")[0]
            bid = int(l.split(" ")[1])
            hands.append((hand, bid))
    bubble_sort_2(hands)
    result = 0
    print(hands)
    for i in range(len(hands)):
        print(hands[i][0], i + 1)
        result += (hands[i][1] * (i + 1))
    return result


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
