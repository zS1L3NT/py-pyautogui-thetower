from threading import Event, Thread
import time
import os

execution_time = time.strftime("%Y-%m-%d %H-%M-%S")

class Process:
    id = ""
    __thread: Thread
    __stop_event: Event

    def is_stopped(self):
        return self.__stop_event.is_set()

    def start(self):
        self.log(f"Starting {self.id.lower()} thread")
        self.__stop_event = Event()
        self.__thread = Thread(target = self.run)
        self.__thread.start()

    def stop(self):
        self.log(f"Stopping {self.id.lower()} thread")
        self.__stop_event.set()

    def log(self, message: str):
        message = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] <{self.id}> {message}"
        print(message)
        with open(os.path.join("logs", "shells", f"{execution_time}.log"), "a") as file:
            file.write(f"{message}\n")

    def run(self):
        while not self.__stop_event.is_set():
            self.iteration()

    def iteration(self) -> None:
        raise NotImplementedError("Iteration not implemented")