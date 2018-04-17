# coding: utf-8
import urllib.request
from bs4 import BeautifulSoup


import sys
from tqdm import tqdm
import json


URL = "http://www.hamazushi.com/hamazushi/menu/"
menu_type = [
    "nigiri",
    "gunkan",
    "zeitaku",
    "side",
    "dessert",
    "takeout",
]

html = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html, "html.parser")

menu_list = {}

for type in menu_type:
    a = soup.select_one("#{}".format(type))

    title = a.select_one("div.titArea > h2 > img")['alt']

    menu_list[title] = []

    b = a.select_one("ul.menuList")
    for menu in b.select("li"):
        menu_list[title].append(menu.text)

json_text = json.dumps(menu_list, ensure_ascii=False)
json_dict = json.loads(json_text)
f = open("menu.json", "w")
json.dump(json_dict, f, ensure_ascii=False)




###################################
###################################
###################################

