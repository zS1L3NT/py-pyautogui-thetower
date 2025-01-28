class EnemiesData:
    wave = 0
    damage = 0
    health = 0

    def __setattr__(self, name, value):
        if value is not None:
            super().__setattr__(name, value)

    def __str__(self):
        return f"{{\n    wave: {self.wave}\n    damage: {self.damage}\n    health: {self.health}\n  }}"