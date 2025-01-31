class Data:
    wave: int
    attack: list[bool]
    defence: list[bool]
    utility: list[bool]

    categories: tuple[list[bool], list[bool], list[bool]]

    def __init__(self):
        self.reset()

    def reset(self):
        self.wave = 0

        self.attack = [False] * 13
        self.defence = [False] * 15
        self.utility = [False] * 11

        self.attack[7] = True
        self.attack[11] = True
        self.defence[1] = True
        self.defence[3] = True
        self.utility[7] = True

        self.categories = (self.attack, self.defence, self.utility)

data = Data()