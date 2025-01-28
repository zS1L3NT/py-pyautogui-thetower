from engine.game.data.resources import ResourcesData
from engine.game.data.player import PlayerData
from engine.game.data.enemies import EnemiesData
from engine.game.data.upgrades import UpgradesData

class GameData:
    resources = ResourcesData()
    player = PlayerData()
    enemies = EnemiesData()
    upgrades = UpgradesData()

    def __str__(self):
        return f"GameData {{\n  resources: {self.resources}\n  player: {self.player}\n  enemies: {self.enemies}\n  upgrades: {self.upgrades}\n}}"