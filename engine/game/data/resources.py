class ResourcesData:
    cash = 0
    coins = 0
    gems = 0

    def __setattr__(self, name, value):
        if value is not None:
            super().__setattr__(name, value)

    def __str__(self):
        return f"{{\n    cash: {self.cash}\n    coins: {self.coins}\n    gems: {self.gems}\n  }}"