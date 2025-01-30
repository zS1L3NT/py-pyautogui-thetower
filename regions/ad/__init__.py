from constants import *
from regions import Region
from regions.ad.close_button import CloseButtonRegion

class AdRegion(Region):
    width = GAME_WIDTH
    height = GAME_HEIGHT

    left_close_button = CloseButtonRegion(0)