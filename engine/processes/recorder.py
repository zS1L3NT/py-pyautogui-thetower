from threading import Thread
import logging
import time
import os

class Recorder:
    id = "RECORDER"

    def start(self, duration: int = 10):
        logging.info(f"▶︎ Starting {self.id.lower()} thread")
        thread = Thread(target = self.run, args = (duration,), name = self.id)
        thread.start()

    def run(self, duration: int):
        os.system(f"screencapture -V{duration} \"logs/videos/{time.strftime("%Y-%m-%d %H-%M-%S")}.mp4\"")
        logging.info(f"⏸︎ Stopping {self.id.lower()} thread")

recorder = Recorder()