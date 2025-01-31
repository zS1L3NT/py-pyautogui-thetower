from constants import *
from region import Region
from .upgrade import UpgradeRegion
import pyautogui as ui
import time

class UpgradesRegion(Region):
    id = "playing.upgrades"
    x = GAME_CENTER_X - 276 - 6
    y = GAME_CENTER_Y + 162
    width = 560
    height = 308

    first_left = UpgradeRegion(0)
    first_right = UpgradeRegion(1)
    second_left = UpgradeRegion(2)
    second_right = UpgradeRegion(3)
    last_left = UpgradeRegion(4)
    last_right = UpgradeRegion(5)

    def scroll(self, upgrades: int):
        center_x = self.x + self.width / 2
        height = 108 + 8 + 1

        ui.mouseDown(center_x, self.y + height)
        ui.dragRel(0, -height * upgrades, 0.25, button = "left", mouseDownUp = False)
        time.sleep(0.5)
        ui.mouseUp(center_x, self.y + height)

    def scroll_last(self, direction: int):
        center_x = self.x + self.width / 2
        height = 108 + 8 + 1
        last_height = 40

        ui.mouseDown(center_x, self.y + height)
        ui.dragRel(0, -last_height * direction, 0.25, button = "left", mouseDownUp = False)
        time.sleep(0.5)
        ui.mouseUp(center_x, self.y + height)