# urllib.parse 안 urlencode() 사용하기
# urlencode() - 파라메터 값 넘길 때 주로 사용
# https://naver.com?search=영화

from urllib.request import urlopen
from urllib.parse import urlencode

api = "https://api.ipify.org"

url = api + "?" + "format=json"
print("요청 URL = {}".format(url))

response = urlopen(url).read().decode("utf-8")
print(response)

