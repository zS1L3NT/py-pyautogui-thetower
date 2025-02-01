from constants import *
from regions.game import region
from ..data import data
from ..process import Process
import pyautogui as ui
import logging
import time
import os

class Retry(Process):
    id = "RETRY"

    def iteration(self):
        if region.playing.modals.game_over.is_present():
            logging.info("💀 Game over modal is present, retrying")

            file_name = os.path.join("logs", "images", f"{time.strftime("%Y-%m-%d %H-%M-%S")}.png")
            ui.screenshot(region = GAME_REGION).save(file_name)

            region.playing.modals.game_over.retry_button.click()
            data.reset()

        time.sleep(30)

retry = Retry()