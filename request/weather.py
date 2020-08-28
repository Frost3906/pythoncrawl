import requests

# request 라이브러리를 이용
weather_url = (
    "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
)

# res = requests.get(weather_url)
# print(res.text)


# 세션을 이용하는 경우
with requests.Session() as s:
    res = s.get(weather_url)
    print(res.text)
