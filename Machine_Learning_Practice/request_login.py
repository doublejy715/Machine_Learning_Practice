import requests
from bs4 import BeautifulSoup
'''
매개변수를 모두 url을 필요로 한다. url : 정보를 가져오고자하는 site
session.get(url)
session.post(url)
session.put(url)
session.delete(url)

이때까지 학습한 것은 get형식이다.
'''
'''
Get의 활용
requests 라이브러리를 이용하여 인터넷에 매개변수 날리기
url = "http://google.com"
data = {
    "a" : "10",
    "b" : "20"
}

session = requests.session()
response = session.get(url,data = data) 이 작업을 통해서 매개변수를 날려준다.
'''
'''
이번 시간에는 post에 대한 함수의 이용을 알아볼 시간이다.
로그인이 필요할 경우(로그인의 자동화)

아이디와 비밀번호가 어디에서 해당 서버로 넘어가는지 확인하라
아이디와 비밀번호가 들어간 곳을 찾기
General 의 항목들을 통해서 어떤 URL에서 어떠한 방법으로(method) 보냈는지 알아본다.
이 method를 통해서 get인지 post인지 등을 알 수 있다.

Form Data에서 어떠한 변수들이 넘어갔는지를 알아내야 올바르게 로그인할 수 있게 된다.

이러한 부분을 requests 모듈로 python에서 구현하게 되면 python에서 로그인을 할 수 있게 된다.


'''

# General > Request URL을 참조한다.
url = "https://www.hanbit.co.kr/member/login_proc.php"

# 로그인
# From Data 의 내부항목을 참조한다.
data = {
    "retun_url":"http://www.hanbit.co.kr/index.html",
    "m_id":"doublejy715",
    "m_passwd":"DE!nf13rn0"
}


session = requests.session()

# 로그인을 위해서 Data를 보낸다.
response = session.post(url, data=data) # 이 부분을 조심해야 한다. 해당 페이지가 어떠한 Request Method를 가지고 있는가에 따라 맞춰주면 된다.
response.raise_for_status()

# 로그인 한 이후에 개인 정보의 코인 정보를 들고와 보자
url = "http://www.hanbit.co.kr/myhanbit/myhanbit.html" # 해당 코인의 정보가 들어있는 주소이다.
response = session.get(url)
response.raise_for_status() # th. 이 명령어를 통해서 메모리 상에서 읽어오느 건가?
# 특정 단어를 건져오기 위해서 beautifulsoup를 이용한다.
soup = BeautifulSoup(response.text,"html.parser")
text = soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span").get_text() # get_text()로 들고온다.
print("이코인 : " ,text)

 # 이러한 방식으로 인터넷에서 정보를 txt 형식으로 끌어왓다.
