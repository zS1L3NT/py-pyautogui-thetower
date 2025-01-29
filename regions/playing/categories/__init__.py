from constants import *
from regions import Region
from regions.playing.categories.category import CategoryRegion

class CategoriesRegion(Region):
    id = "playing.categories"
    x = 2
    y = GAME_HEIGHT - 54
    width = 584
    height = 54

    attack = CategoryRegion(0)
    defence = CategoryRegion(1)
    utility = CategoryRegion(2)

    all = [attack, defence, utility]