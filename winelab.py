from requests_html import AsyncHTMLSession
from teleprint import tprint

async def winelab(message):
    search_string = message.text
    session = AsyncHTMLSession()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    link = f'https://www.winelab.ru/search?text={search_string}'
    link = link.replace(' ', '%20')
    r = await session.get(link, headers=headers)
    await r.html.arender()
    print(r.html.html)

