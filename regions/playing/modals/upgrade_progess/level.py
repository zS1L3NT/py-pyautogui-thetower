from typing import Callable
from constants import *
from regions import Region

class LevelRegion(Region):
    id = "playing.upgrade_progress.level"
    x = 168
    y = 6
    width = 60
    height = 24

    def read(self, is_valid: Callable[[any], bool] = lambda _: True):
        return super().read(process_image = False, characters = "1234567890", is_valid = is_valid)