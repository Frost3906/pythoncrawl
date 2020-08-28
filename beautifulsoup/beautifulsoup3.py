from bs4 import BeautifulSoup
import requests

with open("./beautifulsoup/story.html") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())

# 타이틀 태그 출력
print("title >> {}".format(soup.title))
# 타이틀 태그 내용 출력
print("title >> {}".format(soup.title.string))
# h1 태그 내용 출력
print("h1 >> {}".format(soup.body.h1))

print("p >> {}".format(soup.body.p))
p1 = soup.p

print("p >> {}".format(p1))
print("p class value >> {}".format(p1["class"]))

###find

print("----- find() 함수-----")
print("h1 : {}".format(soup.find("h1")))
print("p : {}".format(soup.find("p")))

## 두번째 p 태그 가져오기
print("\n-- 두번쨰 p태그 --")
p2 = p1.next_sibling.next_sibling
print(p2)
print()
p2 = p1.find_next_sibling()
print(p2.prettify())

print("\n --- 세번째 태그 --- ")
p3 = p2.next_sibling.next_sibling
print(p3)
print()

p3 = p2.find_next_sibling()
print(p3.prettify())

print()
for v in p2.next_element:
    print(v, end="")

print()

# p3가 사용할 수 있는 함수 /속성 확인
print(dir(p3))