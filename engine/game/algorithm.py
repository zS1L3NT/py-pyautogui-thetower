from engine.game.data import GameData
from regions.playing import PlayingRegion
import threading

class GameAlgorithm:
    data: GameData
    region: PlayingRegion

    stop_event = threading.Event()

    def __init__(self, data: GameData, region: PlayingRegion):
        self.data = data
        self.region = region

    def __del__(self):
        self.stop_event.set()

    def run(self):
        print("[GAME_ALGORITHM] ✅ Starting algorithm thread")
        thread = threading.Thread(target = self.algorithm)
        thread.start()

    def algorithm(self):
        while not self.stop_event.is_set():
            pass
