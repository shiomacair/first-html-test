# pip install requests bs4

import requests
from bs4 import BeautifulSoup
import re

url = "https://www.yahoo.co.jp/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
for elem in elems:
    print("#" * 42)
    print(elem.contents[0].get_text())
    print(elem.attrs['href'])
