from constants import *
from region import Region
from .claim_button import ClaimButtonRegion

class AdClaimedRegion(Region):
    width = GAME_WIDTH
    height = GAME_HEIGHT

    claim_button = ClaimButtonRegion()