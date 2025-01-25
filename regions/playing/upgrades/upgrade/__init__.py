from constants import *
from regions import Region
from regions.playing.upgrades.upgrade.name import Name
from regions.playing.upgrades.upgrade.value import Value
from regions.playing.upgrades.upgrade.cost import Cost

class Upgrade(Region):
    width = 276
    height = 108

    name: Name
    value: Value
    cost: Cost

    def __init__(self, index):
        self.name = Name()
        self.value = Value()
        self.cost = Cost()

        if index % 2 == 0:
            self.x = 0
        else:
            self.x = self.width + 8

        match index // 2:
            case 0:
                self.y = 0
            case 1:
                self.y = self.height + 8
            case 2:
                self.y = 308 - self.height - 10