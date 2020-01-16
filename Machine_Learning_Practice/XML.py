'''
** 얻어오고자 하는 데이터 형식이 XML형식으로 주어질 때 정보를 추출하는 방법**

[1]여는 태그와 닫는 태그가 존재한다.
1. <태그></태그> # 요소(element)
2. <태그 /> : 여는 태그와 닫는 태그가 동시에 존재하는 경

[2]콘텐츠 : 태그와 태그 사이에 입력을 할 수 있는것이다.
1.<태그>{{콘텐츠}}</태그>  : {{콘탠츠}} 내부의 글자들을 '텍스트'라 부르게 된다.
2. 태그 내부에 태그가 존재하는 경우는 '콘덴츠' 라고 부른다.
<태그>
    <태그></태그> # 콘덴츠
    <태그></태그> # 콘덴츠
    <태그></태그>
</태그>

[3] 속성 : 태그 내부에 적는 것이다.
<태그 속성="값" 속성="값" 속성="값" 속성="값">{{콘덴츠}}</태그>
<태그 속성="값" 속성="값" 속성="값" 속성="값" />
문자열이던 숫자이던 반드시 "" 안에 존재하여야 하며, 숫자로 할려변 형변환을 겨쳐야 한다.

[4] root tag : 가장 상위에 존재하게 되는 태그이다. 반드시 하나이다.

'''

from bs4 import BeautifulSoup
import  urllib.request

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
request = urllib.request.urlopen(url)
xml = request.read()

soup = BeautifulSoup(xml,"html.parser")
seoul = soup.find_all("location")[0] # 서울의 날씨 정보를 가져오기 위해서 location tag의 0번째 정보를 모두 가져온다.
datas = seoul.find_all("data") # data tag의 모든 정보를 들고온다.
for item in datas: # 많은 datas의 정보들 중에서 날씨 정보 변수인 wf를 들고온다.
    print("날씨"+item.find("wf").text) # 이것으로 모든 것의 날씨 정보를 불러올 수 있다.
    print("최저온도" +item.find("tmn").text)
    print("최고온도" +item.find("tmx").text)

# 결국에는 기존의 html의 방식과 비슷하다고 볼 수 있다.
 