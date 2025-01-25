from engine.game.data.upgrades.categories import Category
from engine.game.data.upgrades.upgrade import Upgrade, Type

class Defence(Category):
    category = "defence"

    health = Upgrade(Type.NUMBER, 6000)
    health_regen = Upgrade(Type.PER_SECOND, 6000)
    defence_percentage = Upgrade(Type.PERCENTAGE, 99)
    defence_absolute = Upgrade(Type.NUMBER, 6000)
    thorn_damage = Upgrade(Type.PERCENTAGE, 99)
    lifesteal = Upgrade(Type.PERCENTAGE, 80)
    knockback_chance = Upgrade(Type.PERCENTAGE, 80)
    knockback_force = Upgrade(Type.NUMBER, 40)
    orb_speed = Upgrade(Type.NUMBER, 38)
    orbs = Upgrade(Type.NUMBER, 4)
    shockwave_size = Upgrade(Type.NUMBER, 35)
    shockwave_frequency = Upgrade(Type.DURATION, 40)
    land_mine_chance = Upgrade(Type.PERCENTAGE, 50)
    land_mine_damage = Upgrade(Type.NUMBER, 200)
    land_mine_radius = Upgrade(Type.NUMBER, 50)

    def __init__(self):
        self.list = [
            self.health,
            self.health_regen,
            self.defence_percentage,
            self.defence_absolute,
            self.thorn_damage,
            self.lifesteal,
            self.knockback_chance,
            self.knockback_force,
            self.orb_speed,
            self.orbs,
            self.shockwave_size,
            self.shockwave_frequency,
            self.land_mine_chance,
            self.land_mine_damage,
            self.land_mine_radius,
        ]

        super().__init__()