from regions import Region

class ButtonRegion(Region):
    id = "playing.menu.toggle"
    width = 54
    height = 54

    def __init__(self, index: int):
        self.x = 8 + ((index % 2) * (self.width + 4))
        self.y = 8 + ((index // 2) * (self.height + 4))

        if index >= 2:
            self.y -= 2