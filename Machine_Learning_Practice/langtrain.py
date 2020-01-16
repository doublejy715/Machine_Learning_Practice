from sklearn import svm, metrics
import glob, os.path, re, json

files = glob.glob("./lang/train/*.txt") # *.txt를 하게 되면 해당 확장자 파일만 모두 끌어오게 된다.
# 원하는 파일들이  추출되었다.
train_data = []
train_label = []

# 파일들을 하나씩 끌어와서 알파벳이 얼마나 있는지 확인한다.
for file_name in files:
    # 레이블 구하기
    basename = os.path.basename(file_name) # basename : 파일의 경로를 제외한 나머지를 출력한다.(txt파일 이름만 나오게 된다.)(tl-20.txt)
    lang = basename.split("-")[0] # - 을 기준으로 하여 앞뒤로 나누게 된다.(tl,20)(참고로 해당 줄에서만 구분되어진다.)
    # 텍스트 추출하기
    file = open(file_name,"r",encoding = "utf-8")
    text = file.read() # text 변수에 file을 입력한다. file의 내부 전체 문자열을 해당 변수로 돌려준다.
    text = text.lower() # 내부의 모든 문자를 소문자로 변형시킨다.
    file.close()
    # 이때까지는 text변수 내에 문장 형태로 존재해 있다. 이제 알파벳 출현 빈도 구하기
    code_a = ord("a") # ord의 함수로 인해서 문자를 숫자형태로 바꿔주게된다.(아스키코드표를 따른다.)
    code_z = ord("z")
    count = [0 for n in range(0,26)] # 해당 알파벳이 얼마나 나왔는지 카운트해 주기 위해서 만들었다.
    for character in text:
        code_current = ord(character) # 해당 분리되어있는 알파벳을 숫자형태로 바꿔준다.
        if code_a <= code_current <= code_z:
            count[code_current-code_a] += 1
    
    # 횟수를 세게 되면 값이 1이상의 값이 나오기 때문에 바꿔준다. -> 정규화 실시
    total = sum(count) # 카운트에 나온 빈도수를 모두 더해준다.
    # 그렇다면 그냥 count/total 하면 안되나? 해보면 count는 list형태이고 total은 int이므로 형이 맞지 않는다.
    # 이를 해결해 주기 위해서 map을 이용하여 각각의 값에 int, int 형태로 형을 맞춰주어 다시 count에 저장한다.
    count = list(map(lambda n: n/total,count )) # n이라는 매개변수를 넣고 return은 n/total로 해 준다. 다시 list형성

    # 리스트에 넣기
    train_data.append(count) # 데이터 가공된 Input
    train_label.append(lang) # 데이터 가공된 정답

files = glob.glob("./lang/test/*.txt")
# 이제는 올바르게 학습했는지 테스트 해 본다.
test_data = []
test_label = []

# 파일들을 하나씩 끌어와서 알파벳이 얼마나 있는지 확인한다.
for file_name in files:
    # 레이블 구하기
    basename = os.path.basename(file_name) # basename : 파일의 경로를 제외한 나머지를 출력한다.(txt파일 이름만 나오게 된다.)(tl-20.txt)
    lang = basename.split("-")[0] # - 을 기준으로 하여 앞뒤로 나누게 된다.(tl,20)(참고로 해당 줄에서만 구분되어진다.)
    # 텍스트 추출하기
    file = open(file_name,"r",encoding = "utf-8")
    text = file.read() # text 변수에 file을 입력한다. file의 내부 전체 문자열을 해당 변수로 돌려준다.
    text = text.lower() # 내부의 모든 문자를 소문자로 변형시킨다.
    file.close()
    # 이때까지는 text변수 내에 문장 형태로 존재해 있다. 이제 알파벳 출현 빈도 구하기
    code_a = ord("a") # ord의 함수로 인해서 문자를 숫자형태로 바꿔주게된다.(아스키코드표를 따른다.)
    code_z = ord("z")
    count = [0 for n in range(0,26)] # 해당 알파벳이 얼마나 나왔는지 카운트해 주기위해서 만들었다. [0] * 26 도 된다.
    for character in text:
        code_current = ord(character) # 해당 분리되어있는 알파벳을 숫자형태로 바꿔준다.
        if code_a <= code_current <= code_z:
            count[code_current-code_a] += 1
    
    # 횟수를 세게 되면 값이 1이상의 값이 나오기 때문에 바꿔준다. -> 정규화 실시
    total = sum(count) # 카운트에 나온 빈도수를 모두 더해준다.
    # 그렇다면 그냥 count/total 하면 안되나? 해보면 count는 list형태이고 total은 int이므로 형이 맞지 않는다.
    # 이를 해결해 주기 위해서 map을 이용하여 각각의 값에 int, int 형태로 형을 맞춰주어 다시 count에 저장한다.
    count = list(map(lambda n: n/total,count ))# n이라는 매개변수를 넣고 return은 n/total로 해 준다.

    # 리스트에 넣기
    test_data.append(count) # 데이터 가공된 Input
    test_label.append(lang) # 데이터 가공된 정답

# 학습시키기
clf = svm.SVC() # 학습기 생성
clf.fit(train_data,train_label) 
predict = clf.predict(test_data)
ac_score = metrics.accuracy_score(test_label,predict)
print("정답률 : ",ac_score)
result = metrics.classification_report(test_label,predict) # 레포트를 만들어주는  녀석
print(" --- report --- ")
print(result)



'''
lambda n 의 형태는 기본적으로 이것이다. 바로 리턴해 주는 함수를  만들때 이용한다.
def test(n):
    return n
그렇다면 
'''


'''
clf = svm.SVC()
# 매개변수로 무엇을 어떻게 넣을 것인가?
# 1. 알파벳의 출현 빈도를 확률로 넣을 것이다. 2. 결과로 어떤 언어인지 정답을 알려준다.
clf.fit() 
predict = clf.predict()
ac_score = metrics.accuracy_score()
print("정답률 : ",ac_score)
'''