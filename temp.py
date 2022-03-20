from requests_html import AsyncHTMLSession, HTML
from aiogram import Bot, Dispatcher, executor, types
from simple_wine import simple_wine
wine_name = 'trimbach riesling'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
session = AsyncHTMLSession()
async def tprint (message, text):
    if isinstance(text, str):
        await message.reply(text)
    elif isinstance(text, list):
        final_text = ''
        for line in text:
            final_text = final_text + str(line) + '\n'
        await message.reply(final_text.rstrip('\n'))
async  def winestyle_find(message):
    global headers
    global wine_name
    global session
    global bot
    link = f'https://winestyle.ru/catalog/?search_query={wine_name}'
    link = link.replace(' ', '%20')
    print(link)
    r = await session.get(link, headers=headers)
    await r.html.arender(sleep=3)
    if r.status_code == 200:
        result = ['Winestyle: ']
        prices = r.html.find('.price-container .price')
        titles = r.html.find('.item-header .title')
        for i in range(len(prices)):
            s = titles[i].text + ': ' + prices[i].text
            print(s)
            result.append(s)
        await tprint(message, result)
        return result
    else:
        return False
async  def am_wine(message):
    global headers
    global wine_name
    global session
    global bot
    link = f'https://amwine.ru/?digiSearch=true&term={wine_name}&params=%7Csort%3DDEFAULT'
    link = link.replace(' ', '%20')
    print(link)
    r = await session.get(link, headers=headers)
    await r.html.arender(sleep=3)
    print(dir(r.html))
    print(r.html.html)
    if r.status_code == 200:
        result = ['Ароматный мир: ']
        prices = r.html.find('.digi-product__main .digi-product__price')
        titles = r.html.find('.digi-product__main .digi-product__brand')
        for i in range(len(prices)):
            s = titles[i].text + ': ' + prices[i].text
            print(s)
            result.append(s)
        await tprint(message, result)
        return result
    else:
         return False
async  def simple_wine():
    global headers
    global wine_name
    global session
    search_text = wine_name.replace(' ', '+')
    link = f'https://simplewine.ru/ajax/v2/search/suggesters/?q={search_text}&suggestionCount={s_sw_suggestion_count}&productCount={s_sw_product_count}'
    print(link)
    r = await session.get(link, headers=headers)
    print (r)
    await r.html.arender(sleep=3)
    if r.status_code == 200:
        result = ['Simple Wine: ']
        items = r.html.find('.digi-product-grid', first=True)
        prices = items.find('.digi-product-price')
        titles = items.find('.digi-product-label')
        for i in range(len(prices)):
            s = titles[i].text + ': ' + prices[i].text
            result.append(s)
        return result
    else:
        return False