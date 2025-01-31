from constants import *
from region import Region
from .wave import WaveRegion
from .damage import DamageRegion
from .health import HealthRegion

class EnemiesRegion(Region):
    id = "playing.enemies"
    x = GAME_CENTER_X + 2
    y = 540
    width = 284
    height = 88

    wave = WaveRegion()
    damage = DamageRegion()
    health = HealthRegion()