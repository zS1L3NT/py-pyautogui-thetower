from constants import *
from regions import Region

class BattleButton(Region):
    id = "home.battle_button"
    x = GAME_CENTER_X - 140
    y = 804
    width = 280
    height = 108
    image = __file__.replace(".py", ".png")