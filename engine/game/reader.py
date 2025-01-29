from engine.game.data import GameData
from regions.playing import PlayingRegion
import threading

class GameReader:
    data: GameData
    region: PlayingRegion

    stop_event = threading.Event()

    def __init__(self, data: GameData, region: PlayingRegion):
        self.data = data
        self.region = region

    def run(self):
        print("[GAME_READER] Starting reader thread")
        thread = threading.Thread(target = self.thread)
        thread.start()

    def thread(self):
        while not self.stop_event.is_set():
            self.data.wave = self.region.enemies.wave.read()