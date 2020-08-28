# 외부라이브러리로서 설치 필요

import requests

# 세션을 이용한 접속
# get 방식으로 요청

# 세션 가져오기
# s = requests.Session()
# # 세션 안에서 요청하기
# res = s.get('https://www.naver.com')


# print(res) # <Response [200]>
# # print(res.text) # request로 가져온 내용 출력 

# print("status code : {}".format(res.status_code))
# print("OK ? : {}".format(res.ok))

# # 세션 종료

# s.close()

with requests.Session() as s:
    res = s.get("http://www.naver.com")
    print(res.text)