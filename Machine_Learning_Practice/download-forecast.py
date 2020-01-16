'''
*** 주소를 끌어오는 방법***
https://search.naver.com/search.naver?where=nexearch&query=%EC%86%A1%EC%B0%BD%EC%8B%9D&sm=top_lve.agallgrpmamsi0en0sp0&x_nxpr-front=all01-2&ie=utf8
홈페이지에서 데이터를 들고오는 방법
방식 : GET, POST, PUT, DELETE
데이터를 들고올 떄는 '대상, 경로, 데이터' 가 필요하다.
대상 : (호스트 이름) https://search.naver.com 이 된다.(페이지의 정보를 달라고 요청한다.)
추가적인 정보
- 경로(path) :  /search.naver
- 데이터 : ?where=nexearch&query=%EC%86%A1%EC%B0%BD%EC%8B%9D&sm=top_lve.agallgrpmamsi0en0sp0&x_nxpr-front=all01-2&ie=utf8
    - 데이터의 분석
    기본적으로 & 연산자를 통 해서 (t) = (value)들이 이어진 형태를 이어놓았다.
    ex)
    &where=nexearch
    &query=%EC%86%A1%EC%B0%BD%EC%8B%9D -> 한글로는 '송창식'의 의미를 가지고 있다. 송창식을 알파벳&기호를 통해 인코딩된 문자로 표현한다.
    &sm=top_lve.agallgrpmamsi0en0sp0
    &x_nxpr-front=all01-2&ie=utf8
    4개의 데이터가 전달이 된다. 이렇게 네이버는 4가지의 변수가 필요하다는 것을 알아낼 수 있다.
- 데이터 지정(? 이후의 것으로 get방식을 통해서 데이터를 불러온다.) : where=nexearch

'''

''' 예시1번
import urllib.request
import urllib.parse # 필요한 이유 : 송창식이라는 한글 표기를 영어나 기호로 바꾸어주기 위함

api = "https://search.naver.com/search.naver" # 호스트 이름의 설정
# 데이터의 지정
values = {
    "where":"nexearch",
    "query":"송창식",  # %EC%86%A1%EC%B0%BD%EC%8B%9D
    "sm":"top_lve.agallgrpmamsi0en0sp0",
    "x_nxpr-front":"all01-2&ie=utf8" # utf8 : 인코딩 방식
}
params = urllib.parse.urlencode(values)
url = api + "?" + params

data = urllib.request.urlopen(url).read()
print(data)

'''

# 예시 2번 https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%B4%88%EC%BD%9C%EB%A6%BF&oquery=%EC%B4%88%EC%BD%9C%EB%A6%BF&tqi=Umk2%2Bdp0YihssanLuksssssstoR-241125
import urllib.request
import urllib.parse # 필요한 이유 : 송창식이라는 한글 표기를 영어나 기호로 바꾸어주기 위함

api = "https://search.naver.com/search.naver" # 호스트 이름의 설정
# 데이터의 지정 및 매개변수를 인터넷 상으로 날리는 방법
values = {
    "sm":"tab_hty.top",
    "where":"nexearch",
    "query":"%EC%B4%88%EC%BD%9C%EB%A6%BF",
    "oquery":"%EC%B4%88%EC%BD%9C%EB%A6%BF",
    "tqi":"Umk2%2Bdp0YihssanLuksssssstoR-241125"
}
params = urllib.parse.urlencode(values)
url = api + "?" + params

data = urllib.request.urlopen(url).read()
print(data)