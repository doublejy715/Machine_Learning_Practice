import urllib.request
from bs4 import BeautifulSoup # 데이터를 분석하여주는 것

url = "https://finance.naver.com/marketindex/"
response = urllib.request.urlopen(url) # 데이터를 파이썬에서 읽어들이는것
# 먼저 원하는 데이터를 읽어들이기 위해서는 원하는 데이터의 위치를 파악하는 것이 가장 중요하다.
# 펼쳐보면 태그 이름은 span이고 class이름은 value이다.
soup = BeautifulSoup(response, "html.parser")

# soup.select_one()
# results = soup.select("span.value") # 이 결과로써 span태그 내부의 value 값들이 모조리 나오게 된다. 대상을 구체화할 필요가 있다.
results = soup.select("span.value")

# 위치를 이용해서 대상의 위치를 구체화 한다.
print("원달러 : " + results[0].string) # 원달러 환율
print("원엔 : " + results[1].string) # 원엔 환율
print("원유로 : " + results[2].string) # 원유로 환
for result in results:
    print(result.string)