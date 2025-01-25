from constants import *
from regions import Region

class Category(Region):
    width = 192
    height = 54

    def __init__(self, index):
        self.id = "playing.categories." + ["attack", "defence", "utility"][index]
        self.x = (self.width + 4) * index
        self.image = __file__.replace("category.py", ["attack", "defence", "utility"][index] + ".png")