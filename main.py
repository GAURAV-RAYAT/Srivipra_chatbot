from boltiotai import openai

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from example import example

bot = Bot(token='7228746620:AAGT94xbeJxbcAsxwDPGuT5wqia_OXqi_fc')

dp = Dispatcher()

openai.api_key = "aYJ74AVbRfBdKV9gZglxbFc080PLlXsb89iZFRKlbFU"

example()


@dp.message(CommandStart(['start', 'help']))
async def welcome(message: types.Message):
  await message.reply('')


@dp.message()
async def gpt(message: types.Message):
  messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role":"user", "content":message.text}]
  
  response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

  await message.reply(response['choices'][0]['message']['content'])

async def main():
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())