"""
This is a length bot.
It echoes any incoming text messages.
"""

import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6149940727:AAEe4Yem7SMs1w2gBYurVO7lm8lE5iJSq8E'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to our bot!")


@dp.message_handler()
async def get_length(message: types.Message):
    length = len(message.text)
    await message.answer(length)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
