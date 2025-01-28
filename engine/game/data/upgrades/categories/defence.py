from engine.game.data.upgrades.categories import Category
from engine.game.data.upgrades.upgrade import Upgrade

class Defence(Category):
    category = "defence"

    health = Upgrade.number(6000)
    health_regen = Upgrade.per_second(6000)
    defence_percentage = Upgrade.percentage(99)
    defence_absolute = Upgrade.number(6000)
    thorn_damage = Upgrade.percentage(99)
    lifesteal = Upgrade.percentage(80)
    knockback_chance = Upgrade.percentage(80)
    knockback_force = Upgrade.number(40)
    orb_speed = Upgrade.number(38)
    orbs = Upgrade.number(4)
    shockwave_size = Upgrade.number(35)
    shockwave_frequency = Upgrade.duration(40)
    land_mine_chance = Upgrade.percentage(50)
    land_mine_damage = Upgrade.number(200)
    land_mine_radius = Upgrade.number(50)

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