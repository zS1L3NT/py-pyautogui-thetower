from engine.game.data.cleaner import Cleaner

class Resources:
    cash = 0
    coins = 0
    gems = 0

    def __setattr__(self, name, value):
        number = Cleaner(value).number()
        if not number: return
        super().__setattr__(name, number)

    def __str__(self):
        return f"{{\n    cash: {self.cash}\n    coins: {self.coins}\n    gems: {self.gems}\n  }}"