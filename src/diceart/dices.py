import numpy as np

DICE_SIZE = 7

PATTERNS = {
    1: np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ),
    2: np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ),
    3: np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ),
    4: np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ),
    5: np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ),
    6: np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ),
}


def gen_dice(id: int):
    """id in [-6,6] (0 excluded). Negative numbers means black background"""
    black_bg = id < 0
    number = abs(id)
    assert 1 <= number <= 6, f"Invalid number {number}"
    pattern = PATTERNS[number]
    if black_bg:
        return 255 * pattern
    else:
        return (-255 * pattern) + 255


def gen_dices():
    """Generates every possible dice as 8-bit array. Returns a map with dice's id as key"""
    dices = dict[int, np.ndarray]()
    for n in range(1, 7):
        for k in (-1, 1):
            dice_id = n * k
            dices[dice_id] = gen_dice(dice_id)
    return dices


def gen_color_map(available_colors: np.ndarray):
    """Generates a mapping between colors and nearest represented color

    available_colors is expected to be a sorted (asc) array of uint8"""
    c_map = np.zeros((256,), dtype=np.uint8)
    available_colors.sort()
    borders = [
        round(available_colors[i : i + 2].mean())
        for i in range(len(available_colors) - 1)
    ] + [256]
    a = 0
    for i in range(len(available_colors)):
        b = borders[i]
        color = available_colors[i]
        for k in range(a, b):
            c_map[k] = color
        a = b
    return c_map


class DiceSet:
    dice_size = DICE_SIZE

    def __init__(self):
        self.by_id = gen_dices()
        self.by_color = dict((round(dice.mean()), dice) for dice in self.by_id.values())
        self.available_colors = np.array(list(self.by_color.keys()), dtype=np.uint8)
        self.available_colors.sort()
        self.color_map = gen_color_map(self.available_colors)
