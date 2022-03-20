from aiogram import Bot, Dispatcher, executor, types
from simple_wine import simple_wine
from am import am_wine
from winestyle import winestyle
from settings import TOKEN
import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
functions = [
    simple_wine,
    am_wine,
    winestyle,
]

@dp.message_handler()
async def all_commands(message: types.Message):
    wine_name = message.text
    tasks = []
    for function in functions:
        tasks.append(asyncio.create_task(function(message)))
    
    for task in tasks:
        await task

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)