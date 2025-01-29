from engine.game.data import GameData
from regions.playing import PlayingRegion
import threading
import time

class GameAdmin:
    data: GameData
    region: PlayingRegion

    stop_event = threading.Event()

    def __init__(self, data: GameData, region: PlayingRegion):
        self.data = data
        self.region = region

    def run(self):
        print("[GAME_ADMIN] Starting admin thread")
        thread = threading.Thread(target = self.thread)
        thread.start()

    def thread(self):
        while not self.stop_event.is_set():
            if self.region.game_over_modal.is_present():
                print("[GAME_ADMIN] Game over modal is present, retrying")
                self.region.game_over_modal.retry_button.click()
            time.sleep(5)