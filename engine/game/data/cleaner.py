import re

class Cleaner:
    raw = ""

    def __init__(self, raw):
        self.raw = raw

    def number(self):
        match = re.search(r"\d+(\.\d+)?[KMBT]?", str(self.raw))
        if not match:
            return None
        
        return self.parse(match.group())

    def number_slash_number(self):
        match = re.match(r"(\d+(?:\.\d+)?[KMBT]?)\s*\/\s*(\d+(?:\.\d+)?[KMBT]?)", str(self.raw))
        if not match:
            return None

        return (self.parse(match.group(1)), self.parse(match.group(2)))

    def number_slash_s(self):
        match = re.match(r"(\d+(?:\.\d+)?[KMBT]?)\/s", str(self.raw))
        if not match:
            return None

        return self.parse(match.group(1))

    def parse(self, string):
        if string[-1].isnumeric():
            return float(string)
        
        multipliers = {
            "K": 1_000,
            "M": 1_000_000,
            "B": 1_000_000_000,
            "T": 1_000_000_000_000,
        }

        return float(string[:-1]) * multipliers[string[-1]]