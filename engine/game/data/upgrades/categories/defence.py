from engine.game.data.upgrades.categories import CategoryData
from engine.game.data.upgrades.upgrade import UpgradeData
from utilities.parser import ValueType

class DefenceData(CategoryData):
    id = "defence"
    first = "Health"

    health = UpgradeData(ValueType.NUMBER, 6000)
    health_regen = UpgradeData(ValueType.PER_SECOND, 6000)
    defence_percentage = UpgradeData(ValueType.PERCENTAGE, 99)
    defence_absolute = UpgradeData(ValueType.NUMBER, 6000)
    thorn_damage = UpgradeData(ValueType.PERCENTAGE, 99)
    lifesteal = UpgradeData(ValueType.PERCENTAGE, 80)
    knockback_chance = UpgradeData(ValueType.PERCENTAGE, 80)
    knockback_force = UpgradeData(ValueType.NUMBER, 40)
    orb_speed = UpgradeData(ValueType.NUMBER, 38)
    orbs = UpgradeData(ValueType.NUMBER, 4)
    shockwave_size = UpgradeData(ValueType.NUMBER, 35)
    shockwave_frequency = UpgradeData(ValueType.DURATION, 40)
    land_mine_chance = UpgradeData(ValueType.PERCENTAGE, 50)
    land_mine_damage = UpgradeData(ValueType.NUMBER, 200)
    land_mine_radius = UpgradeData(ValueType.NUMBER, 50)

    upgrades = [
        health,
        health_regen,
        defence_percentage,
        defence_absolute,
        thorn_damage,
        lifesteal,
        knockback_chance,
        knockback_force,
        orb_speed,
        orbs,
        shockwave_size,
        shockwave_frequency,
        land_mine_chance,
        land_mine_damage,
        land_mine_radius
    ]