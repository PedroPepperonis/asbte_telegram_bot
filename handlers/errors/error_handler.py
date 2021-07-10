import logging
from aiogram.utils.exceptions import BotBlocked

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    if isinstance(exception, BotBlocked):
        logging.exception('Пользователь заблокировал бота')
        return True

    logging.exception(f'Update {update}\n{exception}')
