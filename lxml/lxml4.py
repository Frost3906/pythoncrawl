import requests
from lxml import etree


# lxml 구조
# lxml.html
# lxml.etree

def main():
    # 행정안전부 rss 기본 주소
    url = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001"

    res = requests.get(url)

    parseData(res)

def parseData(res):

    # lxml에서 parsing을 할 수 있는 구조로 변경
    root = etree.fromstring(res.content)
    # print(type(root)) # <class 'lxml.html.HtmlElement'>

    channel = root.xpath("//channel")
    print(channel[0].tag)

    print("\n--link 태그--")
    link1 = root.xpath("//link/text()")
    print(link1)

    print("\n--title 태그--")
    title = root.xpath("//title/text()")
    print(title)

    print("\n")
    items = root.xpath("//channel/item")
    for item in items:
        for data in item:
            print(data.tag, ":", data.text)
        print("\n")
    
if __name__ =="__main__":
    main()

