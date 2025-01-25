from constants import *
from regions import Region
from regions.home.battle_button import BattleButton

class HomeScreen(Region):
    id = "home"
    width = GAME_WIDTH
    height = GAME_HEIGHT

    battle_button = BattleButton()