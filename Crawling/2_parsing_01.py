"""
    날짜 : 2021-06-07
    이름 : 박재형
    내용 : 파이썬 HTML 페이지 파싱 실습하기

    * 파싱(parsing)
        - 문서 해독을 의미한다.
        - 마크업 문서(HTML, XML)에서 특정 태그의 데이터를 추출하는 처리과정
"""

import requests as req
from bs4 import BeautifulSoup as bs



# (1) 페이지 요청
response = req.get("https://news.naver.com/",
                   headers={"user-Agent": "Mozilla/5.0"})

# print(response.text)

# (2) 페이지 파싱 데이터출력
dom = bs(response.text, "html.parser")  # dom =  document object model

titles = dom.select("#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a")

for tit in titles:
    print(tit.text.strip())  # strip() : 공백제거(trim)



# 다음 뉴스 랭킹 1 ~ 10 출력하기

response = req.get("https://news.daum.net/ranking/popular", headers={"user-Agent": "Mozilla/5.0"})

dom = bs(response.text, "html.parser")
titles = dom.select("#mArticle > div.rank_news > ul.list_news2 > li")

for tit in range(10):
    print(tit.text.strip())




















