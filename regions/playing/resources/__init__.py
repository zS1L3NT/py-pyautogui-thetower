from constants import *
from regions import Region
from regions.playing.resources.cash import Cash
from regions.playing.resources.coins import Coins
from regions.playing.resources.gems import Gems

class Resources(Region):
    id = "playing.resources"
    x = 0
    y = 10
    width = 180
    height = 140

    cash = Cash()
    coins = Coins()
    gems = Gems()