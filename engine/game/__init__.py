from constants import *
from engine.game.algorithm import GameAlgorithm
from engine.game.reader import GameReader
from engine.game.data import GameData
from regions.game import GameRegion

class GameEngine:
    data = GameData()
    region: GameRegion

    reader: GameReader
    algorithm: GameAlgorithm

    def __init__(self, region):
        self.region = region
        self.screen = region.playing

        self.reader = GameReader(self.data, self.region)
        self.algorithm = GameAlgorithm(self.data, self.region)

    def run(self):
        self.reader.run()
        # self.algorithm.run()
