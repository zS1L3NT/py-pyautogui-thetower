from typing import Callable
from engine.game.data import GameData
from regions.playing import PlayingRegion
import threading
import time

class GameAdmin:
    data: GameData
    region: PlayingRegion

    stop_event = threading.Event()
    reset: Callable[[], None]

    def __init__(self, data: GameData, region: PlayingRegion):
        self.data = data
        self.region = region

    def run(self, reset: Callable[[], None]):
        self.reset = reset

        print("[GAME_ADMIN] Starting admin thread")
        thread = threading.Thread(target = self.thread)
        thread.start()

    def thread(self):
        while not self.stop_event.is_set():
            if self.region.game_over_modal.is_present():
                print("[GAME_ADMIN] Game over modal is present, retrying")
                self.region.game_over_modal.retry_button.click()
                self.reset()
            time.sleep(5)