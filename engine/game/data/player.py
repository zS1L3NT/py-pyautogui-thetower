from utilities.parser import Parser

class Player:
    damage = 0
    health = 0
    max_health = 0
    health_regen = 0

    def __setattr__(self, name, value):
        if name == "damage":
            number = Parser(value).number()
            if not number:
                raise ValueError(f"Failed to parse {name} value: {value}")    

            super().__setattr__(name, number)
        elif name == "healths":
            numbers = Parser(value).number_slash_number()
            if not numbers:
                raise ValueError(f"Failed to parse healths value: {value}")    

            super().__setattr__("health", numbers[0])
            super().__setattr__("max_health", numbers[1])
        elif name == "health_regen":
            number = Parser(value).per_second()
            if not number:
                raise ValueError(f"Failed to parse {name} value: {value}")    

            super().__setattr__(name, number)

    def __str__(self):
        return f"{{\n    damage: {self.damage}\n    health: {self.health}\n    max_health: {self.max_health}\n    health_regen: {self.health_regen}\n  }}"