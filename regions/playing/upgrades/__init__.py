from constants import *
from regions import Region
from regions.playing.upgrades.upgrade import Upgrade
import pyautogui as ui
import time

class Upgrades(Region):
    id = "playing.upgrades"
    x = GAME_CENTER_X - 276 - 6
    y = GAME_CENTER_Y + 162
    width = 560
    height = 308

    first_left = Upgrade(0)
    first_right = Upgrade(1)
    second_left = Upgrade(2)
    second_right = Upgrade(3)
    last_left = Upgrade(4)
    last_right = Upgrade(5)

    def scroll(self, upgrades: int):
        center_x = self.x + self.width / 2
        height = 108 + 8 + 1

        ui.mouseDown(center_x, self.y + height)
        ui.dragRel(0, -height * upgrades, 0.25, button = "left", mouseDownUp = False)
        time.sleep(0.5)
        ui.mouseUp(center_x, self.y + height)

    def scroll_fix(self):
        center_x = self.x + self.width / 2
        height = 108 + 8 + 1
        reset_height = 40

        ui.mouseDown(center_x, self.y + height)
        ui.dragRel(0, reset_height, 0.25, button = "left", mouseDownUp = False)
        time.sleep(0.5)
        ui.mouseUp(center_x, self.y + height)