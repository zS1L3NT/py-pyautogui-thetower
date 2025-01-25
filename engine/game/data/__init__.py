from engine.game.data.resources import Resources
from engine.game.data.player import Player
from engine.game.data.enemies import Enemies
from engine.game.data.upgrades import Upgrades

class GameData:
    resources = Resources()
    player = Player()
    enemies = Enemies()
    upgrades = Upgrades()

    def __str__(self):
        return f"GameData {{\n  resources: {self.resources}\n  player: {self.player}\n  enemies: {self.enemies}\n  upgrades: {self.upgrades}\n}}"