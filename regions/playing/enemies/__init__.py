from constants import *
from regions import Region
from regions.playing.enemies.wave import Wave
from regions.playing.enemies.damage import Damage
from regions.playing.enemies.health import Health

class Enemies(Region):
    id = "playing.enemies"
    x = GAME_CENTER_X + 2
    y = 540
    width = 284
    height = 88

    wave = Wave()
    damage = Damage()
    health = Health()