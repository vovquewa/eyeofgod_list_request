"""
Telegram message to EyeOfGod
"""

from os import getenv
from re import DEBUG
from time import sleep, time
from datetime import datetime

from pyrogram import Client
from dotenv import load_dotenv
from tqdm import tqdm


load_dotenv()

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BOT_NAME = getenv("BOT_NAME")
PHONE_LIST_FILE = "phone_list.txt"

DEBUG = True

if DEBUG:
    BOT_NAME = "me"


def get_phone_list() -> list[str]:
    """Getting list of phones from file"""
    with open(PHONE_LIST_FILE, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def main():
    client = Client("my_account", api_id=API_ID, api_hash=API_HASH)

    client.start()

    prone_list = get_phone_list()

    for phone in tqdm(prone_list, "Sending messages"):
        client.send_message(BOT_NAME, phone)
        sleep(5)

    messages = client.get_chat_history(BOT_NAME, limit=len(prone_list) * 2)
    with open(
        f'history/chat_history_{datetime.fromtimestamp(time()).strftime("%Y-%m-%d %H:%M:%S")}.txt',
        "w",
        encoding="utf-8",
    ) as file:
        for message in messages:
            file.write(message.text + "\n" + "***" + "\n")

    client.stop()


if __name__ == "__main__":
    main()
