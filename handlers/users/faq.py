from aiogram import types

from loader import dp


@dp.message_handler(commands='faq')
async def bot_faq(message: types.Message):
    await message.answer('Здесь будут часто задаваемые вопросы')
