import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Supun = Client(
    "Reply Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)
START_TEXT = """
හායි {}, I am a image background remover bot. Send me a photo I will send the photo without background.
Made by [BioHazard Bots](t.me/BioHazard_Bots).
"""
