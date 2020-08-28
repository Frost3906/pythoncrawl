import requests

# 행정안전부 rss 기본 주소
api = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

print(params)

with requests.Session() as s:

    for param in params:

        # 요청
        contents = s.get(api, params=param)
        print("*" * 50)
        print(contents.text)
        print()
