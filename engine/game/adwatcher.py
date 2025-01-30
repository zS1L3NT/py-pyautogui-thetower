from typing import Callable
from engine.game.data import GameData
from engine.game.process import Process
from regions.game import game_region
from regions.playing import PlayingRegion
from utilities.parser import ValueType
from utilities.windows import switch_to_game
import pyautogui as ui
import time

class GameAdWatcher(Process):
    data: GameData
    region: PlayingRegion
    pause: Callable
    resume: Callable

    def __init__(self, data: GameData, region: PlayingRegion, pause: Callable, resume: Callable):
        self.data = data
        self.region = region
        self.pause = pause
        self.resume = resume
        super().__init__("GAME_ADWATCHER", "adwatcher")

    def close_ad(self):
        # Left ads seem to not have a second screen
        if game_region.ad.left_close_button.read(type = ValueType.STRING).lower() == "x":
            print("[GAME_ADWATCHER] Left ad closing mechanism")
            game_region.ad.left_close_button.click()
        else:
            print("[GAME_ADWATCHER] Right ad closing mechanism")
            game_region.ad.right_close_button.click()

            ui.press("enter")

            time.sleep(1)

            switch_to_game()

            time.sleep(5)

            if game_region.ad.right_close_button.read(type = ValueType.STRING).lower() == "x":
                game_region.ad.right_close_button.click()

        time.sleep(1)

    def run(self):
        while not self.stop_event.is_set():
            if self.region.ad_gems.is_present():
                print("[GAME_ADWATCHER] Watching ad for gems")
                self.pause()

                self.region.ad_gems.click()

                time.sleep(75)

                self.close_ad()

                # Claim the gems
                game_region.ad_claimed.claim_button.click()

                self.resume()

            if self.region.ad_coin_bonus.status.read(type = ValueType.STRING) == "Inactive":
                print("[GAME_ADWATCHER] Watching ad for coin bonus")
                self.pause()

                # Open the coin bonus modal
                self.region.ad_coin_bonus.click()

                for _ in range(3):
                    self.region.coin_bonus_modal.watch_button.click()

                    time.sleep(75)

                    self.close_ad()

                # Close the coin bonus modal
                self.region.menu.toggle.click()

                self.resume()
