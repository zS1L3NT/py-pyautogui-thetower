from constants import *
from regions import Region
from regions.playing.upgrade_border.multiplier_one import MultiplierOneRegion
from regions.playing.upgrade_border.multipliers import MultipliersRegion
from regions.playing.upgrade_border.title import TitleRegion

class UpgradeBorderRegion(Region):
    id = "playing.upgrade_border"
    x = 0
    y = 632
    width = GAME_WIDTH
    height = 52

    title = TitleRegion()
    multipliers = MultipliersRegion()
    multiplier_one = MultiplierOneRegion()