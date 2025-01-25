from engine.game.data.upgrades.categories import Category
from engine.game.data.upgrades.upgrade import Upgrade, Type

class Attack(Category):
    category = "attack"

    damage = Upgrade(Type.NUMBER, 6000)
    attack_speed = Upgrade(Type.NUMBER, 99)
    critical_chance = Upgrade(Type.PERCENTAGE, 79)
    critical_factor = Upgrade(Type.MULTIPLIER, 150)
    range = Upgrade(Type.DISTANCE, 79)
    damage_per_meter = Upgrade(Type.PER_METER, 200)
    multishot_chance = Upgrade(Type.PERCENTAGE, 99)
    multishot_targets = Upgrade(Type.NUMBER, 7)
    rapid_fire_chance = Upgrade(Type.PERCENTAGE, 85)
    rapid_fire_duration = Upgrade(Type.DURATION, 99)
    bounce_shot_chance = Upgrade(Type.PERCENTAGE, 85)
    bounce_shot_targets = Upgrade(Type.NUMBER, 7)
    bounce_shot_range = Upgrade(Type.DISTANCE, 60)

    def __init__(self):
        self.list = [
            self.damage,
            self.attack_speed,
            self.critical_chance,
            self.critical_factor,
            self.range,
            self.damage_per_meter,
            self.multishot_chance,
            self.multishot_targets,
            self.rapid_fire_chance,
            self.rapid_fire_duration,
            self.bounce_shot_chance,
            self.bounce_shot_targets,
            self.bounce_shot_range,
        ]

        super().__init__()