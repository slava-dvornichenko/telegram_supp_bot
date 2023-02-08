from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from aiogram.types import Message
from keyboards.default import starting
from aiogram.dispatcher.filters import Text


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Добро пожаловать, <b>, {message.from_user.full_name} </b> !\nЯ - бот, созданный, чтобы помочь и ответить на все ваши вопросы! \nВыберите на клавиатуре '\n'FAQ'- чтобы получить общие ответы на вопросы. \n'Связаться с техподдержкой' - чтобы получить помощь от поддержки.  ",parse_mode="HTML",reply_markup=starting)

