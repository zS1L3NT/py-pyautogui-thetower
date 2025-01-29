from engine.game.data.upgrades.categories import CategoryData
from engine.game.data.upgrades.upgrade import UpgradeData
from utilities.parser import ValueType

class UtilityData(CategoryData):
    id = "utility"
    first = "Cash Bonus"

    cash_bonus = UpgradeData(ValueType.MULTIPLIER, 149)
    cash_per_wave = UpgradeData(ValueType.NUMBER, 149)
    coins_per_kill_bonus = UpgradeData(ValueType.MULTIPLIER, 149)
    coins_per_wave = UpgradeData(ValueType.NUMBER, 149)
    free_attack_upgrade = UpgradeData(ValueType.PERCENTAGE, 99)
    free_defence_upgrade = UpgradeData(ValueType.PERCENTAGE, 99)
    free_utility_upgrade = UpgradeData(ValueType.PERCENTAGE, 99)
    interest_per_wave = UpgradeData(ValueType.PERCENTAGE, 99)
    recovery_amount = UpgradeData(ValueType.PERCENTAGE, 300)
    max_recovery = UpgradeData(ValueType.MULTIPLIER, 500)
    package_chance = UpgradeData(ValueType.PERCENTAGE, 60)

    upgrades = (
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
    )