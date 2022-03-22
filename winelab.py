from requests_html import AsyncHTMLSession
from teleprint import tprint

async def winelab(message):
    search_string = message.text
    session = AsyncHTMLSession()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    link = f'https://www.winelab.ru/search?text={search_string}'
    link = link.replace(' ', '%20')
    r = await session.get(link, headers=headers)
    print(dir(r))
    print(r.content)
    await r.html.arender(sleep=3)
    result = ['Winestyle']
    if r.status_code == 200:
        prices = r.html.find('.price-container .price')
        titles = r.html.find('.item-header .title')
        if len(prices) > 0:
            for i in range(len(prices)):
                s = f'{titles[i].text} - {prices[i].text}'
                result.append(s)
        else:
            result.append('Ничего не найдено.')
    else:
        result.append('Этот магазин сейчас недоступен.')
    await tprint(message, result)

