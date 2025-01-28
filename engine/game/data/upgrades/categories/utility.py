from engine.game.data.upgrades.categories import Category
from engine.game.data.upgrades.upgrade import Upgrade

class Utility(Category):
    category = "utility"

    cash_bonus = Upgrade.multiplier(149)
    cash_per_wave = Upgrade.number(149)
    coins_per_kill_bonus = Upgrade.multiplier(149)
    coins_per_wave = Upgrade.number(149)
    free_attack_upgrade = Upgrade.percentage(99)
    free_defence_upgrade = Upgrade.percentage(99)
    free_utility_upgrade = Upgrade.percentage(99)
    interest_per_wave = Upgrade.percentage(99)
    recovery_amount = Upgrade.percentage(300)
    max_recovery = Upgrade.multiplier(500)
    package_chance = Upgrade.percentage(60)

    upgrades = [
        cash_bonus,
        cash_per_wave,
        coins_per_kill_bonus,
        coins_per_wave,
        free_attack_upgrade,
        free_defence_upgrade,
        free_utility_upgrade,
        interest_per_wave,
        recovery_amount,
        max_recovery,
        package_chance
    ]