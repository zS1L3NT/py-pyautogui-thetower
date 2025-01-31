from constants import *
from region import Region
from .retry_button import RetryButtonRegion
from .home_button import HomeButtonRegion

class GameOverRegion(Region):
    id = "playing.modals.game_over"
    x = 120
    y = 210
    width = 542
    height = 632

    retry_button = RetryButtonRegion()
    home_button = HomeButtonRegion()

    def is_present(self):
        return self.retry_button.is_present() or self.home_button.is_present()