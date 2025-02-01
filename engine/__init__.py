from constants import *
from regions.game import region
from utilities.parser import ValueType
from utilities.windows import switch_to_game, center_game
from .processes.adwatcher import adwatcher
from .processes.algorithm import algorithm
from .processes.reader import reader
from .processes.retry import retry

class Engine:
    def start(self):
        switch_to_game()
        center_game()

        # Close any initially opened modals
        # We click on menu because it's a position where it doesn't affect reading of values
        #   or the game itself, it's just a visual thing
        region.playing.menu.toggle.click()

        # The only modal we can't close is the game over modal, so we need to check if it's present
        if region.playing.modals.game_over.is_present():
            region.playing.modals.game_over.retry_button.click()

        # Hide the multiplier select if it's present so we can read the category name
        if region.playing.upgrade_border.multiplier_one.is_present():
            region.playing.upgrade_border.multiplier_one.click()

        # If the upgrades menu is closed or we are on a different category, open it
        if region.playing.upgrade_border.title.read(type = ValueType.STRING) != "ATTACK UPGRADES":
            region.playing.categories.attack.click()

        reader.start()

        # Reset all category settings to initial state
        for category in region.playing.categories.all:
            if not region.playing.upgrade_border.multiplier_one.is_present():
                region.playing.upgrade_border.multipliers.click()
            region.playing.upgrade_border.multiplier_one.click()

            for _ in range(10):
                region.playing.upgrades.first_left.name.id = f"playing.upgrades.{category.id}.first_left.name"
                if region.playing.upgrades.first_left.name.read(type = ValueType.STRING) != category.first:
                    region.playing.upgrades.scroll(-2)
                else:
                    break
            else:
                raise Exception(f"Failed to scroll to the top of the {category.id} category")

            if category.id.endswith("attack"):
                region.playing.categories.defence.click()
            elif category.id.endswith("defence"):
                region.playing.categories.utility.click()

        adwatcher.start()
        algorithm.start()
        retry.start()

engine = Engine()