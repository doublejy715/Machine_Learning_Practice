# 이건 ImageDataGenerator를 이용하지 않고 classification하는 방법
# 99%를 위해서, batch_nomalization, validation data 들 이용
# 'Dataset Augmentation'은 데이터 개수가 충분한것 같아(50000개) 적용하지 않음
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical
from model import models
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import cv2

data = np.load('./save_file.npz')

x_data,y_data=data['images'],data['labels']

# data Nomalization(추가사항)
x_data =  x_data.astype('float32')/255

# to_category
y_data = to_categorical(y_data)

# shuffle idx
idx = np.arange(x_data.shape[0])
np.random.shuffle(idx)

x_data = x_data[idx]
y_data = y_data[idx]

# make validation_data(추가사항) --> 애초에 npz파일에 따로 저장하는 방법이 있나?
x_train,x_vali = x_data[:30000],x_data[30000:]
y_train,y_vali = y_data[:30000],y_data[30000:]

# Model
Input_layer,Output_layer = models()
model = Model(Input_layer,Output_layer)
model.summary()
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

# practice
history = model.fit(x_data,y_data,batch_size=200,epochs=30,validation_data=(x_vali,y_vali))

# show in two graph
def show_graph(history_dict):
    accuracy = history_dict['accuracy']
    val_accuracy = history_dict['val_accuracy']
    loss = history_dict['loss']
    val_loss = history_dict['val_loss']

    epochs = range(1, len(loss) + 1)
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1,2,1) # 위치 지정
    plt.plot(epochs, accuracy, 'ro', label='Training accuracy')
    plt.plot(epochs, val_accuracy, 'r-', label='Validation accuracy')
    plt.title('Trainging and validation accuracy and loss')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy and Loss')
    plt.legend(bbox_to_anchor=(1, -0.1))

    plt.subplot(1,2,2)
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b-', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    
    plt.legend(bbox_to_anchor=(1, -0.1))
    plt.show()

show_graph(history.history)