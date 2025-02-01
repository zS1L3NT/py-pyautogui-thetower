from regions.game import region
from ..data import data
from ..process import Process
import logging

class Reader(Process):
    id = "READER"

    def believable(self, old: int, new: int) -> bool:
        if old < 10: return True
        if new < old: return False
        return (new - old) / old < 0.1

    def iteration(self):
        wave = region.playing.enemies.wave.read()
        if isinstance(wave, (int, float)):
            wave = int(wave)
            if data.wave != wave and self.believable(data.wave, wave) and wave - data.wave >= 10:
                logging.info(f"🏆 Wave increased: {data.wave} + {wave - data.wave} = {wave}")
                data.wave = int(wave)

        coins = region.playing.resources.coins.read()
        if isinstance(coins, (int, float)):
            coins = int(coins)
            if data.coins != coins and self.believable(data.coins, coins) and coins - data.coins >= 10000:
                logging.info(f"💰 Coins increased: {data.coins} + {coins - data.coins} = {coins}")
                data.coins = int(coins)

        gems = region.playing.resources.gems.read()
        if isinstance(gems, (int, float)):
            gems = int(gems)
            if data.gems != gems and self.believable(data.gems, gems):
                logging.info(f"💎 Gems increased: {data.gems} + {gems - data.gems} = {gems}")
                data.gems = int(gems)

reader = Reader()