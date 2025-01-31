from constants import *
from region import Region

class HomeButtonRegion(Region):
    id = "playing.modals.game_over.home_button"
    x = 284
    y = 540
    width = 240
    height = 76
    image = __file__.replace(".py", ".png")