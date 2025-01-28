from engine import Engine
from constants import *
import pyautogui as ui

ui.MINIMUM_DURATION = 0.005
ui.MINIMUM_SLEEP = 0.005

engine = Engine()
engine.game_engine.run()