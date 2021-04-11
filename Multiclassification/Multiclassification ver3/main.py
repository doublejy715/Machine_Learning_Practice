# 이건 ImageDataGenerator를 이용하지 않고 classification하는 방법
# 99%를 위해서, batch_nomalization, validation data 들 이용
# 'Dataset Augmentation'은 데이터를 일부 삭제하여 부족한 상황을 만들었음
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from model import models
from graph import show_graph
from ImageDataGenerator import Image_Data_Generator
import cv2

train_generator = Image_Data_Generator()

# Model
Input_layer,Output_layer = models()
model = Model(Input_layer,Output_layer)
model.summary()
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

# practice
# (ImageDataGenerator을 이용시 fit_generator을 이용한다.)
history = model.fit_generator(train_generator,steps_per_epoch = 20,epochs=50) # flow_from_directory 에서의 batch_size를 참고한다. steps_per_epoch은 한 번 epoch 돌 때, 데이터를 몇 번 볼 것인가를 정해준다

# show_graph
show_graph(history.history)

# 되긴 되는데.... 컴퓨터 성능이 딸려서 많이 학습을 하지 못한다. 특히 steps_per_epoch를 많이 늘리지 못함
