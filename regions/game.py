from constants import *
from regions import Region
from regions.home import HomeRegion
from regions.playing import PlayingRegion
from regions.ad import AdRegion
from regions.ad_claimed import AdClaimedRegion

class GameRegion(Region):
    id = "game"
    x = GAME_X
    y = GAME_Y
    width = GAME_WIDTH
    height = GAME_HEIGHT

    home = HomeRegion()
    playing = PlayingRegion()
    ad = AdRegion()
    ad_claimed = AdClaimedRegion()