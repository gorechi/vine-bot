import requests

def winestyle(search_string):
    search_string = search_string.replace(' ', '+')
    link = f'https://winestyle.ru/remote.php'
    headers = {
        'Host': 'winestyle.ru',
        'Referer': 'https://winestyle.ru/catalog/?search_query=riesling',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        }
    params = {
        'r': 0.10271848365681024,
        'w': 'loadmoreproducts',
        'search_query': search_string,
        'sort': 'productpopularity',
        'searchlimit': 0,
        'ajax': 1
    }
        
    r = requests.get(link, headers=headers, params=params)
    print(r.text)
    result = []
    if products:
        for product in products:
            print(f'{product["title"]} - {product["priceSchema"]} ₽')
            result.append(f'{product["title"]} - {product["priceSchema"]} ₽')
    else:
        print('Ничего не найдено')
        result.append('Ничего не найдено')
    return result

winestyle('riesling')