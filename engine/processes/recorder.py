from telegram.api import TelegramAPI
from subprocess import Popen, PIPE
import logging
import time
import os

class Recorder:
    id = "RECORDER"
    process: Popen[bytes]
    video_path: str

    def start(self):
        logging.info(f"▶︎ Starting {self.id.lower()}")
        self.video_path = os.path.join("logs", "videos", f"{time.strftime("%Y-%m-%d %H-%M-%S")}.mp4")
        self.process = Popen(f"screencapture -v \"{self.video_path}\"", stdin = PIPE, stdout = PIPE, shell = True)

        time.sleep(1)

    def stop(self):
        time.sleep(1)

        logging.info(f"⏸︎ Stopping {self.id.lower()}")
        self.process.communicate(input = b" ")

        time.sleep(3)

        try:
            TelegramAPI.send_video(self.video_path)
        except:
            logging.error(f"❗ Failed to send video to Telegram")

recorder = Recorder()