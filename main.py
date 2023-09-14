from tkinter import *
import tkinter.messagebox as mb
import customtkinter
import os.path
import requests
from bs4 import BeautifulSoup
import json


def save():

    headers = {
        'authority': 'ultra-ultra.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru,en;q=0.9,la;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'referer=https%3A%2F%2Fyandex.ru%2F; _ym_uid=1676272120453210067; _ym_d=1676272120; __utmz=193754345.1676272122.1.1.utmcsr=yandex.ru|utmccn=(referral)|utmcmd=referral|utmcct=/; _gid=GA1.2.2056440425.1676583669; shop_viewed=18347%2C22374%2C16852%2C22498%2C18087%2C22700%2C18286%2C20144%2C20949; _ym_isad=1; landing=%2F; PHPSESSID=45bcdb52e8fd269f69f2beafe7f04485; _gat_gtag_UA_75622416_1=1; _gat_UA-219886478-1=1; _ga_HSQMSDREW7=GS1.1.1676805686.14.0.1676805686.0.0.0; _ga=GA1.1.979682655.1676272120; _ym_visorc=w; __utma=193754345.979682655.1676272120.1676742558.1676805687.13; __utmc=193754345; __utmt=1; __utmb=193754345.1.10.1676805687',
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


    #Считываем страницу сайтас
    response = requests.get('https://ultra-ultra.ru/',  headers=headers)
    src = response.text

    response2 = requests.get('https://g8.ru/', cookies=cookies2, headers=headers2)
    src2 = response2.text

    # Запускаем обработку страницы
    # Первый сайт
    soup = BeautifulSoup(src, "lxml")
    all_products_href = soup.find("div", "sidebar-box").find(class_="base-menu").find_all("a")

    soup2 = BeautifulSoup(src2, "lxml")
    produt_all = soup2.find("ul", id="menu-main-horizontal-menu").find_all("a")

    #Сохраняем словарь категорий и сылок
    all_cotigories_href = {}

    all_coter = {}
    #цикл обработки страницы и вывода результоат
    for item in all_products_href:
        item_text = item.text
        item_href = "https://ultra-ultra.ru" + item.get("href")
        all_cotigories_href[item_text] = item_href
    # #Сохраняем результат цикла в файл json
    # #парамитр indent переносит на новую строку записи
    # #Убирает проблемы с кодировкой ensure_ascii=False
    for items in produt_all:
        title_name = items.text
        title_href = items.get("href")
        all_coter[title_name] = title_href

    with open("all_cotigories_href.json", "w", encoding="utf-8") as file:
        json.dump(all_cotigories_href, file, indent=4, ensure_ascii=False)

    with open("all_cat_g8.json", "w", encoding="utf8") as file:
        json.dump(all_coter, file, indent=4, ensure_ascii=False)

    with open("all_cat_g8.json", encoding="utf8") as File:
        value = json.load(File)
        text1 = "https://g8.ru"
    val_new = ""
    for k, v, in value.items():
        val = v.find(text1)
        if val == 0:
            pass
        else:
            val_new = text1 + v
            value[k] = val_new
    with open("all_cat_g8.json", "w", encoding="utf8") as file:
        json.dump(value, file, indent=4, ensure_ascii=False)

    #Считываем файл с катигориями
    with open("all_cotigories_href.json", encoding="utf-8") as file:
        all_categories = json.load(file)



    count = 0

    #Переходим по катигориям и собираем информацию

    Name_title_href = {}

    for category_name, category_href in all_categories.items():

    #заменяем не нужные символы
            rep = [",", " ", "-"]
            for item in rep:
                if item in category_name:
                    category_name = category_name.replace(item, "_")

            req = requests.get(url=category_href, headers=headers)
            src = req.text

            soup = BeautifulSoup(src, "lxml")

            #собираем данные со страницы

            for tablet_name in soup.find_all('div', class_='pl-item-info'):
                table_titlt = tablet_name.findNext("div", class_="pl-item-info-expandable").find("a")
                tablet_price = table_titlt.findNext("div", class_="price-wrapper").find("span")
                tPrice = tablet_price.text
                tablet_title_name = table_titlt.text
                tablet_href_name = "https://ultra-ultra.ru" + table_titlt.get("href")
                Name_title_href[tablet_title_name.lower()] = tPrice, tablet_href_name

            count += 1

            window.update()
            progres_bar.start()

    mb.showinfo("Информация", "Первый сайт готов")
    with open("all_cat_g8.json", encoding="utf8") as file:
        all_cat = json.load(file)

    count2= 0
    name_title_href_g8 = {}
    for cat_name, cat_href in all_cat.items():

            # заменяем не нужные символы
            rep = [",", " ", "-"]
            for item in rep:
                if item in cat_name:
                    cat_name = cat_name.replace(item, "_")

            req2 = requests.get(url=cat_href, headers=headers2)
            src2 = req2.text

            soup2 = BeautifulSoup(src2, "lxml")

            for tablet_name2 in soup2.find_all('div', class_='product-inner'):
                try:
                    table_nam = tablet_name2.findNext("a").find("h2")
                    tab_name = table_nam.text
                    table_price = tablet_name2.findNext("a").find("span")
                    tab_rice = table_price.text
                    table_href = tablet_name2.findNext("a")
                    tab_href = table_href.get("href")
                    name_title_href_g8[tab_name.lower()] = tab_rice, tab_href
                except AttributeError:
                    print("нет цены")
            count2 += 1
            window.update()

    with open("Name_title_href.json", "w", encoding="utf-8") as file:
        json.dump(Name_title_href, file, indent=3, ensure_ascii=False)
    with open("name_title_href_g8.json", "w", encoding="utf-8") as file:
        json.dump(name_title_href_g8, file, indent=3, ensure_ascii=False)
    mb.showinfo("Информация", "Файл с данными обнавлен")
    progres_bar.stop()
    progres_bar.set(value=0)

file_path ="Name_title_href.json"
file_path2 ="name_title_href_g8.json"
def clicked():
   text.delete(1.0, END)
   text_g8.delete(1.0, END)
   if os.path.exists(file_path) == True:
    if os.path.exists(file_path2) == True:
            with open("Name_title_href.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            with open("name_title_href_g8.json", "r", encoding="utf-8") as file:
                data2 = json.load(file)
            kes = txt.get()
            keys = txt.get()
            if keys == "":
                pass
            else:
                for k, v in data.items():
                    key = k.find(keys.lower())
                    if key == 0:
                            info = f"{k.upper()} \n {v} \n\n"
                            s = info.replace("[", "").replace("]", "").replace("'", "").replace(", ", "  <<<<<Ссылка:  ")
                            text.insert(INSERT, s)
                            txt.delete(0, "end")
                for k, v in data2.items():
                    key = k.find(kes.lower())
                    if key == 0:
                            info = f"{k.upper()} \n {v} \n\n"
                            s = info.replace("[", "").replace("]", "").replace("x", "").replace("a", "").replace("\\0",
                                                                                                                 "").replace(
                                "'", "").replace(", ", "  <<<<<Ссылка:  ")
                            text_g8.insert(INSERT, s)
                            txt.delete(0, "end")

   else:
     mb.showinfo("Информация", "проведите сканирование")

def cleaner():
    text.delete(1.0, END)
    text_g8.delete(1.0, END)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.title("Приложение ParsingSait")
window.resizable(width=False, height=False)

f_top = Frame(window, pady=10)
f_center1 = Frame(window)
f_center = Frame(window)
f_bottom = Frame(window, background="#27222e")


btn = customtkinter.CTkButton(f_top,
                              text="Поиск",
                              width=100,
                              font=("Arial Bold", 17),
                              command=clicked)

btn_clener = customtkinter.CTkButton(f_bottom,
                                     text="Очистить",
                                     width=100,
                                     font=("Arial Bold", 17),
                                     command=cleaner)

txt = customtkinter.CTkEntry(f_top,
                             placeholder_text="Введите название товара",
                             border_width=1,
                             corner_radius=8,
                             width=700,
                             font=("Arial Bold", 15))
Label(f_center1, text='Магазин: Ультра',font=("Arial Bold", 17)).pack(side=LEFT, padx=170, pady=5)
text = customtkinter.CTkTextbox(f_center,
                                        width=400,
                                        height=400,
                                        corner_radius=10
                                        )
Label(f_center1, text='Магазин: G8',font=("Arial Bold", 17)).pack(side=LEFT, padx=170, pady=5)
text_g8 = customtkinter.CTkTextbox(f_center,
                                        width=400,
                                        height=400,
                                        corner_radius=10
                                        )




progres_bar = customtkinter.CTkProgressBar(f_bottom,
                                           orientation="horizontal",
                                           mode="determinate",

                                           )
progres_bar.set(value=0)

btn1 = customtkinter.CTkButton(f_bottom,
                               text="Сканирование",
                               width=150,
                               height=32,
                               font=("Arial Bold", 17),
                               command=save)


f_top.pack()
f_center1.pack()
f_center.pack()
f_bottom.pack()
txt.pack(side=LEFT, padx=5, pady=5)
btn.pack(side=LEFT, padx=1, pady=5)



text.pack(side=LEFT, padx=5, pady=10)
text_g8.pack(side=LEFT, padx=5, pady=10)
btn_clener.pack(side=TOP,  padx=5, pady=5)

progres_bar.pack(side=LEFT, padx=115, pady=20)
btn1.pack(side=LEFT, padx=115, pady=20)

window.mainloop()




