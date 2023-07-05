from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("Главное меню")
b2 = KeyboardButton("Добавление работы в базу")

main_command_board = ReplyKeyboardMarkup(resize_keyboard=True)

main_command_board.add(b1).add(b2)
