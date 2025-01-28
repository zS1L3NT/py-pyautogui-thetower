from utilities.parser import Parser

class Enemies:
    wave = 0
    damage = 0
    health = 0

    def __setattr__(self, name, value):
        number = Parser(value).number()
        if not number:
            raise ValueError(f"Failed to parse {name} value: {value}")    

        super().__setattr__(name, number)

    def __str__(self):
        return f"{{\n    wave: {self.wave}\n    damage: {self.damage}\n    health: {self.health}\n  }}"