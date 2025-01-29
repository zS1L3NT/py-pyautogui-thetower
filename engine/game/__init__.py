from constants import *
from engine.game.algorithm import GameAlgorithm
from engine.game.reader import GameReader
from engine.game.data import GameData
from regions.playing import PlayingRegion

class GameEngine:
    data = GameData()
    region: PlayingRegion

    reader: GameReader
    algorithm: GameAlgorithm

    def __init__(self, region: PlayingRegion):
        self.region = region

        self.reader = GameReader(self.data, self.region)
        self.algorithm = GameAlgorithm(self.data, self.region)

    def end(self):
        if not self.region.playing.menu.end_button.is_present():
            self.region.playing.menu.toggle.click()

        self.region.playing.menu.end_button.click()
        self.region.playing.end_game_modal.yes_button.click()

    def run(self):
        # Close any initially opened modals
        # We click on menu because it's a position where it doesn't affect reading of values
        #   or the game itself, it's just a visual thing
        self.region.menu.toggle.click()

        # The only modal we can't close is the game over modal, so we need to check if it's present
        if self.region.game_over_modal.is_present():
            self.region.game_over_modal.retry_button.click()

        # If the upgrades menu is closed or we are on a different category, open it
        if self.region.upgrade_border.title.read() != "ATTACK":
            self.region.categories.attack.click()

        # Set the upgrade multiplier to 1x
        if not self.region.upgrade_border.multiplier_one.is_present():
            self.region.upgrade_border.multipliers.click()
        self.region.upgrade_border.multiplier_one.click()

        self.reader.run()
        self.algorithm.run()
