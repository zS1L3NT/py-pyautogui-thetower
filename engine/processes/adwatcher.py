from recorder import Recorder
from regions.game import region
from typing import Callable
from utilities.parser import Parser, ValueType
from utilities.windows import switch_to_game
from .algorithm import algorithm
from .reader import reader
from ..process import Process
import logging
import time

class AdWatcher(Process):
    id = "ADWATCHER"
    failed_at: float | None = None

    def pause_processes(self):
        reader.stop()
        algorithm.stop()

        time.sleep(1)

    def resume_processes(self):
        time.sleep(1)

        reader.start()
        algorithm.start()

    def not_on_cooldown(self):
        if self.failed_at is None:
            return True
        
        if time.time() - self.failed_at > (5 * 60):
            self.failed_at = None
            return True

        return False

    def close_ad(self):
        # Left ads seem to not have a second screen
        is_reward_granted: Callable[[object], bool] = lambda value: isinstance(value, str) and "x" in value.lower() and "reward" in value.lower() and "granted" in value.lower()

        if region.ad.left_reward_granted.read(type = ValueType.STRING, is_valid = is_reward_granted) is not None:
            logging.info("⬅️ Left reward granted mechanism")
            region.ad.left_reward_granted.close_button.click()
        elif region.ad.right_reward_granted.read(type = ValueType.STRING, is_valid = is_reward_granted) is not None:
            logging.info("➡️ Right reward granted mechanism")
            region.ad.right_reward_granted.close_button.click()
        else:
            logging.info("➡️ Right closing mechanism")
            region.ad.right_close_button.click()

            time.sleep(1)

            switch_to_game()

            time.sleep(5)

            if region.ad.right_close_button.read(type = ValueType.STRING) in ["x", "X"]:
                region.ad.right_close_button.click()

        time.sleep(1)

    def iteration(self):
        if region.playing.ad_gems.is_present() and self.not_on_cooldown():
            with Recorder():
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
                    time.sleep(75)

                    self.close_ad()

                    # Claim the gems
                    if region.ad_claimed.claim_button.is_present():
                        region.ad_claimed.claim_button.click()
                    else:
                        logging.warning("❗ Claim gem modal did not show up?!")

                self.resume_processes()

        duration = Parser(str(region.playing.ad_coin_bonus.status.read(type = ValueType.STRING))).time()
        if isinstance(duration, int) and duration < 60 * 60 and self.not_on_cooldown():
            with Recorder():
                logging.info("📺 Watching ad for coin bonus")
                self.pause_processes()

                # Open the coin bonus modal
                region.playing.ad_coin_bonus.click()

                # wait for the modal to open fully?
                time.sleep(0.5)

                region.playing.modals.coin_bonus.watch_button.click()

                # wait for the ad to load / fail
                time.sleep(5)

                if region.playing.modals.ad_failed.ok_button.is_present():
                    logging.warning("⚠️ Could not load ad, will wait 5 minutes before trying again")
                    self.failed_at = time.time()

                    region.playing.modals.ad_failed.ok_button.click()
                else:
                    # wait for the ad to finish
                    time.sleep(75)

                    self.close_ad()

                    # expect the coin bonus modal to still be open
                    if not region.playing.modals.coin_bonus.watch_button.is_present():
                        logging.warning("❗ Coins bonus modal did not show up?!")

                # Close the coin bonus modal
                region.playing.menu.toggle.click()

                self.resume_processes()

adwatcher = AdWatcher()