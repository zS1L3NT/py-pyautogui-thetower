from constants import *
from region import Region
from .left_close_area import LeftCloseArea
from .left_close_button import LeftCloseButtonRegion
from .right_close_button import RightCloseButtonRegion

class AdRegion(Region):
    id = "ad"
    width = GAME_WIDTH
    height = GAME_HEIGHT

    left_close_area = LeftCloseArea()
    left_close_button = LeftCloseButtonRegion()
    right_close_button = RightCloseButtonRegion()