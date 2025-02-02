from constants import *
from region import Region
from .left_reward_granted import LeftRewardGrantedRegion
from .right_reward_granted import RightRewardGrantedRegion
from .right_close_button import RightCloseButtonRegion

class AdRegion(Region):
    id = "ad"
    width = GAME_WIDTH
    height = GAME_HEIGHT

    left_reward_granted = LeftRewardGrantedRegion()
    right_reward_granted = RightRewardGrantedRegion()
    right_close_button = RightCloseButtonRegion()