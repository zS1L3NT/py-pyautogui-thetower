from constants import *
from regions import Region
from regions.playing.player.damage import Damage
from regions.playing.player.health_regen import HealthRegen
from regions.playing.player.healths import Healths

class Player(Region):
    id = "playing.player"
    x = GAME_CENTER_X - 284 - 6
    y = 540
    width = 284
    height = 88

    damage = Damage()
    health_regen = HealthRegen()
    healths = Healths()