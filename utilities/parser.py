from enum import Enum
import re

class ValueType(Enum):
    STRING = r"([\w\s]+)"
    NUMBER = r"(\d+(?:\.\d+)?[KMBT]?)"
    PERCENTAGE = rf"{NUMBER}\s?%"
    MULTIPLIER = rf"x?\s?{NUMBER}"
    DISTANCE = rf"{NUMBER}\s?m"
    DURATION = rf"{NUMBER}\s?s(?:ec)?"
    PER_METER = rf"{NUMBER}\s?\/\s?m"
    PER_SECOND = rf"{NUMBER}\s?\/\s?s(?:ec)?"
    COST = rf"\$\s?{NUMBER}|Max"
    TIME = r"(Inactive)|(?:(\d+)h )?(\d+)m (\d+)s"

    NUMBER_SLASH_NUMBER = rf"{NUMBER}\s?\/\s?{NUMBER}"

    def characters(self):
        numbers = ".0123456789"
        multipliers = "KMBT"

        match self:
            case ValueType.STRING:
                return None
            case ValueType.NUMBER:
                return f"{numbers}{multipliers}"
            case ValueType.PERCENTAGE:
                return f"%{numbers}"
            case ValueType.MULTIPLIER:
                return f"x{numbers}{multipliers}"
            case ValueType.DISTANCE:
                return f"m{numbers}"
            case ValueType.DURATION:
                return f"s{numbers}"
            case ValueType.PER_METER:
                return f"/m{numbers}"
            case ValueType.PER_SECOND:
                return f"/s{numbers}"
            case ValueType.COST:
                return f"$ax{numbers}{multipliers}"
            case ValueType.TIME:
                raise Exception("This should not be called")
            case ValueType.NUMBER_SLASH_NUMBER:
                return f"/{numbers}"

class Parser:
    value = ""

    def __init__(self, value: str):
        self.value = str(value).strip()
    
    def __flatten(self, value: str) -> float:
        if value[-1].isnumeric():
            return float(value)
        
        multipliers = {"K": 1e3, "M": 1e6, "B": 1e9, "T": 1e12}

        return float(value[:-1]) * multipliers[value[-1]]

    def type(self, type: ValueType) -> tuple[float, float] | str | float | None:
        match = re.search(type.value, self.value)
        if match:
            if type == ValueType.NUMBER_SLASH_NUMBER:
                return self.__flatten(match.group(1)), self.__flatten(match.group(2))
            elif type == ValueType.STRING:
                return match.group(1)
            elif type == ValueType.COST:
                return self.__flatten(match.group(1)) if match.group(1) is not None else float('inf')
            elif type == ValueType.TIME:
                if match.group(1) == "Inactive":
                    return 0
                elif match.group(2) is None:
                    return (int(match.group(3)) * 60) + int(match.group(4))
                else:
                    return (int(match.group(2)) * 60 * 60) + (int(match.group(3)) * 60) + int(match.group(4))
            else:
                return self.__flatten(match.group(1))

    def string(self):
        return self.type(ValueType.STRING)
            
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

    def time(self):
        return self.type(ValueType.TIME)

    def number_slash_number(self) -> tuple[float, float] | None:
        match = re.search(ValueType.NUMBER_SLASH_NUMBER.value, self.value)
        if match:
            return (self.__flatten(match.group(1)), self.__flatten(match.group(2)))