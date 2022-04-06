from teleprint import tprint

async def metro(message, session):
    search_string = message.text
    search_string = search_string.replace(' ', '+')
    link = f'https://online.metro-cc.ru/search'
    headers = {
    'authority': 'api.metro-cc.ru',
    'method': 'GET',
    'path': f'/api/v1/C98BB1B547ECCC17D8AEBEC7116D6/10/search?q={search_string}&limit=30&content=1&page=1&in_stock=0',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'allowedCookieCategories=default%7Cnecessary; metroStoreId=10; _gcl_au=1.1.251935474.1647972954',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'nuxt-environment': 'nuxt_client',   
    'origin': 'https://online.metro-cc.ru',
    'referer': 'https://online.metro-cc.ru/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
    }
    params = {
        'q': search_string,
        'limit': 30,
        'content': 1,
        'page': 1,
        'in_stock': 0
    }
    result = ['Metro']
    r = await session.get(link, headers=headers, params=params)
    print(r)
    print(r.request)
    print(r.text)
    print(dir(r))
    if r.status_code == 200:
        products = r.json()['data']['products']
        if products:
            for product in products:
                result.append(f'{product["name"]} - {product["prices"]["price"]} ₽')
        else:
            result.append('Ничего не найдено.')
    else:
        result.append('Этот магазин сейчас недоступен.')
    await tprint(message, result)
    return result