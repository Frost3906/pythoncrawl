import requests
from fake_useragent import UserAgent

user_agent = UserAgent()

s = requests.Session()

headers = {
    "user-agent": user_agent.chrome
}

res = s.get("http://httpbin.org/get", headers=headers)


# 상태 체크를 한 후 이상이 발생하면 다음 문장을 처리 안함
res.raise_for_status()
print(res.text)

s.close()