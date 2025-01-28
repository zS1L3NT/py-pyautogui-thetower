from utilities.parser import Parser

class Resources:
    cash = 0
    coins = 0
    gems = 0

    def __setattr__(self, name, value):
        number = Parser(value).number()
        if not number:
            raise ValueError(f"Failed to parse {name} value: {value}")
            
        super().__setattr__(name, number)

    def __str__(self):
        return f"{{\n    cash: {self.cash}\n    coins: {self.coins}\n    gems: {self.gems}\n  }}"