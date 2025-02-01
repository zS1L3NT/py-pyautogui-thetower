from constants import *
from regions.game import game_region
from utilities.parser import ValueType
from utilities.windows import switch_to_game, center_game
from .processes.adwatcher import adwatcher
from .processes.algorithm import algorithm
from .processes.reader import reader
from .processes.retry import retry

class Engine:
    def start(self):
        playing_region = game_region.playing

        switch_to_game()
        center_game()

        # Close any initially opened modals
        # We click on menu because it's a position where it doesn't affect reading of values
        #   or the game itself, it's just a visual thing
        playing_region.menu.toggle.click()

        # The only modal we can't close is the game over modal, so we need to check if it's present
        if playing_region.modals.game_over.is_present():
            playing_region.modals.game_over.retry_button.click()

        # Hide the multiplier select if it's present so we can read the category name
        if playing_region.upgrade_border.multiplier_one.is_present():
            playing_region.upgrade_border.multiplier_one.click()

        # If the upgrades menu is closed or we are on a different category, open it
        if playing_region.upgrade_border.title.read(type = ValueType.STRING) != "ATTACK UPGRADES":
            playing_region.categories.attack.click()

        reader.start()

        # Reset all category settings to initial state
        for category in playing_region.categories.all:
            if not playing_region.upgrade_border.multiplier_one.is_present():
                playing_region.upgrade_border.multipliers.click()
            playing_region.upgrade_border.multiplier_one.click()

            for _ in range(10):
                playing_region.upgrades.first_left.name.id = f"playing.upgrades.{category.id}.first_left.name"
                if playing_region.upgrades.first_left.name.read(type = ValueType.STRING) != category.first:
                    playing_region.upgrades.scroll(-2)
                else:
                    break
            else:
                raise Exception(f"Failed to scroll to the top of the {category.id} category")

            if category.id.endswith("attack"):
                playing_region.categories.defence.click()
            elif category.id.endswith("defence"):
                playing_region.categories.utility.click()

        adwatcher.start()
        algorithm.start()
        retry.start()

engine = Engine()