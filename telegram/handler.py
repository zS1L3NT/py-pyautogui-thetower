import traceback
import logging
from .api import TelegramAPI

class TelegramHandler(logging.Handler):
    pinned = False

    def emit(self, record: logging.LogRecord):
        [_, thread, message] = self.format(record).split(" - ")
        if record.exc_info:
            message = "".join(traceback.format_exception(*record.exc_info))

        response = TelegramAPI.send_message(f"```{thread}\n{message}\n```")

        if not self.pinned:
            self.pinned = True
            TelegramAPI.pin_message(response.json()['result']['message_id'])