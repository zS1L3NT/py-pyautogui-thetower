from constants import *
from region import Region
from .multiplier_one import MultiplierOneRegion
from .multipliers import MultipliersRegion
from .title import TitleRegion

class UpgradeBorderRegion(Region):
    id = "playing.upgrade_border"
    x = 0
    y = 632
    width = GAME_WIDTH
    height = 52

    title = TitleRegion()
    multipliers = MultipliersRegion()
    multiplier_one = MultiplierOneRegion()