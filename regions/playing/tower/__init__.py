from constants import *
from regions import Region
from regions.playing.tower.gem_point import GemPointRegion

class TowerRegion(Region):
    id = "playing.tower"
    x = 200
    y = 62
    width = 386
    height = 386

    gem_point_top = GemPointRegion(0)
    gem_point_right = GemPointRegion(1)
    gem_point_bottom = GemPointRegion(2)
    gem_point_left = GemPointRegion(3)

    gem_points = (gem_point_top, gem_point_right, gem_point_bottom, gem_point_left)