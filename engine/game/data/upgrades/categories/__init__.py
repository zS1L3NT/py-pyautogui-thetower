from typing import List
from engine.game.data.upgrades.upgrade import Upgrade

class Category:
    category = ""
    list: List["Upgrade"]

    def __init__(self):
        for key in dir(self):
            value = getattr(self, key)
            if isinstance(value, Upgrade):
                value.id = key
                value.category = self.category
    
    def __str__(self):
        return f"{{\n{"\n".join([f"      {upgrade}" for upgrade in self.list])}\n    }}"