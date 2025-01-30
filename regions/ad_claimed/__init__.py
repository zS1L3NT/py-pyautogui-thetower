from constants import *
from regions import Region
from regions.ad_claimed.claim_button import ClaimButtonRegion

class AdClaimedRegion(Region):
    width = GAME_WIDTH
    height = GAME_HEIGHT

    claim_button = ClaimButtonRegion()