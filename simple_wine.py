from requests_html import AsyncHTMLSession
from teleprint import tprint

async def simple_wine(message):
    search_string = message.text
    session = AsyncHTMLSession()
    suggestion_count = 3
    product_count = 10
    search_string = search_string.replace(' ', '+')
    link = f'https://simplewine.ru/ajax/v2/search/suggesters/?q={search_string}&suggestionCount={suggestion_count}&productCount={product_count}'
    headers = {
    'authority': 'simplewine.ru',
    'cache-control': 'no-store, no-cache, must-revalidate, private',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.3',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    result = ['Simple Wine']
    r = await session.get(link, headers=headers)
    if r.status_code == 200:
        products = r.json()['data']['products']
        if products:
            for product in products:
                print(f'{product["title"]} - {product["priceSchema"]} ₽')
                result.append(f'{product["title"]} - {product["priceSchema"]} ₽')
        else:
            print('Ничего не найдено')
            result.append('Ничего не найдено.')
    else:
        result.append('Этот магазин сейчас недоступен.')
    await tprint(message, result)
    return result