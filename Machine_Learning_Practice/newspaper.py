# 신문기사 긁어오기

import urllib.request
from bs4 import BeautifulSoup
import time # 해당 웹사이트에 단위시간동안 많이 호출하게 된다면 ip를 차단당할 수 있으므로 해당 lib을 통해서 조절하여 준다.
url ="https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response,"html.parser")

# 뽑아오려는 기사들의 공통점을 찾아내야 한다. 기사들만 뽑아오기 위함이다.
# 우클릭 후 '검사'를 통해서 어떻게 구성되어 있는지, 어떤 태그로 되어 있는지 공통점을 찾아나간다.

results = soup.select("#main_content a") # 공통된 태그와 위치를 여기다가 적는다.
# id를 이용해서 데이터를 들고오기 위해서는 '#(id이름)'을 이용해서 들고온다.

# 위치를 특정하기 위해서 후손선택자나 자식선택자를 찾아본다.
for result in results:
    # 기사들을 들고 올 수 있게된다.
    print(result.attrs["href"]) # class 내부의 url을 가리키는 'herf'를 입려하게 되면, 모든 링크를 가지고 올 수있게된다.
    url_articl = result.attrs["href"]
    # url내부에 있는 링크를 가져오고 그 내부의 내용까지 들고오기
    response = urllib.request.urlopen(url_articl)
    soup_article = BeautifulSoup(response,"html.parser")
    content = soup_article.select_one("articleBodyContents")
    print(content.contents) # string을 하게 되면 기사 제목만 들고오게 된다.
    # 1초 휴식
    time.sleep(1)
# 이렇게 신문 기사들의 제목을 가져올 수 있다. a 태그 내부의  url역시 들오올 수 있게 된댜.(링크를 들고 올 수 있게 된다.)
# #section_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2)