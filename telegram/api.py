import requests
import json
import os

CHAT_ID = str(os.getenv("TELEGRAM_CHAT_ID"))
TOKEN = str(os.getenv("TELEGRAM_BOT_TOKEN"))

class TelegramAPI:
    @staticmethod
    def send_message(message: str):
        response = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage", data = {
                'chat_id': CHAT_ID,
                'text': message,
                'parse_mode': 'Markdown'
            }
        )
        response.raise_for_status()
        return response

    @staticmethod
    def pin_message(message_id: int):
        response = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/pinChatMessage", data = {
                'chat_id': CHAT_ID,
                'message_id': message_id
            }
        )
        response.raise_for_status()
        return response

    @staticmethod
    def send_video(path: str):
        with open(path, 'rb') as file:
            response = requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendVideo",
                data = { 'chat_id': CHAT_ID, },
                files = { 'video': file }
            )
            response.raise_for_status()
            return response

    @staticmethod
    def send_media_group(media: list[tuple[str, str, str]]):
        response = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMediaGroup",
            data = {
                'chat_id': CHAT_ID,
                'media': json.dumps([{
                    "type": _type,
                    "media": f"attach://{name.lower()}",
                    "caption": name
                } for _type, name, _ in media])
            },
            files = { name.lower(): open(path, 'rb') for _, name, path in media }
        )
        response.raise_for_status()
        return response
