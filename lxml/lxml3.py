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


    print(root)
    print(root.tag)
    
    children = root[0]
    print("children tag : {}".format(children.tag))

    for child in children:
        print(child.tag, ":", child.text)
        for ch in child:
            print(ch.tag, ":", ch.text)

if __name__ =="__main__":
    main()

