import traceback
import requests
import logging
import os

class TelegramHandler(logging.Handler):
    pinned = False
    chat_id = str(os.getenv("TELEGRAM_CHAT_ID"))
    token = str(os.getenv("TELEGRAM_BOT_TOKEN"))

    def emit(self, record: logging.LogRecord):
        [_, thread, message] = self.format(record).split(" - ")
        if record.exc_info:
            message = "".join(traceback.format_exception(*record.exc_info))

        response = requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", data = {
            'chat_id': self.chat_id,
            'text': f"```{thread}\n{message}\n```",
            'parse_mode': 'Markdown'
        })

        response.raise_for_status()

        if not self.pinned:
            self.pinned = True
            requests.post(f"https://api.telegram.org/bot{self.token}/pinChatMessage", data = {
                'chat_id': self.chat_id,
                'message_id': response.json()['result']['message_id']
            })
            
            response.raise_for_status()
