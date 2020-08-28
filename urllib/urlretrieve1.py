# urlretrieve : 요청하는 url의 정보를 로컬 파일로 저장
#               csv 파일, api 데이터 등 많은 양의 데이터를 한꺼번에 저장할 때 사용
import urllib.request as req

# 요청 url
url = "http://google.com"
# 로컬 파일
save = "d:/google.html"

try:
    file1, header1 = req.urlretrieve(url, save)
except Exception as e:
    print(e)
else:
    print(header1)
    print("성공")
