from threading import Event, Thread

class Process:
    id = ""
    __thread: Thread
    __stop_event: Event

    def is_stopped(self):
        return self.__stop_event.is_set()

    def start(self):
        print(f"[{self.id}] Starting {self.id.lower()} thread")
        self.__stop_event = Event()
        self.__thread = Thread(target = self.run)
        self.__thread.start()

    def stop(self):
        print(f"[{self.id}] Stopping {self.id.lower()} thread")
        self.__stop_event.set()

    def run(self):
        while not self.__stop_event.is_set():
            self.iteration()

    def iteration(self) -> None:
        raise NotImplementedError("Iteration not implemented")