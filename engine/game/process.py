from threading import Event, Thread

class Process:
    id = ""
    name = ""
    thread: Thread
    stop_event: Event

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def start(self):
        print(f"[{self.id}] Starting {self.name} thread")
        self.stop_event = Event()
        self.thread = Thread(target = self.run)
        self.thread.start()

    def stop(self):
        print(f"[{self.id}] Stopping {self.name} thread")
        self.stop_event.set()

    def run(self):
        pass
