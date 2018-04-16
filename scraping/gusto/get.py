# coding: utf-8
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# アクセスするURL
url = "https://www.skylark.co.jp/gusto/menu/index.html"

### load & parse
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# ブラウザのオプションを格納する変数
options = Options()

# Headlessモードを有効にする(コメントアウトするとブラウザが実際に立ち上がる)
options.set_headless(True)

# ブラウザを起動する
driver = webdriver.Chrome(executable_path="../../chromedriver", chrome_options=options)

# ブラウザでアクセスする
driver.get(url)

# HTMLを文字コードをUTF-8に変換してから取得する
html = driver.page_source.encode('utf-8')

# BeautifulSoupで扱えるようにパース
soup = BeautifulSoup(html, "html.parser")

#open("index.html", "w").write(str(soup))

"""
for i in range(10, 60+1, 10):
    menu_book = soup.select_one("#menu_book_{}".format(i))
    print(menu_book.string)
"""

#a = soup.select_one("p._date")

"""
for menu_book_item in soup.select("ul.mod-grid04"):
    ...
"""

a = soup.select_one("ul.mod-grid04")
b = a.select("p._cap")
#print(a)
print(b)



