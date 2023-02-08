from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запуск бота"),
        types.BotCommand("faq", "Справка по общим вопросам"),
        types.BotCommand("support_call", "Связаться с техподдержкой"),
        types.BotCommand("help", "Помощь"),
    ])