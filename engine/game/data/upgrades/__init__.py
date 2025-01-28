from typing import List
from engine.game.data.upgrades.categories import Category
from engine.game.data.upgrades.categories.attack import Attack
from engine.game.data.upgrades.categories.defence import Defence
from engine.game.data.upgrades.categories.utility import Utility

class Upgrades:
    attack = Attack()
    defence = Defence()
    utiltiy = Utility()

    categories: List["Category"] = [attack, defence, utiltiy]

    def __str__(self):
        return f"{{\n    attack: {self.attack}\n    defence: {self.defence}\n    utility: {self.utiltiy}\n  }}"