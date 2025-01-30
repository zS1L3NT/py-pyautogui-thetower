from engine.game.data import GameData
from engine.game.process import Process
from regions.playing import PlayingRegion

class GameReader(Process):
    data: GameData
    region: PlayingRegion

    def __init__(self, data: GameData, region: PlayingRegion):
        self.data = data
        self.region = region
        super().__init__("GAME_READER", "reader")

    def run(self):
        while not self.stop_event.is_set():
            wave = self.region.enemies.wave.read()
            if wave is not None:
                self.data.wave = wave