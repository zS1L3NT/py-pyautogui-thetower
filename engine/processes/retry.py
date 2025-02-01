from regions.game import region
from ..data import data
from ..process import Process
import logging
import time

class Retry(Process):
    id = "RETRY"

    def iteration(self):
        if region.playing.modals.game_over.is_present():
            logging.info("💀 Game over modal is present, retrying")
            region.playing.modals.game_over.retry_button.click()
            data.reset()

        time.sleep(30)

retry = Retry()