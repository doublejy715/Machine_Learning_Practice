# fit함수의 매개변수를 어떻게 넣어야 할까???

import pandas
from sklearn import model_selection, svm, metrics
'''
input = "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 67 232 39 0 0 0 0 0 0 0 0 0 62 81 0 0 0 0 0 0 0 0 0 0 0 0 0 0 120 180 39 0 0 0 0 0 0 0 0 0 126 163 0 0 0 0 0 0 0 0 0 0 0 0 0 2 153 210 40 0 0 0 0 0 0 0 0 0 220 163 0 0 0 0 0 0 0 0 0 0 0 0 0 27 254 162 0 0 0 0 0 0 0 0 0 0 222 163 0 0 0 0 0 0 0 0 0 0 0 0 0 183 254 125 0 0 0 0 0 0 0 0 0 46 245 163 0 0 0 0 0 0 0 0 0 0 0 0 0 198 254 56 0 0 0 0 0 0 0 0 0 120 254 163 0 0 0 0 0 0 0 0 0 0 0 0 23 231 254 29 0 0 0 0 0 0 0 0 0 159 254 120 0 0 0 0 0 0 0 0 0 0 0 0 163 254 216 16 0 0 0 0 0 0 0 0 0 159 254 67 0 0 0 0 0 0 0 0 0 14 86 178 248 254 91 0 0 0 0 0 0 0 0 0 0 159 254 85 0 0 0 47 49 116 144 150 241 243 234 179 241 252 40 0 0 0 0 0 0 0 0 0 0 150 253 237 207 207 207 253 254 250 240 198 143 91 28 5 233 250 0 0 0 0 0 0 0 0 0 0 0 0 119 177 177 177 177 177 98 56 0 0 0 0 0 102 254 220 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 169 254 137 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 169 254 57 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 169 254 57 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 169 255 94 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 169 254 96 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 169 254 153 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 169 255 153 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 96 254 153 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
input = input.split(' ') # 이렇게 하면 input을 리스트 형식으로 띄어쓰기를 기준으로 하여 구분짓게 된다.(28*28개의 1차원 list가 나온다.)

for i in range(len(input)): # 위의 input을 28*28pixel의 binary 형식으로 표현하기 위해서 가다듬는 과정이다.
    print("{:3}".format(input[i]),end=" ")
    if i % 28 == 0:
        print()
이제 clf.fit()을 통해서 올바른 데이터 값을 넣어주고, 올바른 value를 넣어줄 것이다.
대신에 하나씩 하면 너무 귀찮으므로 pandas를 이용하기로 한다.
'''
# pandas를 통해서 파일을 불러 온다.
train_csv = pandas.read_csv("./mnist/train.csv",header=None)
tk_csv = pandas.read_csv("./mnist/t10k.csv",header=None)

# 이 정의를 통해서 0~1 사이의 값으로 편환시킨다.    
def test(l):
    output = []
    for i in l:
        output.append(float(i) / 256)
    return output

# 들고온 파일을 행렬을 통해서 분리시킨다.
train_csv_data = list(map(test,train_csv.iloc[:,1:].values)) # 일정 범위의 행렬을 선택하도록 해 준다.
train_csv_label = train_csv[0].values

tk_csv_data = list(map(test,tk_csv.iloc[:,1:].values))
tk_csv_label = tk_csv[0].values

clf = svm.SVC()
# fit 안에 들어가는 data의 각각 value 들은 0~1사이의 값을 가지고 있어야 하므로 가공이 필요하다. 
clf.fit(train_csv_data, train_csv_label) 
predict = clf.predict(tk_csv_data)
score = metrics.accuracy_score(tk_csv_label,predict)
print("정답률:", score)

