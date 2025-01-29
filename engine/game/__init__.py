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
        print("[GAME_ENGINE] Any modals closed")

        # The only modal we can't close is the game over modal, so we need to check if it's present
        if self.region.game_over_modal.is_present():
            self.region.game_over_modal.retry_button.click()
            print("[GAME_ENGINE] Game over modal closed, game restarted")

        # Hide the multiplier select if it's present so we can read the category name
        if self.region.upgrade_border.multiplier_one.is_present():
            self.region.upgrade_border.multiplier_one.click()
            print("[GAME_ENGINE] Multiplier select hidden")

        # If the upgrades menu is closed or we are on a different category, open it
        if self.region.upgrade_border.title.read() != "ATTACK UPGRADES":
            self.region.categories.attack.click()
            print("[GAME_ENGINE] Attack category selected")

        # Reset all category settings to initial state
        for category in self.data.upgrades.categories:
            print(f"[GAME_ENGINE] Setting multiplier to 1x for the {category.id} category")
            if not self.region.upgrade_border.multiplier_one.is_present():
                self.region.upgrade_border.multipliers.click()
            self.region.upgrade_border.multiplier_one.click()

            print(f"[GAME_ENGINE] Scrolling to the top of the {category.id} category")
            for _ in range(10):
                self.region.upgrades.first_left.name.id = f"playing.upgrades.{category.id}.first_left.name"
                if self.region.upgrades.first_left.name.read() != category.first:
                    self.region.upgrades.scroll(-2)
                else:
                    break
            else:
                raise Exception(f"Failed to scroll to the top of the {category.id} category")

            category = category.id
            if category == "attack":
                self.region.categories.defence.click()
            elif category == "defence":
                self.region.categories.utility.click()
            elif category == "utility":
                self.region.categories.attack.click()

        self.reader.run()
        self.algorithm.run()
