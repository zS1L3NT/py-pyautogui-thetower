from engine.game.data.cleaner import Cleaner

class Enemies:
    wave = 0
    damage = 0
    health = 0

    def __setattr__(self, name, value):
        number = Cleaner(value).number()
        if not number: return
        super().__setattr__(name, number)

    def __str__(self):
        return f"{{\n    wave: {self.wave}\n    damage: {self.damage}\n    health: {self.health}\n  }}"