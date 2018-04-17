# coding: utf-8
import urllib.request
from bs4 import BeautifulSoup


import sys
from tqdm import tqdm
import json


URL = "https://www.akindo-sushiro.co.jp/menu/"

html = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html, "html.parser")

menu_list = {}
for i in range(1, 7+1):
    a = soup.select_one("#anchor-sec0{}".format(i))

    title = a.select_one("h3.sec-ttl > a.acc-trigger").text
    title = title.replace("\n", "")

    menu_list[title] = []

    b = a.select("ul.item-list > li")
    for menu in b:

        menu_info = {}
        for item in menu.select("span.txt-wrap > span"):
            if item.string is None:
                continue
            menu_info[ item["class"][0] ] = item.string

        menu_list[title].append(menu_info)

json_text = json.dumps(menu_list, ensure_ascii=False)
json_dict = json.loads(json_text)
f = open("menu.json", "w")
json.dump(json_dict, f, ensure_ascii=False)
