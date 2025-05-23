from pathlib import Path
from PIL import Image
import numpy as np

from diceart.dices import DiceSet


def convert(img_path: Path):
    img = Image.open(img_path).convert("L")
    height = img.height
    width = img.width
    img_arr = np.array(img)
    dices = DiceSet()

    # recolor the image based on colors represented by dices
    def recolor(x: int):
        return dices.color_map[x]

    vreplace = np.vectorize(recolor)
    recolored = vreplace(img_arr)

    ds = dices.dice_size
    dice_img_arr = np.zeros((ds * height, ds * width))
    for i in range(height):
        for j in range(width):
            dice_img_arr[
                (ds * i) : (ds * (i + 1)),
                (ds * j) : (ds * (j + 1)),
            ] = dices.by_color[int(recolored[i, j])]
    dices_img = Image.fromarray(dice_img_arr).convert("L")
    return dices_img
