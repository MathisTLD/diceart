from pathlib import Path
from PIL import Image
import pytest
from testutils.paths import TESTS_DIR

from diceart.convert import convert
from diceart.dices import DICE_SIZE

TEST_DATA_DIR = TESTS_DIR / "data"


@pytest.mark.parametrize(
    "img_path",
    [
        TEST_DATA_DIR / "robert_smith-1.jpg",
        TEST_DATA_DIR / "robert_smith-2-1.jpg",
        TEST_DATA_DIR / "robert_smith-2-2.jpg",
        TEST_DATA_DIR / "ian_curtis.jpg",
    ],
)
def test_convert(img_path: Path):
    img = convert(img_path)
    # use PNG to avoid compression
    img.save(img_path.with_suffix(".diceart.png"))
    base_img = Image.open(img_path)
    assert img.width == (base_img.width * DICE_SIZE)
    assert img.height == (base_img.height * DICE_SIZE)
