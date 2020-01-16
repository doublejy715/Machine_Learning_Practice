import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt # 원래는 Twitter 였는데 koNLpy v0.4.5 이후로는 Okt로 바뀌엇단다. twitter해도 알아서 바꿔줌

# 원하는 파일을 불러오는 과정
file = codecs.open("2BEXXX01.txt","r",encoding="utf-16")
soup = BeautifulSoup(file, "html.parser")
body = soup.select_one("text > body")
text = body.getText()

# ** 명사 빈도를 추출하기 **
twitter = Okt() # 트위터 인스턴스 생성
word_dic = {} # 언어의 빈출도를 조사할 dict하나 생성 (아마 key : 단어, value : 품사)
lines = text.split("\r\n") # text분할하기
for line in lines:
    malist = twitter.pos(line)
    for taeso, pumsa in malist : # malist 내부에 존재하는 teaso와 pumsa를 동시에 하나씩 돌린다.
        if pumsa == "Noun": # 품사가 명사인 것 중에서
            if not (taeso in word_dic) : # 품사가 Noun인데 태소가 word_dic의 key에 존재하지 않는다면(단어가 기록되어있지 않았다면)
                word_dic[taeso] = 0 # 하나 key를 새롭게 추가한다.
            word_dic[taeso] += 1 # 있으면 하나 카운터한다.

# 책에서 말하는 최대 빈도 명사를 50개 가량 추출하는 코드
keys = sorted(word_dic.items(),key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1})".format(word,count),end="")
print()

# 이렇게 많은 빈도수를 찾아내어 책, 기사 와 같은 글의 종류 또한 파악할 수 있다.