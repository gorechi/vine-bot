import requests

def l_wine(search_string):
    link = 'https://l-wine.ru/local/php_interface/ajax/controller.php'
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
        'action': '\Itgrade\Lwine\Search\getHints',
        'query': search_string,
        'bxAjaxId': '29f09c2de5b5869951fb3d696731a258'
    }
    
    r = requests.post(link, headers=headers, params=params)
    '''  products = r.json()['data']['products']
    result = []
    if products:
        for product in products:
            print(f'{product["title"]} - {product["priceSchema"]} ₽')
            result.append(f'{product["title"]} - {product["priceSchema"]} ₽')
    else:
        print('Ничего не найдено')
        result.append('Ничего не найдено')
    return result '''

l_wine('chateauneuf du pape')