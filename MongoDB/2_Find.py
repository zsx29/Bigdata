"""
날짜 : 2021-06-14
이름 : 박재형
내용 : 파이썬 MongoDB Find 실습하기
"""

from pymongo import MongoClient as mongo
from datetime import datetime

# 1단계 - mongoDB 접속
conn = mongo('mongodb://admin:1234@192.168.100.102:27017')

# 2단계 - DB 선택
db = conn.get_datebase("test")

# 3단계 - Collection 선택
collection = db.get_collection("MEMBER")

# 4단계 - Query 실행
rs = collection.find()

for row in rs:
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print('%s, %s' % (row['uid'], row['name']))

# 5단계 - 종료
conn.close()
print("Find success...")