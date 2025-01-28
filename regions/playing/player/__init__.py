from constants import *
from regions import Region
from regions.playing.player.damage import DamageRegion
from regions.playing.player.health_regen import HealthRegenRegion
from regions.playing.player.healths import HealthsRegion

class PlayerRegion(Region):
    id = "playing.player"
    x = GAME_CENTER_X - 284 - 6
    y = 540
    width = 284
    height = 88

    damage = DamageRegion()
    health_regen = HealthRegenRegion()
    healths = HealthsRegion()