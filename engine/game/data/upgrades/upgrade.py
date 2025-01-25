from engine.game.data.cleaner import Cleaner
from enum import Enum
import re

class Type(Enum):
    NUMBER = "number"
    PERCENTAGE = "percentage"
    MULTIPLIER = "multiplier"
    DISTANCE = "distance"
    DURATION = "duration"
    PER_METER = "per_meter"
    PER_SECOND = "per_second"

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)

    def regex(type):
        match type:
            case Type.NUMBER.value: return r"(\d+(?:\.\d+)?[KMBT]?)" 
            case Type.PERCENTAGE.value: return r"(\d+(?:\.\d+)?)%"
            case Type.MULTIPLIER.value: return r"x?(\d+(?:\.\d+)?)"
            case Type.DISTANCE.value: return r"(\d+(?:\.\d+)?)m"
            case Type.DURATION.value: return r"(\d+(?:\.\d+)?)\s?s(ec)?"
            case Type.PER_METER.value: return r"(\d+(?:\.\d+)?)\s?\/\s?m"
            case Type.PER_SECOND.value: return r"(\d+(?:\.\d+)?)\s?\/\s?sec"

class Upgrade:
    id = ""
    category = ""

    type: Type
    value = float('-inf')
    cost = float('-inf')
    level = float('-inf')
    max_level = float('-inf')

    def __init__(self, type, max_level):
        self.type = type
        self.max_level = max_level

    def __setattr__(self, name, value):
        value = str(value).strip()
        if name == "cost":
            match = re.search(r"\D?(\d+(?:\.\d+)?[KMBT]?)", value)
            if not match: return
            super().__setattr__(name, match.group(1))
        elif name == "level":
            if not value.isnumeric(): return
            super().__setattr__(name, int(value))
        elif name == "value":
            if self.type == Type.NUMBER:
                number = Cleaner(value).number()
                if not number: return
                super().__setattr__(name, number)
            else:
                match = re.search(Type.regex(self.type), value)
                if not match: return
                super().__setattr__(name, match.group(1))
        else:
            super().__setattr__(name, value)
    
    def __str__(self):
        return f"{self.id}: {self.value}, ${self.cost} [{self.level} / {self.max_level}]"