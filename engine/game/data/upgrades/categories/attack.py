from engine.game.data.upgrades.categories import Category
from engine.game.data.upgrades.upgrade import Upgrade

class Attack(Category):
    category = "attack"

    damage = Upgrade.number(6000)
    attack_speed = Upgrade.number(99)
    critical_chance = Upgrade.percentage(79)
    critical_factor = Upgrade.multiplier(150)
    range = Upgrade.distance(79)
    damage_per_meter = Upgrade.per_meter(200)
    multishot_chance = Upgrade.percentage(99)
    multishot_targets = Upgrade.number(7)
    rapid_fire_chance = Upgrade.percentage(85)
    rapid_fire_duration = Upgrade.duration(99)
    bounce_shot_chance = Upgrade.percentage(85)
    bounce_shot_targets = Upgrade.number(7)
    bounce_shot_range = Upgrade.distance(60)

    upgrades = [
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
    ]