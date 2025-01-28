from constants import *
from regions import Region
from regions.playing.resources import ResourcesRegion
from regions.playing.player import PlayerRegion
from regions.playing.enemies import EnemiesRegion
from regions.playing.upgrades import UpgradesRegion
from regions.playing.categories import CategoriesRegion
from regions.playing.upgrade_progess import UpgradeProgressRegion

class PlayingRegion(Region):
    width = GAME_WIDTH
    height = GAME_HEIGHT

    resources = ResourcesRegion()
    player = PlayerRegion()
    enemies = EnemiesRegion()
    upgrades = UpgradesRegion()
    categories = CategoriesRegion()
    upgrade_progress = UpgradeProgressRegion()