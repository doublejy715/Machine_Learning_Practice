import urllib.request
from bs4 import BeautifulSoup

url = "https://land.naver.com/"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response,"html.parser")

results = soup.select("div.usefultip_content_inner.type_sale>ul>li>a>div>span.text")
# #anchor_22 > section > div > div:nth-child(2) > div > a.area_text > div > div > strong
for result in results:
    print(result.string)

# usefultip > div.usefultip_content.is-rent > div.usefultip_content_inner.type_sale > ul > li:nth-child(1) > a > div > span.text
# usefultip > div.usefultip_content.is-rent > div.usefultip_content_inner.type_rent > ul > li:nth-child(1) > a > div > span.text