"""
Telegram message to EyeOfGod
"""

import os
from os import getenv
from re import DEBUG
from time import sleep
from datetime import datetime

from pyrogram import Client
from tqdm import tqdm
from dotenv import load_dotenv


load_dotenv()

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BOT_NAME = getenv("BOT_NAME")
PHONE_LIST_FILE = "phone_list.txt"

DEBUG = False

if DEBUG:
    BOT_NAME = "me"


def get_phone_list() -> list[str]:
    """Getting list of phones from file"""
    with open(PHONE_LIST_FILE, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def send_messages(client, prone_list):
    """Send messages to the bot"""
    for phone in tqdm(prone_list, "Sending messages"):
        client.send_message(BOT_NAME, phone)
        sleep(5)


def save_chat_history(client, prone_list):
    """Save chat history to a file"""
    messages = client.get_chat_history(BOT_NAME, limit=len(prone_list) * 2)

    history_dir = "history"
    os.makedirs(history_dir, exist_ok=True)

    new_filename = f'chat_history_{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.txt'
    new_filepath = os.path.join(history_dir, new_filename)

    mode = "a" if os.path.exists(new_filepath) else "w"
    print(
        f"{'Appending to' if mode == 'a' else 'Creating'} history file: {new_filename}"
    )

    with open(new_filepath, mode, encoding="utf-8") as file:
        for message in tqdm(messages, "Saving result"):
            file.write(f"{message.text}\n***\n")


def main():
    """Main script"""
    with Client("my_account", api_id=API_ID, api_hash=API_HASH) as client:
        prone_list = get_phone_list()
        send_messages(client, prone_list)
        save_chat_history(client, prone_list)


if __name__ == "__main__":
    main()
