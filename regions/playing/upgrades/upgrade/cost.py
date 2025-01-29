from constants import *
from regions import Region
from utilities.parser import ValueType
from typing import Callable

class CostRegion(Region):
    x = 142
    y = 68
    width = 124
    height = 24

    def read(self, is_valid: Callable[[any], bool] = lambda _: True):
        return super().read(type = ValueType.COST, characters = "$1234567890", is_valid = is_valid)