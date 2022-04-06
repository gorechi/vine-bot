from requests_html import AsyncHTMLSession
from teleprint import tprint

async def l_wine(message):
    search_string = message.text
    session = AsyncHTMLSession()
    link = 'https://l-wine.ru/collection/?'
    headers = {
    'authority': 'l-wine.ru',
    'cache-control': 'no-store, no-cache, must-revalidate',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'sec-fetch-dest': 'empty',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'origin': 'https://l-wine.ru',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    }
    params = {
        'q': search_string,
        'PAGEN_1': '2',
        'bxajaxid': '556e3da235ad5f10fd6e4d11c79000cf',
        'parent_bxajaxid': '5a96feaafb623ec95f9c643be02cc78f'
    }
    
    r = await session.get(link, headers=headers, params=params)
    #await r.html.arender(timeout=20)
    print(r.text)