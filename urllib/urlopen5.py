# 네이버 / 다음 뉴스 가져오기
# 화면출력 / 파일 저장
import urllib.request as request
from urllib.error import HTTPError

request_url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=016&aid=0001715415"

try:
    contents = request.urlopen(request_url).read().decode("euc-kr")

    print(contents)

    with open("d:/download/navernews.html", "w") as f:
        f.write(contents)
except HTTPError as e:
    print(e)
else:
    print("성공")
