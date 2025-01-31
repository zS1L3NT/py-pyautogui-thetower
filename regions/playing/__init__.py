from constants import *
from region import Region
from .resources import ResourcesRegion
from .ad_coin_bonus import AdCoinBonusRegion
from .menu import MenuRegion
from .ad_gems import AdGemsRegion
from .tower import TowerRegion
from .player import PlayerRegion
from .enemies import EnemiesRegion
from .upgrade_border import UpgradeBorderRegion
from .upgrades import UpgradesRegion
from .categories import CategoriesRegion
from .modals import ModalsRegion

class PlayingRegion(Region):
    width = GAME_WIDTH
    height = GAME_HEIGHT

    resources = ResourcesRegion()
    ad_coin_bonus = AdCoinBonusRegion()
    menu = MenuRegion()
    ad_gems = AdGemsRegion()
    tower = TowerRegion()
    player = PlayerRegion()
    enemies = EnemiesRegion()
    upgrade_border = UpgradeBorderRegion()
    upgrades = UpgradesRegion()
    categories = CategoriesRegion()

    modals = ModalsRegion()