from dataclasses import dataclass

from tqdm import tqdm


@dataclass
class BeamPosition:
    rowc: int
    colc: int
    direction: str


def calculate_energized(mapa, start_beam):
    beams = [start_beam]
    visited_beams = []
    energized_tiles = []
    while len(beams) > 0:
        beam = beams.pop(0)
        visited_beams.append(beam)
        if (beam.rowc, beam.colc) not in energized_tiles:
            energized_tiles.append((beam.rowc, beam.colc))
        if mapa[beam.rowc][beam.colc] == '.':
            # Continua igual depen de la direccio
            if beam.direction == 'up':
                if beam.rowc > 0:
                    new_beam = BeamPosition(beam.rowc - 1, beam.colc, 'up')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'down':
                if beam.rowc < len(mapa) - 1:
                    new_beam = BeamPosition(beam.rowc + 1, beam.colc, 'down')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'left':
                if beam.colc > 0:
                    new_beam = BeamPosition(beam.rowc, beam.colc - 1, 'left')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'right':
                if beam.colc < len(mapa[beam.rowc]) - 1:
                    new_beam = BeamPosition(beam.rowc, beam.colc + 1, 'right')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
        elif mapa[beam.rowc][beam.colc] == '/':
            if beam.direction == 'up':
                if beam.colc < len(mapa[beam.rowc]) - 1:
                    new_beam = BeamPosition(beam.rowc, beam.colc + 1, 'right')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'down':
                if beam.colc > 0:
                    new_beam = BeamPosition(beam.rowc, beam.colc - 1, 'left')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'left':
                if beam.rowc < len(mapa) - 1:
                    new_beam = BeamPosition(beam.rowc + 1, beam.colc, 'down')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'right':
                if beam.rowc > 0:
                    new_beam = BeamPosition(beam.rowc - 1, beam.colc, 'up')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
        elif mapa[beam.rowc][beam.colc] == '\\':
            if beam.direction == 'up':
                if beam.colc > 0:
                    new_beam = BeamPosition(beam.rowc, beam.colc - 1, 'left')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'down':
                if beam.colc < len(mapa[beam.rowc]) - 1:
                    new_beam = BeamPosition(beam.rowc, beam.colc + 1, 'right')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'left':
                if beam.rowc > 0:
                    new_beam = BeamPosition(beam.rowc - 1, beam.colc, 'up')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'right':
                if beam.rowc < len(mapa) - 1:
                    new_beam = BeamPosition(beam.rowc + 1, beam.colc, 'down')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
        elif mapa[beam.rowc][beam.colc] == "|":
            if beam.direction == 'up':
                if beam.rowc > 0:
                    new_beam = BeamPosition(beam.rowc - 1, beam.colc, 'up')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'down':
                if beam.rowc < len(mapa) - 1:
                    new_beam = BeamPosition(beam.rowc + 1, beam.colc, 'down')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'left' or beam.direction == 'right':
                if beam.rowc > 0:
                    new_beam = BeamPosition(beam.rowc - 1, beam.colc, 'up')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
                if beam.rowc < len(mapa) - 1:
                    new_beam = BeamPosition(beam.rowc + 1, beam.colc, 'down')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
        elif mapa[beam.rowc][beam.colc] == "-":
            if beam.direction == 'up' or beam.direction == 'down':
                if beam.colc > 0:
                    new_beam = BeamPosition(beam.rowc, beam.colc - 1, 'left')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
                if beam.colc < len(mapa[beam.rowc]) - 1:
                    new_beam = BeamPosition(beam.rowc, beam.colc + 1, 'right')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'left':
                if beam.colc > 0:
                    new_beam = BeamPosition(beam.rowc, beam.colc - 1, 'left')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)
            elif beam.direction == 'right':
                if beam.colc < len(mapa[beam.rowc]) - 1:
                    new_beam = BeamPosition(beam.rowc, beam.colc + 1, 'right')
                    if new_beam not in beams and new_beam not in visited_beams:
                        beams.append(new_beam)

    return len(energized_tiles)


def part_1():
    with open("input.txt", "r") as f:
        mapa = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            mapa.append([c for c in l])
    return calculate_energized(mapa, BeamPosition(0, 0, 'right'))


def part_2():
    with open("input.txt", "r") as f:
        mapa = []
        for l in [line.rstrip('\n') for line in f.readlines()]:
            mapa.append([c for c in l])
    start_beams = []
    for i, elem in enumerate(mapa[0]):
        start_beams.append(BeamPosition(0, i, 'down'))
    for i, elem in enumerate(mapa[len(mapa) - 1]):
        start_beams.append(BeamPosition(len(mapa) - 1, i, 'up'))
    for rowc, row in enumerate(mapa):
        start_beams.append(BeamPosition(rowc, 0, 'right'))
        start_beams.append(BeamPosition(rowc, len(row) - 1, 'left'))
    max_tiles = 0
    for beam in tqdm(start_beams):
        max_tiles = max(max_tiles, calculate_energized(mapa, beam))
    return max_tiles


if __name__ in "__main__":
    print("PART 1:".center(30, "="))
    print(str(part_1()).center(30))
    print("=" * 30)
    print("PART 2:".center(30, "="))
    print(str(part_2()).center(30))
    print("=" * 30)
