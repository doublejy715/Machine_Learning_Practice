import codecs
from bs4 import BeautifulSoup
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys

# 토지 내용 끌어오기
fp = codecs.open("./2BEXXX09.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body")
text = body.getText() + " "
print('코퍼스의 길이: ', len(text))

# 문자를 하나하나 읽어 들이고 ID 붙이기
chars = sorted(list(set(text))) # 내부에 들어가 있는 글자 하나하나 분리하여 list형태로 저장한다
print('사용되고 있는 문자의 수:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars)) # 문자 → ID
indices_char = dict((i, c) for i, c in enumerate(chars)) # ID → 문자
    # ID와 문자가 서로 상호작용 할 수 있도록 만들어준다.
# 텍스트를 maxlen개의 문자로 자르고 다음에 오는 문자 등록하기
maxlen = 20 # sentences에 들어갈 문장의 길이
step = 3 # 본문에서 3글자씩 뛰어넘고 다음 예상 단어를 추출하게 된다.
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
# sentences를 통해서 현재 어떠한 문장이 있는지 저장한다.
# next_chars를 통해서 sentences다음에 어떤 단어가 올지 예상하게 된다.

print('학습할 구문의 수:', len(sentences))
print('텍스트를 ID 벡터로 변환합니다...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
# data : x(원소가 모두 0데이터)를 모두 bool형식으로 만들어서 리턴(len(sentences)*maxlen*len(chars) 크기의 배열을 형성한다.)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
# label y(원소가 모두 0데이터)를 모두 bool형식으로 만들어서 리턴
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1 
    y[i, char_indices[next_chars[i]]] = 1
    # 결국은 x문장이 오면 다음 단어로 y를 가리키게 된다.

# 모델 구축하기(LSTM)
print('모델을 구축합니다...')
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)
# 후보를 배열에서 꺼내기
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)
# 학습시키고 텍스트 생성하기 반복
for iteration in range(1, 60):
    print()
    print('-' * 50)
    print('반복 =', iteration)
    model.fit(X, y, batch_size=128, nb_epoch=1) # 
    # 임의의 시작 텍스트 선택하기
    start_index = random.randint(0, len(text) - maxlen - 1) # 이후에 maxlen 만큼 뽑을것이기 때문에 길이 조정
    # 다양한 다양성의 문장 생성
    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print()
        print('--- 다양성 = ', diversity)
        generated = ''
        sentence = text[start_index: start_index + maxlen] # 아무런 문장의 시작점을 뽑아오는 문장
        generated += sentence # 문장을 넣어준다.
        print('--- 시드 = "' + sentence + '"')
        sys.stdout.write(generated)
        # 시드를 기반으로 텍스트 자동 생성
        for i in range(400): # 400번 반복
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.
            # 다음에 올 문자를 예측하기
            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]
            # 출력하기
            generated += next_char # 한글자 추가
            sentence = sentence[1:] + next_char # 계속해서 앞글자를 반복한다.(400번)
            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()

# 계속해서 다음에 나올 단어들을 예측하여 학습한다. -> 문장 생성