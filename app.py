from engine import engine
from constants import *
import pyautogui as ui
import logging
import time
import sys

ui.MINIMUM_DURATION = 0.005
ui.MINIMUM_SLEEP = 0.005

logging.basicConfig(
    handlers=[
        logging.FileHandler(f"logs/{time.strftime('%Y-%m-%d %H-%M-%S')}.log"),
        logging.StreamHandler(sys.stdout)
    ],
    level=logging.INFO,
    format="%(asctime)s - %(threadName)s - %(message)s"
)

engine.start()