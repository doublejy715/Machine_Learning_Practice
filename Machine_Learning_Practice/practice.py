import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://dict.naver.com/"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response,"html.parser")

results1 = soup.select("div.dic_wrap.hot>ul>li>a") # class의 이름에 띄어쓰기가 추가되면 .을 이용한다.
results2 = soup.select("div.usefultip_content_inner.type_rent.is-showbottom > ul > li > a")
for result1,result2 in results1,results2:
    print(result1.string) # 그러나 여기에서는 이름 옆에 부호가 들어가면 인식하지 못하고 none처리된다.
    print(result2.)
# #container > div.view_all.on > div.alldic_wrap.alldic_view > div.view_dic > div.dic_wrap.asia > ul > li:nth-child(1) > a
# #usefultip > div.usefultip_content.is-rent > div.usefultip_content_inner.type_rent.is-showbottom > ul > li:nth-child(3) > a