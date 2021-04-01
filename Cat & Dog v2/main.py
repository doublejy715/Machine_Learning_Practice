# 참조 : https://lsjsj92.tistory.com/355 : 사이즈 조절
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model
from model import models
from opencv import Save_npz
import matplotlib.pyplot as plt
import csv
import os
import numpy as np
import pandas as pd

# Save & Load npz
Save_npz()

b = np.load('./save/save_file.npz')

# reshape image & save as array & save label
x_train,y_train = b['images'],b['labels']

# to_category
y_train = to_categorical(y_train)

Input_layer,Output_layer = models()

# set Model
model = Model(Input_layer,Output_layer)
model.summary()
model.compile(loss='categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])

# practice
model.fit(x_train,y_train,batch_size=200,epochs=10)
# 참조 : https://lsjsj92.tistory.com/355 : 사이즈 조절
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model
from model import models
import csv
import os
import numpy as np
import pandas as pd
import numpy.random # 항목을 섞기 위한 함수

b = np.load('./save/save_file.npz')

# reshape image & save as array & save label
x_data,y_data = b['images'],b['labels']

# data Nomalization(추가사항)
x_data =  x_data.astype('float32')/255

# to_category
y_data = to_categorical(y_data)

# shuffle idx(이건 데이터와 label을 동시에 섞기 위한 방법)(데이터 처리 과정에서 입력을 rand하고 label 만드는 방법도 생각해 볼 수 있을듯)
idx = np.arange(x_data.shape[0])
np.random.shuffle(idx)

x_data = x_data[idx]
y_data = y_data[idx]

# make validation_data(추가사항) --> 애초에 npz파일에 따로 저장하는 방법이 있나?
x_train,x_vali = x_data[:15000],x_data[15000:]
y_train,y_vali = y_data[:15000],y_data[15000:]

Input_layer,Output_layer = models()

# set Model
model = Model(Input_layer,Output_layer)
model.summary()
model.compile(loss='categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])

# practice
history = model.fit(x_train,y_train,batch_size=300,epochs=10,validation_data=(x_vali,y_vali))
print(history.history)

"""
# graph(model.fit의 출력으로 epoch마다 값을 저장한다.(list형식))
import matplotlib.pyplot as plt

def show_graph(history_dict):
    accuracy = history_dict['accuracy']
    val_accuracy = history_dict['val_accuracy']
    loss = history_dict['loss']
    val_loss = history_dict['val_loss']

    epochs = range(1, len(loss) + 1)
    
    plt.figure(figsize=(5, 5))
    
    plt.subplot(121)
    plt.subplots_adjust(top=2)
    plt.plot(epochs, accuracy, 'ro', label='Training accuracy')
    plt.plot(epochs, val_accuracy, 'r-', label='Validation accuracy')
    plt.title('Trainging and validation accuracy and loss')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy and Loss')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
              fancybox=True, shadow=True, ncol=5)
#     plt.legend(bbox_to_anchor=(1, -0.1))

    plt.subplot(122)
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b-', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=5)
#     plt.legend(bbox_to_anchor=(1, 0))
    plt.show()

show_graph(history.history)
"""