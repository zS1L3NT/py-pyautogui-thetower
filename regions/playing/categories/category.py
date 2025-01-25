from constants import *
from regions import Region

class Category(Region):
    width = 192
    height = 54
    upgrades = 0

    def __init__(self, index, upgrades):
        self.id = "playing.categories." + ["attack", "defence", "utility"][index]
        self.x = (self.width + 4) * index
        self.upgrades = upgrades
        self.image = __file__.replace("category.py", ["attack", "defence", "utility"][index] + ".png")