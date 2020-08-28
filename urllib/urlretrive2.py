#urlretrive : 요청하는 url의 정보를 로컬 파일로 저장
#             csv파일, api 데이터 등 많은 양의 데이터를 한꺼번에 저장할 때 사용

import urllib.request as req

# 요청 url
img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR13eikJ52Gdi0ZZCtJsLxWWWHFZxVCiFxGkw&usqp=CAU"
html_url="http://google.com"
# 로컬 파일
save_html="d:/google2.html"
save_img="d:/save1.png"

try:
    file1, header1=req.urlretrieve(img_url, save_img)
    file2, header2=req.urlretrieve(html_url, save_html)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("성공")