# urlretrieve : 요청하는 url의 정보를 로컬 파일로 저장
#               csv 파일, api 데이터 등 많은 양의 데이터를 한꺼번에 저장할 때 사용
import urllib.request as req

# 요청 url
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fkinimage.naver.net%2F20120411_53%2F1334141109594tSwaJ_JPEG%2F%25BB%25F5%25B3%25A2%25B0%25AD%25BE%25C6%25C1%25F66.jpg&type=sc960_832"
html_url = "http://google.com"

# 로컬 파일
save_html = "d:/google2.html"
save_img = "d:/save1.png"

try:
    file1, header1 = req.urlretrieve(img_url, save_img)
    file2, header2 = req.urlretrieve(html_url, save_html)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("성공")
