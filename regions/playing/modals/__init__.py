from constants import *
from region import Region
from .game_over import GameOverRegion
from .upgrade_progress import UpgradeProgressRegion
from .end_game import EndGameRegion
from .coin_bonus import CoinBonusRegion
from .ad_failed import AdFailedRegion

class ModalsRegion(Region):
    id = "playing.modals"
    width = GAME_WIDTH
    height = GAME_HEIGHT

    game_over = GameOverRegion()
    upgrade_progress = UpgradeProgressRegion()
    end_game = EndGameRegion()
    coin_bonus = CoinBonusRegion()
    ad_failed = AdFailedRegion()