from engine.game import GameEngine
from regions.game import GameRegion
from constants import *
from enum import Enum
import pyautogui as ui

class EngineScreen(Enum):
    Home = "home"
    Playing = "playing"

class Engine:
    screen = EngineScreen.Home
    region: GameRegion
    game_engine: GameEngine

    def __init__(self):
        self.region = GameRegion()
        self.region.cascade()

        self.game_engine = GameEngine(self.region)

        self.switch_to_game()
        self.center_game()

    def switch_to_game(self):
        ui.keyDown("command")
        ui.press("tab")
        coords = ui.locate(
            "app.png",
            ui.screenshot(region=(0, SCREEN_CENTER_Y - 90, SCREEN_WIDTH, 180)),
            grayscale=True,
            confidence=0.8,
        )
        ui.leftClick(coords.left + coords.width / 2, SCREEN_CENTER_Y)
        ui.keyUp("command")

    def center_game(self):
        ui.keyDown("command")   
        ui.press("space")
        ui.keyUp("command")
        ui.typewrite("center")
        ui.press("enter")

    def start(self):
        if self.screen != EngineScreen.Home:
            print(f"Cannot start engine when game is on {self.screen} screen")
            return

        self.region.home.battle_button.click()

        self.game_engine.start()