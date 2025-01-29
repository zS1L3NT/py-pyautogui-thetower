from constants import *
from regions import Region
from utilities.parser import ValueType

class NameRegion(Region):
    x = 8
    y = 24
    width = 132
    height = 60

    def read(self):
        return super().read(ValueType.STRING)