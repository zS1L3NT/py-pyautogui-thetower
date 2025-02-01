from constants import *
from regions.game import region
from utilities.parser import ValueType
from ..data import data
from ..process import Process
from .adwatcher import adwatcher
from .algorithm import algorithm
import pyautogui as ui
import logging
import time
import os

class Retry(Process):
    id = "RETRY"

    def iteration(self):
        if region.playing.modals.game_over.is_present():
            logging.info("💀 Game over modal is present, retrying")
            adwatcher.stop()
            algorithm.stop()

            file_name = os.path.join("logs", "images", f"{time.strftime("%Y-%m-%d %H-%M-%S")}.png")
            ui.screenshot(region = GAME_REGION).save(file_name)

            region.playing.modals.game_over.retry_button.click()

            # If the upgrades menu is closed or we are on a different category, open it
            if region.playing.upgrade_border.title.read(type = ValueType.STRING) != "UTILITY UPGRADES":
                region.playing.categories.utility.click()

            data.reset()
            adwatcher.start()
            algorithm.start()

        time.sleep(1)

retry = Retry()