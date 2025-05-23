import numpy as np
import pytest
from diceart.dices import gen_dice, gen_dices


@pytest.mark.parametrize("dice_id", [0, 7, -9])
def test_gen_dice_invalid(dice_id: int):
    with pytest.raises(AssertionError):
        gen_dice(dice_id)


def test_gen_dice():
    dice = gen_dice(-5)
    assert (
        dice
        == np.array(
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 255, 0, 0, 0, 255, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 255, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 255, 0, 0, 0, 255, 0],
                [0, 0, 0, 0, 0, 0, 0],
            ]
        )
    ).all()
    dice = gen_dice(3)
    assert (
        dice
        == np.array(
            [
                [255, 255, 255, 255, 255, 255, 255],
                [255, 0, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 0, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 0, 255],
                [255, 255, 255, 255, 255, 255, 255],
            ]
        )
    ).all()


def test_gen_dices():
    all_dices = gen_dices()
    assert len(all_dices) == 12
    assert (
        all_dices[-1]
        == np.array(
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 255, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
            ]
        )
    ).all()
