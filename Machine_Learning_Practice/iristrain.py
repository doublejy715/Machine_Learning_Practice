import pandas
from sklearn import svm, metrics
# 가공된 데이터의 모습을 잘 파악해야한다.
# 해당 데이터는 맨 마지막 값은 str형시이다. 숫자로 대치한다.

# pandas 원하는 열을 추출하기 위함이다.(나중에 추가설명)
csv = pandas.read_csv('iris.csv') 
# 경로 설정은 이미 가상화 환경에서 해당 파일에 들어가 있는 상태이므로 '(파일명)'을 해 주면 된다.
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

# 이제 데이터를 가공하였으니 직접 학습시켜보자.
clf = svm.SVC()
clf.fit(data,label) # 입력 형식은 반드시 List형식
results=clf.predict([ # 예측하고자 하는 값을 넣어준다.
    [5.1, 3.0, 1.3, 0.2]
])
print(results)
"""
# score = metrics.accuracy_score()
# print("정답률:",score)
"""

# 이것으로 데이터를 통해 붓꽃의 품종을 파악하는 머신러닝을 만들었다.