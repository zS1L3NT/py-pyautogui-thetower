from constants import *
from regions import Region
from regions.game_over.retry_button import RetryButtonRegion

class GameOverRegion(Region):
    id = "game_over"
    x = 120
    y = 210
    width = 542
    height = 632

    retry_button = RetryButtonRegion()