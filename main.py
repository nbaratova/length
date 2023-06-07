"""
This is a length bot.
It echoes any incoming text messages.
"""

import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6149940727:AAEe4Yem7SMs1w2gBYurVO7lm8lE5iJSq8E'
PROXY_URL = "http://proxy.server:3128"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to our bot!")


@dp.message_handler()
async def get_length(message: types.Message):
    s = message.text.split()
    my_map = dict()

    for i in s:
        if i in my_map:
            my_map[i] += 1
        else:
            my_map[i] = 1

    my_list = list()
    for x in range(5):
        try:
            first_max = max(my_map, key=my_map.get)
            my_list.append(f"{first_max} = {my_map[first_max]}")
            del my_map[first_max]
        except:
            pass

    await message.answer(str(my_list))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
