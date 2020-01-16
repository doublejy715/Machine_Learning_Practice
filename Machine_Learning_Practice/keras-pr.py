'''
이것으로 bmi.scv 파일을 형성한다.
import random
# BMI를 계산해서 레이블을 리턴하는 함수
def calc_bmi(h, w):
    bmi = w / (h/100) ** 2
    if bmi < 18.5: return "thin"
    if bmi < 25: return "normal"
    return "fat"
# 출력 파일 준비하기
fp = open("bmi.csv","w",encoding="utf-8")
fp.write("height,weight,label\r\n")
# 무작위로 데이터 생성하기
cnt = {"thin":0, "normal":0, "fat":0}
for i in range(20000):
    h = random.randint(120,200)
    w = random.randint(35, 80)
    label = calc_bmi(h, w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(h, w, label))
fp.close()
print("ok,", cnt)
'''
# 모듈을 읽어 들인다.
import pandas as pd, numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping

# 데이터를 가공한다.
'''
원하는 데이터의 모습
[
    [<키>/200 ,<몸무게>/100], # 여기에 존재하는 값 또한 0.0 ~ 1.0 으로 바꾸어준다.
    [<키>/200 ,<몸무게>/100],
    [<키>/200 ,<몸무게>/100]
]
[
    'thin', # [1,0,0]
    'normal', # [0,1,0]
    'fat' # [0,0,1]
]
위의 과정을 pandas를 이용해서 만들어보자.
'''
csv = pd.read_csv("bmi3.csv") # 데이터가 존재하는 파일을 읽어온다.

print(csv)
# weigth, height의 값들을 정규화 시켜준다.(input)
csv["weigth"] = csv["weigth"] / 100 # csv 목차 중에서 weight의 value를 모두 들고와서 100으로 나누어준다.
csv["height"] = csv["height"] / 200
print(csv)
# value의 값 또한 정규화 시킨다.(value)
bmi_class = { # dict형식을 이용해서 key값으로 받아낸다.
    "thin" : [1,0,0],
    "normal" : [0,1,0],
    "fat" : [0,0,1]
}
y = np.empty((20000,3))
'''
[
    [0,0,0]
    [0,0,0]
    ...
    [0,0,0]
]
'''
for i,v in enumerate(csv["label"]):
    y[i] = bmi_class[v] # label에 존재하는 것을 모두 bmi_class에 키로 넣어 답안지를 숫자로 만들어낸다.

x = csv[["weight","height"]].as_matrix()

  # 학습시킬 데이터와 테스트할 데이터를 구분시켜준다.
x_train, y_train = x[1:15001], y[1:15001] # 15000개
x_test, y_test = x[15001:20001], y[15001:20001] # 5000개

# 모델을 만든다.
model  = Sequential()
model.add(Dense(512,input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))
model.add(Activation('softmax'))
    # 레이어 형성, compile의 매개변수는 keras홈페이지를 참조한다.
model.compile("rmsprop","categorical_corssentropy",metrics=['accuracy'])

# 학습을 시킨다.
model.fit(x_train,y_train)
# 예측을 한다. model.predit()
# 정답률을 구한다.
score = model.evaluate(x_test,y_test)
print("score:",score)