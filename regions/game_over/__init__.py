from constants import *
from regions import Region
from regions.game_over.retry_button import RetryButton

class GameOverScreen(Region):
    id = "game_over"
    x = 120
    y = 210
    width = 542
    height = 632

    retry_button = RetryButton()