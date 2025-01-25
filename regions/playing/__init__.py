from constants import *
from regions import Region
from regions.playing.resources import Resources
from regions.playing.player import Player
from regions.playing.enemies import Enemies
from regions.playing.upgrades import Upgrades
from regions.playing.categories import Categories
from regions.playing.upgrade_progess import UpgradeProgress

class PlayingScreen(Region):
    width = GAME_WIDTH
    height = GAME_HEIGHT

    resources = Resources()
    player = Player()
    enemies = Enemies()
    upgrades = Upgrades()
    categories = Categories()
    upgrade_progress = UpgradeProgress()