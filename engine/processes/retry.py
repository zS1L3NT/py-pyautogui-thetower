from regions.game import game_region
from ..data import data
from ..process import Process
import logging
class Retry(Process):
    id = "RETRY"

    def iteration(self):
        if game_region.playing.modals.game_over.is_present():
            logging.info("💀 Game over modal is present, retrying")
            game_region.playing.modals.game_over.retry_button.click()
            data.reset()

retry = Retry()