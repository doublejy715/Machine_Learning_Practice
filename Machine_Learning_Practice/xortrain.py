from sklearn import svm, metrics

'''
clf = svm.SVC()
clf.fit(data, answer) 해당 매개변수는 list로 감싸서 여러개 보낼 수 있다.
clf.predict() 학습한 내용을 가지고 예측을 해 보는 함수이다(실제적인 답을 얻는 곳)
사실 이 3줄이 모두라고 해도 무방하다.
** 예시
clf = svm.SVC()
clf.fit([ # data를 준다. 
    [0,0], # 해당 요소를 '벡터'라고 하고 이것을 잘 넣어주는것이 매우 중요하다.
    [1,0],
    [0,1],
    [1,1]
],[ # answer를 준다.
    0,
    1,
    1,
    0
])
result = clf.predict([
    [0,0], # 0
    [1,0] # 1
])
'''
# 정답률을 추가적으로 구해본다.(metrics.accuracy_score()로 확인 가능)

datas = [[0,0], [1,0],[0,1],[1,1]]
labels = [0,1,1,0]
examples = [[0,0],[1,0]]
examples_label = [0,1]

clf =  svm.SVC()
clf.fit(datas,labels)
results = clf.predict(examples)
score = metrics.accuracy_score(examples_label,results) # 실제 예시에 대한 결과값과, predict함수로 인해서 나오는 results값들을 비교해서 정답률을 비교한다.
print("정답률",score) # 정답률은 1.0이 100%이다.