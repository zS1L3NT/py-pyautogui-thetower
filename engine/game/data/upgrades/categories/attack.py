from engine.game.data.upgrades.categories import CategoryData
from engine.game.data.upgrades.upgrade import UpgradeData
from utilities.parser import ValueType

class AttackData(CategoryData):
    id = "attack"
    first = "Damage"

    damage = UpgradeData(ValueType.NUMBER, 6000)
    attack_speed = UpgradeData(ValueType.NUMBER, 99)
    critical_chance = UpgradeData(ValueType.PERCENTAGE, 79)
    critical_factor = UpgradeData(ValueType.MULTIPLIER, 150)
    range = UpgradeData(ValueType.DISTANCE, 79)
    damage_per_meter = UpgradeData(ValueType.PER_METER, 200)
    multishot_chance = UpgradeData(ValueType.PERCENTAGE, 99)
    multishot_targets = UpgradeData(ValueType.NUMBER, 7)
    rapid_fire_chance = UpgradeData(ValueType.PERCENTAGE, 85)
    rapid_fire_duration = UpgradeData(ValueType.DURATION, 99)
    bounce_shot_chance = UpgradeData(ValueType.PERCENTAGE, 85)
    bounce_shot_targets = UpgradeData(ValueType.NUMBER, 7)
    bounce_shot_range = UpgradeData(ValueType.DISTANCE, 60)

    upgrades = (
        damage,
        attack_speed,
        critical_chance,
        critical_factor,
        range,
        damage_per_meter,
        multishot_chance,
        multishot_targets,
        rapid_fire_chance,
        rapid_fire_duration,
        bounce_shot_chance,
        bounce_shot_targets,
        bounce_shot_range
    )