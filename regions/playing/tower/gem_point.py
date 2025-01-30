from regions import Region


class GemPointRegion(Region):
    id = "playing.tower.gem_point"
    width = 96
    height = 96

    def __init__(self, index: int):
        if index == 0:
            self.x = 145
            self.y = 49
        elif index == 1:
            self.x = 242
            self.y = 145
        elif index == 2:
            self.x = 145
            self.y = 242
        elif index == 3:
            self.x = 49
            self.y = 145
