from region import Region
from .close_button import CloseButtonRegion

class RightRewardGrantedRegion(Region):
    id = "ad.right_reward_granted"
    x = 656
    y = 4
    width = 128
    height = 32

    close_button = CloseButtonRegion()