from region import Region
from .close_button import CloseButtonRegion

class LeftRewardGrantedRegion(Region):
    id = "ad.left_reward_granted"
    x = 0
    y = 0
    width = 162
    height = 56

    close_button = CloseButtonRegion()