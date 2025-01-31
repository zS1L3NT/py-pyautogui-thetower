from constants import *
from region import Region
from .name import NameRegion
from .value import ValueRegion
from .cost import CostRegion

class UpgradeRegion(Region):
    id = "playing.upgrades.upgrade"
    width = 276
    height = 108

    name: NameRegion
    value: ValueRegion
    cost: CostRegion

    def __init__(self, index):
        self.name = NameRegion()
        self.value = ValueRegion()
        self.cost = CostRegion()

        if index % 2 == 0:
            self.x = 0
            self.id = "left"
        else:
            self.x = self.width + 8
            self.id = "right"

        match index // 2:
            case 0:
                self.y = 0
                self.id = f"first_{self.id}"
            case 1:
                self.y = self.height + 8
                self.id = f"second_{self.id}"
            case 2:
                self.y = 308 - self.height - 10
                self.id = f"last_{self.id}"

        self.id = f"playing.upgrades.{self.id}"