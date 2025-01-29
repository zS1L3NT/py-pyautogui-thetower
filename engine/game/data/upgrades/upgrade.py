from utilities.parser import ValueType

class UpgradeData:
    id = ""
    category = ""

    type: ValueType
    value = float('-inf')
    cost = float('-inf')
    level = float('-inf')
    max_level = float('-inf')

    target_cost = 0

    def __init__(self, type: ValueType, max_level: int):
        self.type = type
        self.max_level = max_level

    def __setattr__(self, name, value):
        if value is not None:
            super().__setattr__(name, value)

    def __str__(self):
        return f"{self.id}: {self.value}, ${self.cost} [{self.level} / {self.max_level}]"