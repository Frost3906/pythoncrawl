# 위키피디아 서울지하철
# https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0

import requests


def info():
    url = "https://ko.wikipedia.org/wiki/서울_지하철"

    res = requests.get(url)
    # print(res.text)
    print(res.content)  # byte


if __name__ == "__main__":
    info()
