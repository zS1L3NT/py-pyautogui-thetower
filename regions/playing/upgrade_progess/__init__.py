from constants import *
from regions import Region
from regions.playing.upgrade_progess.level import Level

class UpgradeProgress(Region):
    id = "playing.upgrade_progress"
    x = GAME_CENTER_X - 125
    y = GAME_CENTER_Y - 10
    width = 250
    height = 75

    level = Level()