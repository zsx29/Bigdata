# 다음 뉴스 랭킹 1 ~ 10 출력하기

import requests as req
from bs4 import BeautifulSoup as bs

response = req.get("https://news.daum.net/ranking/popular", headers={"user-Agent": "Mozilla/5.0"})

dom = bs(response.text, "html.parser")

titles = dom.select("#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong > a")

for i in range(10):
    print([i+1], "번뉴스 : ", titles[i].text.strip())
