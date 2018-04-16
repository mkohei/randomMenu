# coding: utf-8
import urllib.request
from bs4 import BeautifulSoup


import sys
from tqdm import tqdm
import json


URL = "http://www.mcdonalds.co.jp/menu/"
menu_type = [
    "burger",
    "side",
    "drink",
    "dessert",
    "barista",
]


### バーガー
def get_burger(menu_list):
    MENU = "バーガー"
    index = 0
    menu_list[MENU] = {}

    url = URL + menu_type[index]
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    for i in range(1, 3+1):
        a = soup.select_one("#anchor{}".format(i))
        title = a.select_one("h2").string

        menu_list[MENU][title] = []

        print("{}.{}".format(MENU, title))

        if i==1:
            a = soup.select_one("div.c-container-div.ly-wrp-menuset.burger")
            b = a.select("div.c-item-product")
            a = soup.select_one("div.c-container-div.ly-wrp-menuset.bg")
            b.extend(a.select("div.c-item-product"))
        else:
            b = a.select("div.c-item-product")

        for menu in tqdm(b):
            menu_item = {}

            name = menu.select_one("h3").string
            menu_item["name"] = name

            empty = menu.select_one("div.empty")
            label = empty.select_one("p.label").string
            price = empty.select_one("p.price").string
            menu_item[label] = price

            for sm in menu.select("div.sm"):
                label = sm.select_one("p.label")
                if label is None:
                    continue
                label = label.string
                price = sm.select_one("p.price").string
                menu_item[label] = price

            menu_list[MENU][title].append(menu_item)

    return menu_list


### サイドメニュー
def get_side(menu_list):
    index = 1
    MENU = "サイドメニュー"
    menu_list[MENU] = {}

    url = URL + menu_type[index]
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    for  (_t, _m) in zip(["regular", "morning"], ["side", "morning"]):

        a = soup.select_one("div.c-container-div.ly-wrp-menuset.{}".format(_t))
        title = a.select_one("h2.c-item-title-whitespace").string

        menu_list[MENU][title] = []

        print("{}.{}".format(MENU, title))

        a = soup.select_one("div.c-container-div.ly-wrp-menuset.{}".format(_m))
        b = a.select("div.c-item-product")

        for menu in tqdm(b):
            menu_item = {}

            name = menu.select_one("h3").string
            menu_item["name"] = name

            for priceset in menu.select("div.ly-mod-menu-priceset"):
                label = priceset.select_one("p.label").string
                price = priceset.select_one("p.price").string
                menu_item[label] = price

            menu_list[MENU][title].append(menu_item)
    return menu_list


### ドリンク
def get_drink(menu_list):
    index = 2
    MENU = "ドリンク"
    menu_list[MENU] = {}

    url = URL + menu_type[index]
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    for  _t in ["burger", "morning"]:
        
        a = soup.select_one("div.c-container-div.ly-wrp-menuset.{}".format(_t))

        title = a.select_one("h2.c-item-title-whitespace").string

        menu_list[MENU][title] = []

        print("{}.{}".format(MENU, title))

        b = a.select("div.c-item-product")
        for menu in tqdm(b):
            menu_item = {}

            name = menu.select_one("h3").string
            menu_item["name"] = name

            for priceset in menu.select("div.ly-mod-menu-priceset"):
                label = priceset.select_one("p.label").string
                price = priceset.select_one("p.price").string
                menu_item[label] = price

            menu_list[MENU][title].append(menu_item)
    return menu_list


### スイーツ
def get_dessert(menu_list):
    index = 3
    MENU = "スイーツ"
    menu_list[MENU] = {}

    url = URL + menu_type[index]
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    title = "all"
    menu_list[MENU][title] = []

    print("{}.{}".format(MENU, title))

    b = soup.select("div.c-item-product")
    for menu in tqdm(b):
        menu_item = {}

        name = menu.select_one("h3").string
        menu_item["name"] = name

        for priceset in menu.select("div.ly-mod-menu-priceset"):
            label = priceset.select_one("p.label").string
            price = priceset.select_one("p.price").string
            menu_item[label] = price

        menu_list[MENU][title].append(menu_item)
    return menu_list


### マックカフェ バイ バリスタ
...


###################################
###################################
###################################
menu_list = {}

get_burger(menu_list)
get_side(menu_list)
get_drink(menu_list)
get_dessert(menu_list)

json_text = json.dumps(menu_list, ensure_ascii=False)
json_dict = json.loads(json_text)
f = open("menu.json", "w")
json.dump(json_dict, f, ensure_ascii=False)
