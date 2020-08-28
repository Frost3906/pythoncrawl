import urllib.request as request
from urllib.error import URLError, HTTPError

target_url = [
    "https://www.naver.com",
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20100615_12%2Fkkchblue_12765686609822pxfs_jpg%2F%25B0%25AD%25BE%25C6%25C1%25F6_kkchblue.jpg&type=sc960_832",
]

path_list = ["d:/download/naver.html", "d:/download/dog.jpg"]

# for url in target_url:

for i, url in enumerate(target_url):
    try:
        # 정보 가져오기
        response = request.urlopen(url)
        # 정보 읽기
        contents = response.read()
        # 상태 정보 확인
        print("-" * 50)
        print("header info - {} : {}".format(i, response.info()))
        print("Http status code - {}".format(response.getcode()))
        print("-" * 50)
        print()

        # 파일 저장(w : write, b : byte)
        with open(path_list[i], "wb") as f:
            f.write(contents)

    except HTTPError as e1:
        print(e1)
    except URLError as e2:
        print(e2)
    else:
        print("성공")

