from constants import *
from region import Region

class RetryButtonRegion(Region):
    id = "playing.modals.game_over.retry_button"
    x = 18
    y = 540
    width = 240
    height = 76
    image = __file__.replace(".py", ".png")