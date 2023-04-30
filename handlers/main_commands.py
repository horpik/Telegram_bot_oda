from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from create_bot import bot
from keyboards import main_action, main_choice_hairstyle, main_command_board

TEXT_START_PROGRAM = "Выбери раздел, который ты будешь использовать"
TEXT_HAIRSTYLE = "Выбери тип фотографии, которую будешь добавлять"


async def command_start(message: types.Message):
    global TEXT_START_PROGRAM
    await bot.send_message(message.from_user.id,
                           'Приветик! Я очень рад, что ты используешь меня!\n')
    await message.delete()
    await bot.send_message(message.from_user.id,
                           TEXT_START_PROGRAM,
                           reply_markup=main_action)


async def main_start(message: types.Message):
    global TEXT_START_PROGRAM
    await message.delete()
    await bot.send_message(message.from_user.id,
                           f"Начнём сначала {TEXT_START_PROGRAM}",
                           reply_markup=main_action)


async def open_window_choice_hairstyle(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(TEXT_HAIRSTYLE, reply_markup=main_choice_hairstyle)
    await call.message.delete()


def register_handlers_main_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'], is_chat_admin=True)
    dp.register_message_handler(main_start, Text(equals="Главное меню", ignore_case=True))
    dp.register_callback_query_handler(open_window_choice_hairstyle, text_contains="choice_hairstyle")
