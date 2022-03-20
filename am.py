from requests_html import AsyncHTMLSession
from teleprint import tprint

async def am_wine(message):
    search_string = message.text
    session = AsyncHTMLSession()
    search_string = search_string.replace(' ', '%20')
    link = f'https://sort.diginetica.net/search'
    headers = {
        'authority': 'sort.diginetica.net',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'sec-fetch-dest': 'empty',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    params = {
        'st': search_string,
        'apiKey': '949JF9H5VQ',
        'strategy': 'vectors_extended,zero_queries',
        'fullData': 'true',
        'withCorrection': 'true',
        'withFacets': 'true',
        'treeFacets': 'true',
        'regionId': 'Москва',
        'useCategoryPrediction': 'true',
        'size': 20,
        'offset': 0,
        'showUnavailable': 'true',
        'unavailableMultiplier': 0.2,
        'preview': 'false',
        'withSku': 'false',
        'sort': 'PRICE_DESC'
    }
    result = ['Ароматный мир']
    r = await session.get(link, headers=headers, params=params)
    if r.status_code == 200:
        products = r.json()['products']
        if products:
            for product in products:
                if product['price'] != '0.0':
                    print(f'{product["name"]} - {product["price"]} ₽')
                    result.append(f'{product["name"]} - {product["price"]} ₽')
        else:
            print('Ничего не найдено')
            result.append('Ничего не найдено.')
    else:
        result.append('Этот магазин сейчас недоступен.')
    await tprint(message, result)
    return result
