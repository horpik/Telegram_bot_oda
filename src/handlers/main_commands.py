import os

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot
from keyboards import main_action

TEXT_START_PROGRAM = "Выбери раздел, который ты будешь использовать"
TEXT_HAIRSTYLE = "Выбери тип фотографии, которую будешь добавлять"

user_list = os.getenv('USER_ID').replace(' ', '').split(',')


async def command_start(message: types.Message):
    if str(message.chat.id) == os.getenv('GROUP_ID') or str(message.from_user.id) in user_list:
        await bot.send_message(message.from_user.id,
                               'Приветик! Я очень рад, что ты используешь меня!\n')
        await message.delete()
        await bot.send_message(message.from_user.id,
                               TEXT_START_PROGRAM,
                               reply_markup=main_action)
    else:
        await bot.send_message(message.from_user.id,
                               'У Вас нет доступа использовать этого бота')


async def main_start(message: types.Message):
    if message.chat.id == os.getenv('GROUP_ID'):
        await message.delete()
        await bot.send_message(message.from_user.id,
                               f"Начнём сначала {TEXT_START_PROGRAM}",
                               reply_markup=main_action)
    else:
        await bot.send_message(message.from_user.id,
                               'У Вас нет доступа использовать этого бота')


def register_handlers_main_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(main_start, Text(equals="Главное меню", ignore_case=True))
