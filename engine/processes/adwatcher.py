from regions.game import game_region
from utilities.parser import ValueType
from utilities.windows import switch_to_game
from .algorithm import algorithm
from .reader import reader
from .retry import retry
from .recorder import recorder
from ..process import Process
import pyautogui as ui
import logging
import time

class AdWatcher(Process):
    id = "ADWATCHER"

    def pause(self):
        reader.stop()
        algorithm.stop()
        retry.stop()

        time.sleep(1)

    def resume(self):
        time.sleep(1)

        reader.start()
        algorithm.start()
        retry.start()

    def close_ad(self):
        recorder.start()

        # Left ads seem to not have a second screen
        if game_region.ad.left_close_button.read(type = ValueType.STRING) in ["x", "X"]:
            logging.info("⬅️ Left ad closing mechanism")
            game_region.ad.left_close_button.click()
        else:
            logging.info("➡️ Right ad closing mechanism")
            game_region.ad.right_close_button.click()

            ui.press("enter")

            time.sleep(1)

            switch_to_game()

            time.sleep(5)

            if game_region.ad.right_close_button.read(type = ValueType.STRING) in ["x", "X"]:
                game_region.ad.right_close_button.click()

        time.sleep(1)

    def iteration(self):
        playing_region = game_region.playing

        if playing_region.ad_gems.is_present():
            logging.info("📺 Watching ad for gems")
            self.pause()

            playing_region.ad_gems.click()

            time.sleep(75)

            self.close_ad()

            # Claim the gems
            game_region.ad_claimed.claim_button.click()

            time.sleep(1)

            self.resume()

        if playing_region.ad_coin_bonus.status.read(type = ValueType.STRING) == "Inactive":
            logging.info("📺 Watching ad for coin bonus")
            self.pause()

            # Open the coin bonus modal
            playing_region.ad_coin_bonus.click()

            time.sleep(1)

            for _ in range(3):
                playing_region.modals.coin_bonus.watch_button.click()

                time.sleep(75)

                self.close_ad()

                time.sleep(1)

            # Close the coin bonus modal
            playing_region.menu.toggle.click()

            time.sleep(1)

            self.resume()

adwatcher = AdWatcher()