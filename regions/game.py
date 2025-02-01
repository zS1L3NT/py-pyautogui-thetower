from constants import *
from region import Region
from regions.playing import PlayingRegion
from regions.ad import AdRegion
from regions.ad_claimed import AdClaimedRegion

class GameRegion(Region):
    id = "game"
    x = GAME_X
    y = GAME_Y
    width = GAME_WIDTH
    height = GAME_HEIGHT

    playing = PlayingRegion()
    ad = AdRegion()
    ad_claimed = AdClaimedRegion()

region = GameRegion()
region.cascade()