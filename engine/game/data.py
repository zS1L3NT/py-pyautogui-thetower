class GameData:
    wave = 0
    attack = [False] * 13
    defence = [False] * 15
    utility = [False] * 11

    categories = (attack, defence, utility)

    def __init__(self):
        self.attack[7] = True
        self.attack[11] = True
        self.defence[1] = True
        self.defence[3] = True
        self.utility[7] = True