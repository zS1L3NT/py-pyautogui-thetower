from constants import *
from region import Region
from .game_over import GameOverRegion
from .upgrade_progress import UpgradeProgressRegion
from .end_game import EndGameRegion
from .coin_bonus import CoinBonusRegion

class ModalsRegion(Region):
    width = GAME_WIDTH
    height = GAME_HEIGHT

    game_over = GameOverRegion()
    upgrade_progress = UpgradeProgressRegion()
    end_game = EndGameRegion()
    coin_bonus = CoinBonusRegion()