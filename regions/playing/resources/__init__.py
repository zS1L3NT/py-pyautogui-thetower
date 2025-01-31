from constants import *
from region import Region
from .cash import CashRegion
from .coins import CoinsRegion
from .gems import GemsRegion

class ResourcesRegion(Region):
    id = "playing.resources"
    x = 0
    y = 10
    width = 180
    height = 140

    cash = CashRegion()
    coins = CoinsRegion()
    gems = GemsRegion()