"""
날짜 : 2021-06-14
이름 : 박재형
내용 : 파이썬 MongoDB Insert 실습하기
"""

#  패키지 선언
from pymongo import MongoClient as mongo
from datetime import datetime

# 1단계 - mongoDB 접속
conn = mongo("mongodb://admin:1234@192.168.100.102:27017")

# 2단계 - DB 선택
db = conn.get_database("test")

# 3단계 - Collection 선택
collection = db.get_collection("MEMBER")

# 4단계 - Query 실행
collection.insert_one(
    {"uid": "a101",
     "name": "김유신",
     "hp": "010-2222-4144"
    }
)

collection.insert_one(
    {"uid": "a101",
     "name": "김유신",
     "hp": "010-2222-4144",
     "pos": "대리",
     "dep": 102,
     "rdate": datetime.now()
    }
)

# 5단계 - 종료
conn.close()
print("Insert success...")




