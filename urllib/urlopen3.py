# urlopen() : 요청하는 url의 정보를 메모리에 올려서 분석할 때 사용
import urllib.request as req
from urllib.error import HTTPError
from urllib.parse import urlparse

encar_url = "http://www.encar.com/"

try:
    response = req.urlopen(encar_url)

    # 수신된 정보 확인
    print(
        "type : {}".format(type(response))
    )  # type : <class 'http.client.HTTPResponse'>
    print(
        "geturl : {}".format(response.geturl())
    )  # geturl : http://www.encar.com/index.do
    print("status : {}".format(response.status))  # status : 200
    print("header : {}".format(response.getheaders()))
    print("getcode : {}".format(response.getcode()))  # getcode : 200
    # url 파싱 전체정보
    print("parse : {}".format(urlparse("http://www.encar.com?test=test")))
    # url 정보 중 파라메터에 대한 부분만
    print("parse : {}".format(urlparse("http://www.encar.com?test=test").query))

    contents = response.read().decode("euc-kr") # parse : test=test

except HTTPError as e:
    print(e)
else:
    print(contents[:4000])

