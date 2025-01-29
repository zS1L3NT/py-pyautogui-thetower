from enum import Enum
import re

class ValueType(Enum):
    __NUMERIC = r"(\d+(?:\.\d+)?[KMBT]?)"

    NUMBER = __NUMERIC
    PERCENTAGE = rf"{__NUMERIC}\s?%"
    MULTIPLIER = rf"x\s?{__NUMERIC}"
    DISTANCE = rf"{__NUMERIC}\s?m"
    DURATION = rf"{__NUMERIC}\s?s(?:ec)?"
    PER_METER = rf"{__NUMERIC}\s?\/\s?m"
    PER_SECOND = rf"{__NUMERIC}\s?\/\s?s(?:ec)?"
    COST = rf"\$\s?{__NUMERIC}"

    NUMBER_SLASH_NUMBER = rf"{__NUMERIC}\s?\/\s?{__NUMERIC}"

    CUSTOM = r""

    def custom(pattern: str = ""):
        type = ValueType.CUSTOM
        type._value_ = pattern
        return type

class Parser:
    value = ""

    def __init__(self, value):
        self.value = str(value).strip()
    
    def __flatten(value):
        if value[-1].isnumeric():
            return float(value)
        
        multipliers = {"K": 1e3, "M": 1e6, "B": 1e9, "T": 1e12}

        return float(value[:-1]) * multipliers[value[-1]]

    def type(self, type: ValueType):
        match = re.search(type.value, self.value)
        if match:
            if type == ValueType.NUMBER_SLASH_NUMBER:
                return Parser.__flatten(match.group(1)), Parser.__flatten(match.group(2))
            elif type == ValueType.CUSTOM:
                return match.group(1)
            else:
                return Parser.__flatten(match.group(1))
            
    def number(self):
        return self.type(ValueType.NUMBER)

    def percentage(self):
        return self.type(ValueType.PERCENTAGE)
    
    def multiplier(self):
        return self.type(ValueType.MULTIPLIER)
    
    def distance(self):
        return self.type(ValueType.DISTANCE)
    
    def duration(self):
        return self.type(ValueType.DURATION)

    def per_meter(self):
        return self.type(ValueType.PER_METER)
    
    def per_second(self):
        return self.type(ValueType.PER_SECOND)
    
    def cost(self):
        return self.type(ValueType.COST)

    def number_slash_number(self):
        match = re.search(ValueType.NUMBER_SLASH_NUMBER.value, self.value)
        if match:
            return (Parser.__flatten(match.group(1)), Parser.__flatten(match.group(2)))