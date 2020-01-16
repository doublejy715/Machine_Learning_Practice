'''
예시로  '몇|번|을|쓰러지다|몇|번|을|무너지나|다시|일어나다' 문장이 있다.

# 단어 배치
word_dictionary # 이 dict안에 key가 존재하지 않으면 단어를 key로 추가하고 값을 지정하여 준다.
{
    "몇":1,
    "번":2,
    ...         # 중복이 발생하게 되면 추가하지 않는다.
    "일어나다":7
}
위의 것을 기반으로 data를 만들게 된다.
data            # 위의 Key가 몇번 나오는지 카운트 하여 data[value]=count 형식으로 기록한다.
[2,2,2,1,1,1,1]

'''
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn import model_selection, metrics
import json
max_words = 56681 # 입력 단어 수: word-dic.json 파일 참고
nb_classes = 5 # 6개의 카테고리
batch_size = 64 
nb_epoch = 20
# MLP 모델 생성하기 --- (※1)
def build_model():
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])
    return model
# 데이터 읽어 들이기--- (※2)
data = json.load(open("./newstext/data-mini.json")) 
#data = json.load(open("./newstext/data.json"))
X = data["X"] # 텍스트를 나타내는 데이터(출현 빈도)
Y = data["Y"] # 카테고리 데이터
# 학습하기 --- (※3)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
Y_train = np_utils.to_categorical(Y_train, nb_classes)
print(len(X_train),len(Y_train))
    # 해당 부분에는 반드시 단어형태가 아닌 벡터 형태로 값을 넣어줘야 하므로 벡터화 시켜줘야 한다.
model = KerasClassifier( 
    build_fn=build_model, 
    nb_epoch=nb_epoch, 
    batch_size=batch_size)
model.fit(X_train, Y_train)
    # 어떠한 X_train, Y_train을 넣었는지 확인할 필요가 있다.
# 예측하기 --- (※4)
y = model.predict(X_test)
ac_score = metrics.accuracy_score(Y_test, y)
cl_report = metrics.classification_report(Y_test, y)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)