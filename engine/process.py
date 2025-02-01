from threading import Event, Thread
import logging
import time

class Process:
    id = ""
    __thread: Thread
    __stop_event: Event

    def is_stopped(self):
        return self.__stop_event.is_set()

    def start(self):
        logging.info(f"▶︎ Starting {self.id.lower()} thread")
        self.__stop_event = Event()
        self.__thread = Thread(target = self.run, name = self.id)
        self.__thread.start()

    def stop(self):
        logging.info(f"⏸︎ Stopping {self.id.lower()} thread")
        self.__stop_event.set()

    def run(self):
        while not self.__stop_event.is_set():
            try:
                self.iteration()
            except Exception as e:
                logging.error(f"❗ Process {self.id} failed with error: {e}", exc_info = True)
                time.sleep(5)

    def iteration(self) -> None:
        raise NotImplementedError("Iteration not implemented")