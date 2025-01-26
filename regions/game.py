from constants import *
from regions import Region
from regions.home import HomeScreen
from regions.playing import PlayingScreen
from regions.game_over import GameOverScreen

class GameRegion(Region):
    x = GAME_X
    y = GAME_Y
    width = GAME_WIDTH
    height = GAME_HEIGHT

    home = HomeScreen()
    playing = PlayingScreen()
    game_over = GameOverScreen()