from constants import *
from regions import Region
from regions.playing.resources.cash import CashRegion
from regions.playing.resources.coins import CoinsRegion
from regions.playing.resources.gems import GemsRegion

class ResourcesRegion(Region):
    id = "playing.resources"
    x = 0
    y = 10
    width = 180
    height = 140

    cash = CashRegion()
    coins = CoinsRegion()
    gems = GemsRegion()