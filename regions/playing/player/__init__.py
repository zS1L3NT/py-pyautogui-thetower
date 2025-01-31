from constants import *
from region import Region
from .damage import DamageRegion
from .health_regen import HealthRegenRegion
from .healths import HealthsRegion

class PlayerRegion(Region):
    id = "playing.player"
    x = GAME_CENTER_X - 284 - 6
    y = 540
    width = 284
    height = 88

    damage = DamageRegion()
    health_regen = HealthRegenRegion()
    healths = HealthsRegion()