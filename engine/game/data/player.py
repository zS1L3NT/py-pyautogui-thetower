class Player:
    damage = 0
    health = 0
    max_health = 0
    health_regen = 0

    def __setattr__(self, name, value):
        if value is not None:
            super().__setattr__(name, value)

    def __str__(self):
        return f"{{\n    damage: {self.damage}\n    health: {self.health}\n    max_health: {self.max_health}\n    health_regen: {self.health_regen}\n  }}"