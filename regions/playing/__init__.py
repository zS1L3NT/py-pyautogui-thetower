from constants import *
from regions import Region
from regions.playing.resources import ResourcesRegion
from regions.playing.ad_coin_bonus import AdCoinBonusRegion
from regions.playing.menu import MenuRegion
from regions.playing.ad_gems import AdGemsRegion
from regions.playing.tower import TowerRegion
from regions.playing.player import PlayerRegion
from regions.playing.enemies import EnemiesRegion
from regions.playing.upgrade_border import UpgradeBorderRegion
from regions.playing.upgrades import UpgradesRegion
from regions.playing.categories import CategoriesRegion
from regions.playing.modals.game_over import GameOverRegion
from regions.playing.modals.upgrade_progess import UpgradeProgressRegion
from regions.playing.modals.end_game import EndGameRegion
from regions.playing.modals.coin_bonus import CoinBonusRegion

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

    game_over_modal = GameOverRegion()
    upgrade_progress_modal = UpgradeProgressRegion()
    end_game_modal = EndGameRegion()
    coin_bonus_modal = CoinBonusRegion()