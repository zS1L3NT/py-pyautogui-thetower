from regions import Region

class CloseButtonRegion(Region):
    y = 13
    width = 30
    height = 30

    def __init__(self, index: int):
        if index == 0:
            self.x = 11