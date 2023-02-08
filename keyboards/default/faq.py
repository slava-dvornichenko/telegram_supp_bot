from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
faq=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Что такое VPN?"),KeyboardButton(text="Законность VPN"),KeyboardButton(text="Законность обхода блокировки"),],[KeyboardButton(text="Преимущества вашего VPN"),KeyboardButton(text="Поддержка устройствами"),KeyboardButton(text="Преимущества платного VPN"),],[KeyboardButton(text="Вернуться в меню")],], resize_keyboard=True)

starting=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="FAQ"),KeyboardButton(text="Связаться с техподдержкой")],],resize_keyboard=True)