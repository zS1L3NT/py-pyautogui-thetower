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

    def click(self):
        self.value.click()