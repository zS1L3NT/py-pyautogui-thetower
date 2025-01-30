from constants import *
from engine.game.algorithm import GameAlgorithm
from engine.game.data import GameData
from engine.game.reader import GameReader
from engine.game.adwatcher import GameAdWatcher
from regions.game import game_region
from regions.playing import PlayingRegion
from utilities.parser import ValueType
import time

class GameEngine:
    data: GameData
    region: PlayingRegion

    reader: GameReader
    algorithm: GameAlgorithm
    adwatcher: GameAdWatcher

    def __init__(self):
        self.data = GameData()
        self.region = game_region.playing

        self.reader = GameReader(self.data, self.region)
        self.algorithm = GameAlgorithm(self.data, self.region)
        self.adwatcher = GameAdWatcher(self.data, self.region, self.pause, self.resume)

    def reset(self):
        print("[GAME_ENGINE] Resetting game data")
        self.data = GameData()

    def pause(self):
        self.reader.stop()
        self.algorithm.stop()

    def resume(self):
        self.reader.start()
        self.algorithm.start()

    def start(self):
        # Close any initially opened modals
        # We click on menu because it's a position where it doesn't affect reading of values
        #   or the game itself, it's just a visual thing
        self.region.menu.toggle.click()

        # The only modal we can't close is the game over modal, so we need to check if it's present
        if self.region.game_over_modal.is_present():
            self.region.game_over_modal.retry_button.click()

        # Hide the multiplier select if it's present so we can read the category name
        if self.region.upgrade_border.multiplier_one.is_present():
            self.region.upgrade_border.multiplier_one.click()

        # If the upgrades menu is closed or we are on a different category, open it
        if self.region.upgrade_border.title.read(type = ValueType.STRING) != "ATTACK UPGRADES":
            self.region.categories.attack.click()

        self.reader.start()

        # Reset all category settings to initial state
        for category in self.region.categories.all:
            if not self.region.upgrade_border.multiplier_one.is_present():
                self.region.upgrade_border.multipliers.click()
            self.region.upgrade_border.multiplier_one.click()

            for _ in range(10):
                self.region.upgrades.first_left.name.id = f"playing.upgrades.{category.id}.first_left.name"
                if self.region.upgrades.first_left.name.read(type = ValueType.STRING) != category.first:
                    self.region.upgrades.scroll(-2)
                else:
                    break
            else:
                raise Exception(f"Failed to scroll to the top of the {category.id} category")

            if category.id.endswith("attack"):
                self.region.categories.defence.click()
            elif category.id.endswith("defence"):
                self.region.categories.utility.click()

        self.adwatcher.start()
        self.algorithm.start()

        while True:
            if self.region.game_over_modal.is_present():
                print("[GAME_ADWATCHER] Game over modal is present, retrying")
                self.region.game_over_modal.retry_button.click()
                self.reset()
            time.sleep(5)