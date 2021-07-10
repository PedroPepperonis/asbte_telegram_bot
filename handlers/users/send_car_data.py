import asyncio
import logging

from aiogram.utils.exceptions import BotBlocked

from loader import bot
from parse.parser import get_car_data
from utils.db_api.postgres import Database
from config.config import DATABASE_URL


db = Database(DATABASE_URL)


async def send_car_data(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        users = db.get_users()
        data = get_car_data()
        for i in users:
            if data:
                try:
                    await bot.send_message(i['user_id'], text=data)
                except BotBlocked:
                    logging.exception('Пользователь заблокировал бота')
