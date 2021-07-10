from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api.postgres import Database
from config.config import DATABASE_URL


db = Database(DATABASE_URL)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not db.get_user(message.from_user.id):
        db.add_user(message.from_user.username, message.from_user.first_name, message.from_user.id)
        await message.answer(message.from_user.id)
        return
    await message.answer('Я уже запущен')
