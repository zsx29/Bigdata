import os

import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

# 페이지 요청
responce = req.get("https://issue.zum.com/")

# 페이지 파싱 데이터출력
dom = bs(responce.text, "html.parser")
divs = dom.select("#issueKeywordList > li > div.cont")

# 디렉터리 생성
dir = "./keyword/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
    os.makedirs(dir)

# 데이터 파일 생성
fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir + '/' + fname, mode='w', encoding='utf-8')

# 데이터 출력
file.write("순위, 단어\n")
for div in divs:
    rank = div.find(class_="num").text
    word = div.find(class_="word").text
    file.write("%s, %s\n" % (rank, word))

file.close()
print("데이터 수집 완료...")