from aiogram import types

async def tprint (message:types.Message, text:list) -> None:
    if isinstance(text, str):
        await message.reply(text)
    elif isinstance(text, list):
        final_text = ''
        for line in text:
            final_text = final_text + str(line) + '\n'
        await message.reply(final_text.rstrip('\n'), parse_mode=types.ParseMode.HTML)