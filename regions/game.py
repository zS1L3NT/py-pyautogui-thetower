from constants import *
from regions import Region
from regions.home import HomeScreen
from regions.playing import PlayingScreen

class GameRegion(Region):
    x = GAME_X
    y = GAME_Y
    width = GAME_WIDTH
    height = GAME_HEIGHT

    home = HomeScreen()
    playing = PlayingScreen()