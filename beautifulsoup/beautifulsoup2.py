from bs4 import BeautifulSoup
import requests


# 요청 가져오기
res = requests.get("https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=421&aid=0004839426")

# BeutifulSoup 객체 생성 - parser 지정
soup = BeautifulSoup(res.content,"html.parser")

# soup 객체를 이용해 파싱하기
# find() : 검색되는 제일 첫번째 리턴
title = soup.find("h3", id="articleTitle")
print(title)
print(title.string)
print(title.get_text())