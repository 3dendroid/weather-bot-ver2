from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Command list: ",
            "/start - Start a dialogue",
            "/help - Get help")

    await message.answer("\n".join(text))
