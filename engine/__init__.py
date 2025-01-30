from engine.game import GameEngine
from regions.game import game_region
from utilities.windows import switch_to_game, center_game
from constants import *
from enum import Enum

class EngineScreen(Enum):
    Home = "home"
    Playing = "playing"

class Engine:
    screen = EngineScreen.Home
    region = game_region
    game_engine: GameEngine

    def __init__(self):
        self.game_engine = GameEngine()

        switch_to_game()
        center_game()

    def start(self):
        if self.screen != EngineScreen.Home:
            print(f"Cannot start engine when game is on {self.screen} screen")
            return

        self.region.home.battle_button.click()

        self.game_engine.start()

engine = Engine()