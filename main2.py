import requests
from bs4 import BeautifulSoup
import json

import requests

cookies2 = {
    '_ym_uid': '1677235975634360911',
    '_ym_d': '1677235975',
    '_gcl_au': '1.1.297974731.1677235975',
    '_ym_visorc': 'w',
    '_ga_6RNPXFQD1P': 'GS1.1.1677235975.1.0.1677235975.60.0.0',
    '_ga': 'GA1.2.443070273.1677235975',
    '_gid': 'GA1.2.1418173829.1677235975',
    '_gat': '1',
    '_ym_isad': '1',
}

headers2 = {
    'authority': 'g8.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru,en;q=0.9,la;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': '_ym_uid=1677235975634360911; _ym_d=1677235975; _gcl_au=1.1.297974731.1677235975; _ym_visorc=w; _ga_6RNPXFQD1P=GS1.1.1677235975.1.0.1677235975.60.0.0; _ga=GA1.2.443070273.1677235975; _gid=GA1.2.1418173829.1677235975; _gat=1; _ym_isad=1',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.2.931 Yowser/2.5 Safari/537.36',
}

response2 = requests.get('https://g8.ru/', cookies=cookies2, headers=headers2)
src2 = response2.text


# soup = BeautifulSoup(src2, "lxml")
# produt_all = soup.find("ul", id="menu-main-horizontal-menu").find_all("a")
#
#
# all_coter = {}
# for items in produt_all:
#     title_name = items.text
#     title_href = items.get("href")
#     all_coter[title_name] = title_href
#
# with open("all_cat_g8.json", "w", encoding="utf8") as file:
#     json.dump(all_coter, file, indent=4, ensure_ascii=False)
#
#
# with open("all_cat_g8.json", encoding="utf8") as File:
#     value = json.load(File)
#     text = "https://g8.ru"
# val_new = ""
# for k, v, in value.items():
#     val = v.find(text)
#     if val == 0:
#         pass
#     else:
#         val_new = text + v
#         value[k] = val_new
# with open("all_cat_g8.json", "w", encoding="utf8") as file:
#     json.dump(value, file, indent=4, ensure_ascii=False)
#
with open("all_cat_g8.json" , encoding="utf8") as file:
    all_cat = json.load(file)

count = 0
name_title_href_g8 = {}

for cat_name, cat_href in all_cat.items():


        # заменяем не нужные символы
        rep = [",", " ", "-"]
        for item in rep:
            if item in cat_name:
                cat_name = cat_name.replace(item, "_")

        req = requests.get(url=cat_href, headers=headers2)
        src = req.text

        soup = BeautifulSoup(src, "lxml")

        for tablet_name in soup.find_all('div', class_='product-inner'):
            try:
                table_nam = tablet_name.findNext("a").find("h2")
                tab_name = table_nam.text
                table_price = tablet_name.findNext("a").find("span")
                tab_rice = table_price.text
                table_href = tablet_name.findNext("a")
                tab_href = table_href.get("href")
                name_title_href_g8[tab_name.lower()] = tab_rice, tab_href
                print(name_title_href_g8)
            except AttributeError:
                print("нет цены")
        count += 1

with open("name_title_href_g8.json", "w", encoding="utf-8") as file:
    json.dump(name_title_href_g8, file, indent=3, ensure_ascii=False)

with open("name_title_href_g8.json", "r", encoding="utf-8") as file:
    data2 = json.load(file)
    kes = input("Введите название: ")
    for k, v in data2.items():
        key = k.find(kes.lower())
        if key == 0:
            info = f"{k.upper()} \n {v} \n\n"
            s = info.replace("[", "").replace("]", "").replace("x", "").replace("a", "").replace("\\0", "").replace("'", "").replace(", ", "  <<<<<Ссылка:  ")
            print(s)



