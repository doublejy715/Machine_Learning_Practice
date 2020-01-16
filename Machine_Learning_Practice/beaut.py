# CSS 뽑아내기(23P) html,xml(웹 페이지)를 분석, 파싱하여주는 라이브러리 -> beautifulSoup
# 왜 소스를 뽑아내야 할까? : 모은 웹페이지는 html형식으로 되어있기 떄문에 beautifulSoup을 통해서 텍스트나 그림 형태로 뽑아와야한다.
# 1case : 밑의  html에서 li,h1 tag를 뽑는 연습을 해 보자

"""
# 태그/요소 선택자
    "ul"
    "div"
    "li"
# id 선택자 : #을 이용해 준다.
    "#meigen"
# class 선택자 : .을 이용하여 준다.
    만약 class="items art it book" 인 경우에는 띄어쓰기로 구분을 하여준다.
    ".art"로 선택이 가능하다.
    여러 개 선택일 경우에는 "book.art.it.items"로 연이어 설정한다.
# 보통 tag.class형태가 많이 이용된다. : ul class ~~~
    ".items"
# 위의 태그, id, class 선택자들은 서로 조합하여 어떤 형태로든 이용이 가능하다.

# 구조 선택자
    1. 후손 선택자 : 어떠한 태그 아래에 있는 모든 녀석들을 이야기한다.
        예시로 html의 후손 선택자를 의미하게 된다면
        <body> ~~ </body> 까지의 영역이 후손 선택자가 된다.
        ex) "#meigen li" : meigen이라는 태그 아래에 있는 후손 중에 li를 선택하라
    2. 자식 선택자 : 어떠한 태그 바로 밑에 있는 자식을 의미한다.
        html의  자식 선택자 : <body> 하나만 가리키게 된다.
        ex) "ul.items > li" :
위의 5가지를 이용해서 선택을 해 보도록 한다.
"""

from bs4 import BeautifulSoup

html = """
<html><body>
<div id="meigen">
    <h1>위키북스 도서</h1>
    <ul class="items">
        <li>유니티 게임 이펙트 입문</li>
        <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
        <li>모던 웹사이트 디자인의 정석</li>
    </ul>
</div>
</body></html>
"""

# 첫 번째 포인트 "import 하기"

soup = BeautifulSoup(html, 'html.parser') # 첫번째 매개변수로 html의 형식으로 주어진다. 두번쨰 매개변수는 어떠한 parser을 이용할지 묻는다
header = soup.select_one("body > div > h1")  # 'CSS 선택자'를 정확하게 알고 있어야 8,9번 줄을 올바르게 사용이 가능하다.
# 결과로 header에 요소가 추출이 된다.
list_items = soup.select("ul.items > li") # ul.items 아래에 있는 모든 li tag 를 선택해달라 라는 의미이다.
# 결과로 list_items에 요소의 배열 형태로 출력이 된다. -> 단순히 하나를 선택하느냐 여러개 선택하느냐에 따라서 select_one or select가 된다.
#
print(header.string) # 글자 형태로 추출하고자 할 때(표현)
# header.attrs["title"] # 내부의 요소를 추출하고자 할 때, dict형태이기 때문에 []이 필요하다
# 예제 내에서는 속성을 가지고 있는 Tag가 ul밖에 없으므로
print(soup.select_one("ul").attrs) # ul태그의 속성을 가진 것이 출력된다.
for li in list_items: # ul태그의 하위 태그인 li태그를 줄줄이 출력되게 된다.
    print(li.string)

# 35P 특히나 tag 선택자, 요소 선택자가 기본적

# 만약에 terminal에서 'no mudule 'bs4' ~~ ' 이러한 문구가 뜨면 해당 docker 컨테이너 파일안에서 pip install --user BeautifulSoup4를 적어 bs4를 설치해줘야 한다.

