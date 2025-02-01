from subprocess import Popen, PIPE
import logging
import time

class Recorder:
    id = "RECORDER"
    process: Popen[bytes]

    def start(self):
        logging.info(f"▶︎ Starting {self.id.lower()}")
        self.process = Popen(f"screencapture -v \"logs/videos/{time.strftime("%Y-%m-%d %H-%M-%S")}.mp4\"", stdin = PIPE, stdout = PIPE, shell = True)

        time.sleep(1)

    def stop(self):
        time.sleep(1)

        logging.info(f"⏸︎ Stopping {self.id.lower()}")
        self.process.communicate(input = b" ")

recorder = Recorder()