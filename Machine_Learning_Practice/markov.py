import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
import urllib.request
import os, re, json, random
# 마르코프 체인 딕셔너리 만들기 --- (※1)
def make_dic(words): # words는 형태소가 모두 분할이 되서 하나하나 떨어진 형태들이 저장되어있다.
    tmp = ["@"]
    dic = {}
    for word in words:
        '''
        ex) 개|도|닷새|가|되면|주인|을|안다|.
        1) tmp = ["@","개","도"] -> 길이가 3이다.
        2) 3이가 3초과하게 되면 set_word3로 넘어간다.
        3) tmp의 내용물이 각각 w1 = "@", w2="개", w3="도" 로 지정된다.
        4) 이후 dic안에 w1,w2,w3의 존재여부에 따라서 추가해 준다. (있으면 count, 없으면 생성)
         dic = {
             "@":{
                 "개":{
                     "도": 0 -> 1
                 }
             }
        }
        형식으로 된다.
        5) tmp = ["@","개","도","닷새"] -> tmp = ["개","도","닷새"] -> set_word3 ...
        '''
        tmp.append(word)
        # tmp안의 길이를 확인하는 조건문이다.
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == ".":
            tmp = ["@"]
            continue
    return dic

# 딕셔너리에 데이터 등록하기 --- (※2)
def set_word3(dic, s3):
    # 
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1
# 문장 만들기 --- (※3)
def make_sentence(dic):
    ret = []
    if not "@" in dic: return "no dic" # @를 검사함으로써 처리여부를 결정한다.
    top = dic["@"] # 골뱅이부터 꺼내고
    w1 = word_choice(top) #랜덤하게 꺼낸다. ex)개 (여기서는 @을 첫 key로 가진건 "@","개","도"이므로)
    w2 = word_choice(top[w1]) # ex)도 (여기서는 "@"와 "개"를 가진 것은 "도" 이므로)
    ret.append(w1) # ret = ["개","도"]
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2]) # 이번에는 "개","도"가 w1,w2가 되어서 w3를 랜덤적으로 부과한다. ex)"닷새"
        ret.append(w3)
        if w3 == ".": break # 마지막 w3가 '.'이 나올떄까지 반복한다.(문장이 하나 만들어진다.)
        w1, w2 = w2, w3 # 한칸씩 밀어준다.
    ret = "".join(ret)
    # 띄어쓰기
        # 웹에 보내기 위해 변수를 지정하여 준다.
    params = urllib.parse.urlencode({
        "_callback": "",
        "q": ret
    })
    # 만들어진 문장을 가지고 네이버 맞춤법 검사기를 사용합니다.
    data = urllib.request.urlopen("https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy?" + params)
    data = data.read().decode("utf-8")[1:-2]
    data = json.loads(data)
    data = data["message"]["result"]["html"]
    data = soup = BeautifulSoup(data, "html.parser").getText()
    # 리턴
    return data
def word_choice(sel): 
    keys = sel.keys() # "sel" 이라는 key를 가진 것들을 list로 모두 가져온다.
    return random.choice(list(keys)) # 그 중에서 랜덤 선택
# 문장 읽어 들이기 --- (※4)
toji_file = "toji.txt"
dict_file = "markov-toji.json"
    # 만약 dict_file이 존재하지 않을 경우에는 만들게 된다.
if not os.path.exists(dict_file):
    # 토지 텍스트 파일 읽어 들이기
    fp = codecs.open("./2BEXXX09.txt", "r", encoding="utf-16") # 여기서 경로는 자신의 컴퓨터에 맞게 재설정 해 줘야한다.(같은 폴터 내에 대상이 존재한다면 ./을 작성한다.)
    soup = BeautifulSoup(fp, "html.parser")
    body = soup.select_one("text > body") # 본문을 채취한다.
    text = body.getText()
    text = text.replace("…", "") # 현재 koNLPy가 …을 구두점으로 잡지 못하는 문제 임시 해결
    # 형태소 분석
    twitter = Twitter()
    malist = twitter.pos(text, norm=True)
    words = []
    for word in malist: # words 단어장에다가 형태소로 분리하여 추가한다.
        # 구두점 등은 대상에서 제외(단 마침표는 포함)
        if not word[1] in ["Punctuation"]:
            words.append(word[0])
        if word[0] == ".":
            words.append(word[0])
    # 딕셔너리 생성
    dic = make_dic(words)
    json.dump(dic, open(dict_file,"w", encoding="utf-8"))
else:
    # 만약 dict_file이 존재하게 되면 그대로 응용한다.
    dic = json.load(open(dict_file,"r"))
# 문장 만들기 --- (※6)
for i in range(3):
    s = make_sentence(dic)
    print(s)
    print("---")

# 이 마르코프 체인은 단순하게 단어들을 서로 연결하고, 랜덤적으로 생산하기 때문에 올바른 어법을 가진 문장을 만들기로는 부족하다. 또한 사투리가 들어간 경우에는 더욱히 그러하다.