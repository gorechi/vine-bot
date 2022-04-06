from aiogram import Bot, Dispatcher, executor, types
from simple_wine import simple_wine
from am import am_wine
from winestyle import winestyle
from vivino import vivino
from winelab import winelab
from l_wine import l_wine
from metro import metro
from settings import TOKEN
import asyncio
from requests_html import AsyncHTMLSession

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
session = AsyncHTMLSession()
functions = [
   am_wine,
   winestyle,
   simple_wine,
   vivino
]

@dp.message_handler()
async def all_commands(message: types.Message):
    global session
    tasks = []
    for function in functions:
        tasks.append(asyncio.create_task(function(message, session)))
    
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)