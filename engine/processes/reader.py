from regions.game import game_region
from ..data import data
from ..process import Process
import time

class Reader(Process):
    id = "READER"

    def iteration(self):
        wave = game_region.playing.enemies.wave.read()
        if isinstance(wave, (int, float)):
            wave = int(wave)
            if data.wave != wave:
                self.log(f"Wave changed: {data.wave} + {wave - data.wave} = {wave}")
                data.wave = int(wave)

        time.sleep(1)

reader = Reader()