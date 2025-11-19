from balethon import Client
import os

bot = Client(os.getenv("TOKEN"))

bot.run()