from constants import *
from regions.playing import PlayingScreen
from engine.game.data import GameData

class GameEngine:
    data = GameData()
    region: PlayingScreen

    def __init__(self, region):
        self.region = region

    def start(self):
        while True:
            self.data.resources.cash = self.region.resources.cash.read()
            self.data.resources.coins = self.region.resources.coins.read()
            self.data.resources.gems = self.region.resources.gems.read()

            self.data.player.damage = self.region.player.damage.read()
            self.data.player.healths = self.region.player.healths.read()
            self.data.player.health_regen = self.region.player.health_regen.read()

            self.data.enemies.wave = self.region.enemies.wave.read()
            self.data.enemies.damage = self.region.enemies.damage.read()
            self.data.enemies.health = self.region.enemies.health.read()

            print(self.data)