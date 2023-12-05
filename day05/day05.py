from tqdm import tqdm


def part_1():
    with open("input.txt", "r") as f:
        translations = {}
        current_translation = ""
        for l in [line.rstrip('\n') for line in f.readlines()]:
            if l.startswith("seeds:"):
                seeds = [int(s) for s in l.split(":")[1].split(" ") if s != '']
            elif l == '':
                continue
            elif l.endswith("map:"):
                current_translation = l.split(" ")[0]
                translations[current_translation] = {}
            else:
                numbers = [int(n) for n in l.split(" ") if n != '']
                translations[current_translation][(numbers[1], numbers[2])] = numbers[0]
    translations_needed = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location'
    ]
    for translation in translations_needed:
        for i, item in enumerate(seeds):
            for source, rnge in translations[translation].keys():
                if source <= item < source + rnge:
                    seeds[i] = translations[translation][(source, rnge)] + (item - source)

    return min(seeds)


def part_2_sad():
    with open("input.txt", "r") as f:
        translations = {}
        current_translation = ""
        for l in [line.rstrip('\n') for line in f.readlines()]:
            if l.startswith("seeds:"):
                seeds = []
                seedlist = [int(s) for s in l.split(":")[1].split(" ") if s != '']
                for i, number in tqdm(enumerate(seedlist)):
                    if i % 2 == 0:
                        for j in range(number, seedlist[i + 1] + number):
                            seeds.append(j)
            elif l == '':
                continue
            elif l.endswith("map:"):
                current_translation = l.split(" ")[0]
                translations[current_translation] = {}
            else:
                numbers = [int(n) for n in l.split(" ") if n != '']
                translations[current_translation][(numbers[1], numbers[2])] = numbers[0]
    print(len(seeds))
    translations_needed = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location'
    ]
    for translation in translations_needed:
        for i, item in tqdm(enumerate(seeds)):
            for source, rnge in translations[translation].keys():
                if source <= item < source + rnge:
                    seeds[i] = translations[translation][(source, rnge)] + (item - source)

    return min(seeds)


def part_2():
    with open("input.txt", "r") as f:
        translations = {}
        current_translation = ""
        for l in [line.rstrip('\n') for line in f.readlines()]:
            if l.startswith("seeds:"):
                seed_ranges = []
                seedlist = [int(s) for s in l.split(":")[1].split(" ") if s != '']
                for i, number in enumerate(seedlist):
                    if i % 2 == 0:
                        seed_ranges.append((number, seedlist[i + 1]))
            elif l == '':
                continue
            elif l.endswith("map:"):
                current_translation = l.split(" ")[0]
                translations[current_translation] = {}
            else:
                numbers = [int(n) for n in l.split(" ") if n != '']
                translations[current_translation][(numbers[1], numbers[2])] = numbers[0]
    translations_needed = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location'
    ]
    for translation in translations_needed:
        new_seed_ranges = []
        for s, sr in seed_ranges:
            transitions_applied = 0
            new_ranges = []
            new_ranges_no_translate = []
            for t, tr in translations[translation].keys():
                # Si la traducció xoca amb el seed range
                if t <= s and t + tr > s:
                    transitions_applied += 1
                    if t + tr < s + sr:
                        # 3,4, 1
                        # Esquerra anira de s traduida a t + tr
                        # Dreta de t + tr a s + sr
                        translated_s = translations[translation][(t, tr)] + (s - t)
                        left = (translated_s, t + tr - s)
                        right = (t + tr, s + sr - (t + tr))
                        new_ranges.append(left)
                        new_ranges_no_translate.append((s, t + tr - s))
                        new_ranges.append(right)
                        new_ranges_no_translate.append(right)
                    else:
                        # 6, 2
                        # Tot es un tros sencer de la mida de s
                        translated_s = translations[translation][(t, tr)] + (s - t)
                        new_ranges.append((translated_s, sr))
                        new_ranges_no_translate.append((s, sr))
                elif t > s and t < s + sr:
                    transitions_applied += 1
                    if t + tr < s + sr:
                        # 7
                        # Ha d'estar partit en 3
                        left = (s, t - s)
                        translated_t = translations[translation][(t, tr)]
                        middle = (translated_t, tr)
                        right = (t + tr, (s + sr) - (t + tr))
                        new_ranges.append(left)
                        new_ranges_no_translate.append(left)
                        new_ranges.append(middle)
                        new_ranges_no_translate.append((t, tr))
                        new_ranges.append(right)
                        new_ranges_no_translate.append(right)
                    else:
                        # 0, 5
                        # Esquerra anira de s a t
                        # Dreta anira de t traduit a s + sr
                        left = (s, t - s)
                        translated_t = translations[translation][(t, tr)]
                        right = (translated_t, s + sr - t)
                        new_ranges.append(left)
                        new_ranges_no_translate.append(left)
                        new_ranges.append(right)
                        new_ranges_no_translate.append((t, s + sr - t))
            if transitions_applied == 0:
                new_seed_ranges.append((s, sr))
            elif transitions_applied == 1:
                new_seed_ranges.extend(new_ranges)
            else:
                resorted = sorted(list(zip(new_ranges_no_translate, new_ranges)), key=lambda x: x[0][0])
                normal_ranges, final_ranges = zip(*resorted)
                print(normal_ranges)
                return None
        seed_ranges = new_seed_ranges
    print(sorted(seed_ranges, key=lambda x: x[0]))
    return sorted(seed_ranges, key=lambda x: x[0])[0][0]


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2_sad()).center(30))
    print("=" * 30)
