from engine.game.data.cleaner import Cleaner

class Player:
    damage = 0
    health = 0
    max_health = 0
    health_regen = 0

    def __setattr__(self, name, value):
        if name == "damage":
            number = Cleaner(value).number()
            if not number: return
            super().__setattr__(name, number)
        elif name == "healths":
            numbers = Cleaner(value).number_slash_number()
            if not numbers: return
            super().__setattr__("health", numbers[0])
            super().__setattr__("max_health", numbers[1])
        elif name == "health_regen":
            number = Cleaner(value).number_slash_s()
            if not number: return
            super().__setattr__(name, number)

    def __str__(self):
        return f"{{\n    damage: {self.damage}\n    health: {self.health}\n    max_health: {self.max_health}\n    health_regen: {self.health_regen}\n  }}"