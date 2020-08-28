# 다음 쇼핑 베스트100 에서 임의의 카테고리 2개를 정해서
# 정보를 가져온 뒤 상품명 출력하기
# shopping100.py 참고

# 컴퓨터 : https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=B02&durationDays=30&count=100&_=1598407762569
# 식품 : https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=D01&durationDays=30&count=100&_=1598407897813
import requests

url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?durationDays=30&count=100"

params = [
    {"vCateId": "B02", "_": "1598407762569"},  # 컴퓨터
    {"vCateId": "D01", "_": "1598407897813"},  # 식품
]

with requests.Session() as s:
    for param in params:
        res = s.get(url, params=param)

        for i, item in enumerate(res.json(), 1):
            if i < 101:
                print(i, item["product_name"])
        print("*" * 30)

