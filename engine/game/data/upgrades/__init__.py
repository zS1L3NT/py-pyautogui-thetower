from typing import List
from engine.game.data.upgrades.categories import CategoryData
from engine.game.data.upgrades.categories.attack import AttackData
from engine.game.data.upgrades.categories.defence import DefenceData
from engine.game.data.upgrades.categories.utility import UtilityData

class UpgradesData:
    attack = AttackData()
    defence = DefenceData()
    utility = UtilityData()

    categories: List["CategoryData"] = [attack, defence, utility]

    def __str__(self):
        return f"{{\n    attack: {self.attack}\n    defence: {self.defence}\n    utility: {self.utility}\n  }}"