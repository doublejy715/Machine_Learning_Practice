# 단어들을 평면위에 올려 수치화 한다. -> 벡터화 한다.
'''
# 모델 생성하기
data = word2vec.LineSentence("") # 문장을 이것을 통해서 분석할 수 있다.
word2vec.Word2Vec(data, size=200, window=10, hs=1,min_count=2,sq=1) # 이 코드는 word2vec으로 import된 gensim.models 모듈에서 Word2Vec클리스를 매개변수 data를 주어 실행하라는 의미이다.
model.save("")
'''
from gensim.models import word2vec
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

# 이 전에 .wakati 파일을 생성 해야한다.(형태소가 띄어쓰기로 구분이 되어있는 파일이다.)
'''
txt : <p> 문장 문장 문장... </p> -> wakati : 형태소 형태소 형태소 .... 형식으로 바꾸어 준다.
'''
    # 먼저 원하는 파일을 들고온다.
fp = codecs.open("2BEXXX01.txt","r",encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("text > body")
text = body.getText()

# twitter 분석기를 이용해서 형태소 단위로 분리한다.
twitter = Twitter()
lines = text.split("\r\n")
results=[]
for line in lines:
    r = []
    malist = twitter.pos(line, norm=True, stem=True)
    for word, pumsa in malist:
        if not pumsa in ["Josa","Eomi","Punctuation"]:
            r.append(word) # 조사, 어미, 마침표 따위를 제외한 모든 단어들을 r list에 저장하게 된다.
    results.append((" ".join(r)).strip()) # r의 list를 병합한다.(join) 병합할 떄 띄어쓰기를 통해서 병합 문자를 구분하여 준다. # strip은 문장 맨 끝의 \n(줄바꿈)기호를 삭제하여 준다.
output = (" ".join(results)).strip() # 한번 더 해줌으로써 한 줄이 아닌 모든 범위의 줄들을 병합하게 된다.
print(output)

# 이렇게 본문을 띄어쓰기를 구분으로 하여 형태소 단위로 구분하게 해 주는 과정을 마치게 되었다.

# wakati 파일을 형성해 주자
with open("toji.wakati", "w", encoding="utf-8",) as fp:
    fp.write(output)

# ** 중요한 부분이다.
# wakati를 완성하고 Word2Vec을 통해서 model 파일을 하나 형성해 낸다.
data = word2vec.LineSentence("toji.wakati")
model = word2vec.Word2Vec(data, size=200, window =10, hs=1, min_count=2,sg=1)
model.save("toji.model")


# model을 활용하는 방법
# 비슷한 벡터(요소)를 가진 것들을 출력이 가능하다 -> 관련검색어로 활용이 가능하다는 점, 챗봇, 인공지능, 등등
# 이외에도 많을듯