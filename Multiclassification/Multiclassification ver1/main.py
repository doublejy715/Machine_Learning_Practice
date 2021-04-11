# 이건 ImageDataGenerator를 이용하지 않고 classification하는 방법
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

# Model
Input_layer,Output_layer = models()
model = Model(Input_layer,Output_layer)
model.summary()
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

# practice
history = model.fit(x_data,y_data,batch_size=200,epochs=30)

# show in two graph (이건 validation data 없는 경우 graph 형성)
def show_graph(history_dict):
    accuracy = history_dict['accuracy']
    loss = history_dict['loss']

    epochs = range(1, len(loss) + 1)
    
    plt.subplot(1,2,1) # 위치 지정
    plt.plot(epochs, accuracy, 'r-', label='Training accuracy')
    plt.title('Trainging and validation accuracy and loss')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy and Loss')
#     plt.legend(bbox_to_anchor=(1, -0.1))

    plt.subplot(1,2,2)
    plt.plot(epochs, loss, 'b-', label='Training loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
#     plt.legend(bbox_to_anchor=(1, 0))
    plt.show()

show_graph(history.history)