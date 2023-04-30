from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os

storage = MemoryStorage()
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
