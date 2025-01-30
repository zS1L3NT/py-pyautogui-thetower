from constants import *
from regions import Region
from regions.ad.left_close_button import LeftCloseButtonRegion
from regions.ad.right_close_button import RightCloseButtonRegion

class AdRegion(Region):
    width = GAME_WIDTH
    height = GAME_HEIGHT

    left_close_button = LeftCloseButtonRegion()
    right_close_button = RightCloseButtonRegion()