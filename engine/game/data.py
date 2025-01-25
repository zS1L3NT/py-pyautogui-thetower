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

class Resources:
    cash = 0
    coins = 0
    gems = 0

    def __setattr__(self, name, value):
        number = Cleaner(value).number()
        if not number: return
        super().__setattr__(name, number)

    def __str__(self):
        return f"{{ cash: {self.cash}, coins: {self.coins}, gems: {self.gems} }}"

class Player:
    damage = 0
    health = 0
    max_health = 0
    health_regen = 0

    def __setattr__(self, name, value):
        if name == "damage":
            number = Cleaner(value).number()
            if not number: return
            super().__setattr__(name, number)
        elif name == "healths":
            numbers = Cleaner(value).number_slash_number()
            if not numbers: return
            super().__setattr__("health", numbers[0])
            super().__setattr__("max_health", numbers[1])
        elif name == "health_regen":
            number = Cleaner(value).number_slash_s()
            if not number: return
            super().__setattr__(name, number)

    def __str__(self):
        return f"{{ damage: {self.damage}, health: {self.health}, max_health: {self.max_health}, health_regen: {self.health_regen} }}"

class Enemies:
    wave = 0
    damage = 0
    health = 0

    def __setattr__(self, name, value):
        number = Cleaner(value).number()
        if not number: return
        super().__setattr__(name, number)

    def __str__(self):
        return f"{{ wave: {self.wave}, damage: {self.damage}, health: {self.health} }}"

class Upgrades:
    pass

class GameData:
    resources = Resources()
    player = Player()
    enemies = Enemies()
    upgrades = Upgrades()

    def __str__(self):
        return f"GameData {{\n  resources: {self.resources}\n  player: {self.player}\n  enemies: {self.enemies}\n  upgrades: {self.upgrades}\n}}"