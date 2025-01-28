from utilities.parser import Parser, ValueType

class Upgrade:
    id = ""
    category = ""

    type: ValueType
    value = float('-inf')
    cost = float('-inf')
    level = float('-inf')
    max_level = float('-inf')

    def __init__(self, max_level: int):
        self.max_level = max_level

    def __setattr__(self, name, value):
        if name == "cost":
            value = Parser(value).cost()
        elif name == "level":
            value = Parser(value).number()
        elif name == "value":
            value = Parser(value).type(self.type)

        if value is None:
            raise ValueError(f"Failed to parse {name} value: {value}")    

        super().__setattr__(name, value)

    def __str__(self):
        return f"{self.id}: {self.value}, ${self.cost} [{self.level} / {self.max_level}]"

    def number(max_level: int):
        upgrade = Upgrade(max_level)
        upgrade.type = ValueType.NUMBER
        return upgrade
    
    def percentage(max_level: int):
        upgrade = Upgrade(max_level)
        upgrade.type = ValueType.PERCENTAGE
        return upgrade
    
    def multiplier(max_level: int):
        upgrade = Upgrade(max_level)
        upgrade.type = ValueType.MULTIPLIER
        return upgrade
    
    def distance(max_level: int):
        upgrade = Upgrade(max_level)
        upgrade.type = ValueType.DISTANCE
        return upgrade
    
    def duration(max_level: int):
        upgrade = Upgrade(max_level)
        upgrade.type = ValueType.DURATION
        return upgrade

    def per_meter(max_level: int):
        upgrade = Upgrade(max_level)
        upgrade.type = ValueType.PER_METER
        return upgrade
    
    def per_second(max_level: int):
        upgrade = Upgrade(max_level)
        upgrade.type = ValueType.PER_SECOND
        return upgrade