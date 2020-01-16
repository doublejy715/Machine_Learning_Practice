# 데이터를 학습을 위한, 테스트를 위한 항목으로 나누어 데이터를 가공한다.

import pandas
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split


csv = pandas.read_csv('iris.csv') 

data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

# 데이터 나누기
train_data, test_data, train_label, test_label = train_test_split(data, label)

clf = svm.SVC()
clf.fit(train_data,train_label) 
results=clf.predict(test_data)

score = metrics.accuracy_score(results, test_label)
print("정답률:",score)
# 정답률이 높댜 -> 올바르게 품종 측정이 가능하다.
# 이제 CSV데이터를 가공해서 머신러닝을 시킬 수 있는 코드 작성 가능

# 흐름을 파악한다. 