from constants import *
from region import Region
from utilities.parser import ValueType

class HealthRegenRegion(Region):
    id = "playing.player.health_regen"
    x = 120
    y = 9
    width = 80
    height = 24

    def read(self):
        return super().read(ValueType.PER_SECOND)