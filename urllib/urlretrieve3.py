# urlretrieve : 요청하는 url의 정보를 로컬 파일로 저장
#               csv 파일, api 데이터 등 많은 양의 데이터를 한꺼번에 저장할 때 사용
# 좋아하는 연예인 사진 저장하기
import urllib.request as req

# 요청 url
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5242%2F2014%2F03%2F08%2F1394221104_thumb_59_20140308045602.jpg&type=sc960_832"

# 로컬 파일
save_img = "d:/dog.jpg"

try:
    file1, header1 = req.urlretrieve(img_url, save_img)
except Exception as e:
    print(e)
else:
    print(header1)
    print("성공")
