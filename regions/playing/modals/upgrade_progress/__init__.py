from constants import *
from region import Region
from .level import LevelRegion

class UpgradeProgressRegion(Region):
    id = "playing.upgrade_progress"
    x = GAME_CENTER_X - 125
    y = GAME_CENTER_Y - 10
    width = 250
    height = 75

    level = LevelRegion()