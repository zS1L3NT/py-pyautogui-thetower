from constants import *
from engine import engine
from telegram.handler import TelegramHandler
import pyautogui as ui
import threading
import logging
import time
import sys

ui.MINIMUM_DURATION = 0.005
ui.MINIMUM_SLEEP = 0.005
timestamp = time.strftime('%Y-%m-%d %H-%M-%S')
threading.current_thread().name = "MAIN"

logging.basicConfig(
    handlers=[
        logging.FileHandler(f"logs/{timestamp}.log"),
        logging.StreamHandler(sys.stdout),
        TelegramHandler(),
    ],
    level=logging.INFO,
    format="%(asctime)s - %(threadName)s - %(message)s"
)

logging.info(f"Starting engine @ {timestamp}")

engine.start()