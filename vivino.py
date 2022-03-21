from requests_html import AsyncHTMLSession
from teleprint import tprint

async def vivino(message):
    search_string = message.text
    session = AsyncHTMLSession()
    
    headers = {
    'accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '41',
    'content-type': 'application/x-www-form-urlencoded',
    'Host': '9takgwjuxl-dsn.algolia.net',
    'Origin': 'https://www.vivino.com',
    'Referer': 'https://www.vivino.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
    }
    
    params = {
        'x-algolia-agent': 'Algolia for JavaScript (3.33.0); Browser (lite)',
        'x-algolia-application-id': '9TAKGWJUXL',
        'x-algolia-api-key': '60c11b2f1068885161d95ca068d3a6ae'
    }
    
    payload = '{"params":"query=' + search_string + '&hitsPerPage=6"}'
    
    print(payload)
    link = f'https://9takgwjuxl-dsn.algolia.net/1/indexes/WINES_prod/query'
    r = await session.post(link, headers=headers, data=payload.encode('utf-8'), params=params)
    print(r.headers, r.json())
    result = ['Vivino']
    
    if r.status_code == 200:
        products = r.json()['hits']
        if products:
            for product in products:
                result.append(f'{product["winery"]["name"]} {product["name"]} - {product["statistics"]["ratings_average"]} ({product["statistics"]["ratings_count"]} голосов.)')
        else:
            result.append('Ничего не найдено.')
    else:
        result.append('Этот сайт сейчас недоступен.')
    await tprint(message, result)

