from constants import *
from regions import Region

class RetryButton(Region):
    id = "game_over.retry_button"
    x = 18
    y = 540
    width = 240
    height = 76
    image = __file__.replace(".py", ".png")