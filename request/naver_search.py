import requests

search_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8"

param = {"query": "영화"}

try:
    contents = requests.get(search_url, params=param)
    print(contents.text[150000:200000])
except Exception as e:
    print("에러발생", e)
