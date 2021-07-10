import asyncio

from aiogram.utils.executor import start_webhook

import handlers
from loader import dp, bot
from utils.set_bot_commands import set_default_commands
from handlers.users.send_car_data import send_car_data
from config.config import HEROKU_APP_NAME, WEBHOOK_HOST, WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL)
    await set_default_commands(dispatcher)


async def on_shutdown(dispatcher):
    return


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(send_car_data(3))
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
