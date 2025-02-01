from regions.game import region
from typing import Callable
from utilities.parser import Parser, ValueType
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
    failed_at: float | None = None

    def pause_processes(self):
        reader.stop()
        algorithm.stop()
        retry.stop()

        time.sleep(1)

    def resume_processes(self):
        time.sleep(1)

        reader.start()
        algorithm.start()
        retry.start()

    def not_on_cooldown(self):
        if self.failed_at is None:
            return True
        
        if time.time() - self.failed_at > (5 * 60):
            self.failed_at = None
            return True

        return False

    def close_ad(self):
        # Left ads seem to not have a second screen
        is_valid: Callable[[object], bool] = lambda value: isinstance(value, str) and "x" in value.lower() and "reward" in value.lower() and "granted" in value.lower()

        if region.ad.left_close_area.read(type = ValueType.STRING, is_valid = is_valid) is not None:
            logging.info("⬅️ Left ad closing mechanism")
            region.ad.left_close_button.click()
        else:
            logging.info("➡️ Right ad closing mechanism")
            region.ad.right_close_button.click()

            ui.press("enter")

            time.sleep(1)

            switch_to_game()

            time.sleep(5)

            if region.ad.right_close_button.read(type = ValueType.STRING) in ["x", "X"]:
                region.ad.right_close_button.click()

        time.sleep(1)

    def iteration(self):
        if region.playing.ad_gems.is_present() and self.not_on_cooldown():
            recorder.start()

            logging.info("📺 Watching ad for gems")
            self.pause_processes()

            region.playing.ad_gems.click()

            # wait for the ad to load / fail
            time.sleep(5)

            if region.playing.modals.ad_failed.ok_button.is_present():
                logging.warning("⚠️ Could not load ad, will wait 5 minutes before trying again")
                self.failed_at = time.time()

                region.playing.modals.ad_failed.ok_button.click()
            else:
                # wait for the ad to finish
                time.sleep(65)

                self.close_ad()

                # Claim the gems
                if region.ad_claimed.claim_button.is_present():
                    region.ad_claimed.claim_button.click()
                else:
                    logging.warning("❗ Claim gem modal did not show up?!")

            self.resume_processes()

            recorder.stop()

        duration = Parser(str(region.playing.ad_coin_bonus.status.read(type = ValueType.STRING))).time()
        if isinstance(duration, int) and duration < 30 * 60 and self.not_on_cooldown():
            recorder.start()

            logging.info("📺 Watching ad for coin bonus")
            self.pause_processes()

            # Open the coin bonus modal
            region.playing.ad_coin_bonus.click()

            # wait for the modal to open fully?
            time.sleep(0.5)

            for _ in range(5):
                region.playing.modals.coin_bonus.watch_button.click()

                # wait for the ad to load / fail
                time.sleep(5)

                if region.playing.modals.ad_failed.ok_button.is_present():
                    logging.warning("⚠️ Could not load ad, will wait 5 minutes before trying again")
                    self.failed_at = time.time()

                    region.playing.modals.ad_failed.ok_button.click()
                    break
                else:
                    # wait for the ad to finish
                    time.sleep(65)

                    self.close_ad()

                # wait for the ad to close properly
                time.sleep(1)

            # Close the coin bonus modal
            region.playing.menu.toggle.click()

            self.resume_processes()

            recorder.stop()

adwatcher = AdWatcher()