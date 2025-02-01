from regions.game import game_region
from ..data import data
from ..process import Process
import logging

class Reader(Process):
    id = "READER"

    def believable(self, old: int, new: int) -> bool:
        if old == 0: return True
        return abs(new - old) / old < 0.1

    def iteration(self):
        wave = game_region.playing.enemies.wave.read()
        if isinstance(wave, (int, float)):
            wave = int(wave)
            if data.wave != wave and self.believable(data.wave, wave):
                logging.info(f"🏆 Wave changed: {data.wave} + {wave - data.wave} = {wave}")
                data.wave = int(wave)

        gems = game_region.playing.resources.gems.read()
        if isinstance(gems, (int, float)):
            gems = int(gems)
            if data.gems != gems and self.believable(data.gems, gems):
                logging.info(f"💎 Gems changed: {data.gems} + {gems - data.gems} = {gems}")
                data.gems = int(gems)

reader = Reader()