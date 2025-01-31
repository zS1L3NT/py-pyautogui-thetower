from constants import *
from region import Region
from utilities.parser import ValueType

class HealthsRegion(Region):
    id = "playing.player.healths"
    x = 12
    y = 42
    width = 260
    height = 32

    def read(self):
        return super().read(ValueType.NUMBER_SLASH_NUMBER)