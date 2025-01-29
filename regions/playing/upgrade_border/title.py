from regions import Region
from utilities.parser import ValueType

class TitleRegion(Region):
    id = "playing.upgrade_border.title"
    x = 100
    y = 0
    width = 300
    height = 52

    def read(self):
        return super().read(
            type = ValueType.STRING,
            retries = 3,
            is_valid = lambda value: value in ["ATTACK UPGRADES", "DEFENCE UPGRADES", "UTILITY UPGRADES"]
        )