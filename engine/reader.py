from regions.game import game_region
from .data import data
from .process import Process

class Reader(Process):
    id = "READER"

    def iteration(self):
        wave = game_region.playing.enemies.wave.read()
        if isinstance(wave, (int, float)):
            data.wave = int(wave)

reader = Reader()