from constants import *
from regions import Region
from regions.playing.enemies.wave import WaveRegion
from regions.playing.enemies.damage import DamageRegion
from regions.playing.enemies.health import HealthRegion

class EnemiesRegion(Region):
    id = "playing.enemies"
    x = GAME_CENTER_X + 2
    y = 540
    width = 284
    height = 88

    wave = WaveRegion()
    damage = DamageRegion()
    health = HealthRegion()