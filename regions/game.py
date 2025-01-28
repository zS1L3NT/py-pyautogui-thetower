from constants import *
from regions import Region
from regions.home import HomeRegion
from regions.playing import PlayingRegion
from regions.game_over import GameOverRegion

class GameRegion(Region):
    id = "game"
    x = GAME_X
    y = GAME_Y
    width = GAME_WIDTH
    height = GAME_HEIGHT

    home = HomeRegion()
    playing = PlayingRegion()
    game_over = GameOverRegion()