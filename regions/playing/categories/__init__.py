from constants import *
from regions import Region
from regions.playing.categories.category import Category

class Categories(Region):
    id = "playing.categories"
    x = 2
    y = GAME_HEIGHT - 54
    width = 584
    height = 54

    attack = Category(0, 13)
    defence = Category(1, 15)
    utility = Category(2, 11)