# 외부라이브러리로서 설치 필요

import requests

res = requests.get('https://www.naver.com')

print(res)
print(res.text)