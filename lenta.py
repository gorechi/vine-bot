from teleprint import tprint

async def lenta(message:object, session:object) -> None:
    search_string = message.text
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    link = f'https://lenta.com/api/v1/search'
    params = {
        'value': search_string,
    }
    r = await session.get(link, headers=headers, params=params)
    await r.html.arender(sleep=3)
    result = ['<b>Lenta</b>']
    if r.status_code == 200:
        products = r.json()['skus']
        if products:
            for product in products:
                link = product['url']
                result.append(f'<a href = "{link}">{product["title"]}</a> - <b>{product["regularPrice"]["value"]}</b> ₽')
        else:
            result.append('Ничего не найдено.')
    else:
        result.append('Этот магазин сейчас недоступен.')
    await tprint(message, result)

