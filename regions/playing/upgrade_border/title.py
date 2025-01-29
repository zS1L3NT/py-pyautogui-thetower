from regions import Region
from utilities.parser import ValueType

class TitleRegion(Region):
    id = "playing.upgrade_border.title"
    x = 100
    y = 0
    width = 300
    height = 52

    def read(self):
        return super().read(ValueType.custom(r"(ATTACK|DEFENCE|UTILITY) UPGRADES"), retries = 3)