from engine.game.data.upgrades.upgrade import UpgradeData

class CategoryData:
    id = ""
    upgrades: tuple["UpgradeData"]

    def __init__(self):
        for key in dir(self):
            value = getattr(self, key)
            if isinstance(value, UpgradeData):
                value.id = key
                value.category = self.id
    
    def __str__(self):
        return f"{{\n{"\n".join([f"      {upgrade}" for upgrade in self.upgrades])}\n    }}"