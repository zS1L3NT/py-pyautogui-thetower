from engine.game.data.upgrades.categories import Category
from engine.game.data.upgrades.upgrade import Upgrade, Type

class Utility(Category):
    category = "utility"

    cash_bonus = Upgrade(Type.MULTIPLIER, 149)
    cash_per_wave = Upgrade(Type.NUMBER, 149)
    coins_per_kill_bonus = Upgrade(Type.MULTIPLIER, 149)
    coins_per_wave = Upgrade(Type.NUMBER, 149)
    free_attack_upgrade = Upgrade(Type.PERCENTAGE, 99)
    free_defence_upgrade = Upgrade(Type.PERCENTAGE, 99)
    free_utility_upgrade = Upgrade(Type.PERCENTAGE, 99)
    interest_per_wave = Upgrade(Type.PERCENTAGE, 99)
    recovery_amount = Upgrade(Type.PERCENTAGE, 300)
    max_recovery = Upgrade(Type.MULTIPLIER, 500)
    package_chance = Upgrade(Type.PERCENTAGE, 60)

    def __init__(self):
        self.list = [
            self.cash_bonus,
            self.cash_per_wave,
            self.coins_per_kill_bonus,
            self.coins_per_wave,
            self.free_attack_upgrade,
            self.free_defence_upgrade,
            self.free_utility_upgrade,
            self.interest_per_wave,
            self.recovery_amount,
            self.max_recovery,
            self.package_chance,
        ]

        super().__init__()