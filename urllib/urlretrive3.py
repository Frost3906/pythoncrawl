#urlretrive : 요청하는 url의 정보를 로컬 파일로 저장
#             csv파일, api 데이터 등 많은 양의 데이터를 한꺼번에 저장할 때 사용

import urllib.request as req

# 요청 url
img_url="https://static.smalljoys.me/2018/01/this-is-just-the-hair-blowing-in-the-wind-samoyeds_"
html_url="http://google.com"
# 로컬 파일
save_html="d:/google3.html"
save_img="d:/사모예드.png"

try:
    file1, header1=req.urlretrieve(img_url, save_img)
    file2, header2=req.urlretrieve(html_url, save_html)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("성공")