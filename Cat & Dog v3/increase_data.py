# 데이터 이미지를 뒤집거나 이동시키는 연습
# https://keraskorea.github.io/posts/2018-10-24-little_data_powerful_model/
# https://ballentain.tistory.com/4
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pylab as plt
"""
# 랜덤으로 바꿀 방식을 설정한다.
train_data_generator = ImageDataGenerator(
        rescale=1./255,
        featurewise_center=False,  # set input mean to 0 over the dataset
        samplewise_center=False,  # set each sample mean to 0
        featurewise_std_normalization=False,  # divide inputs by std of the dataset
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,  # apply ZCA whitening
        rotation_range=0,  # randomly rotate images in the range (degrees, 0 to 180)
        width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
        horizontal_flip=True,  # randomly flip images
        vertical_flip=False  # randomly flip images
        )

# 이것으로 배치 단위로 불러와 준다. 바로 input size로 수정이 가능하다.
# 이것으로 뽑은 이미지를 수정한다.
train_generator = train_data_generator.flow_from_directory(
    directory='./data/train_c/',
    target_size=(224, 224),
    batch_size=3,
    class_mode='binary'
    )


# 이 ImageDataGenerator이용시 model.fit 대신에,  model.fit_generator() 이용
# model.fit_generator(test_gernerator)안에 바로 넣어줘도 된다.
# 뭐지?? 정답 데이터는 어디로 넣어주나?
# 사용
# 뭔가 선행되어야 하는 데이터 형식이 필요하다
# 다른 곳 보면은 이미 x와 y의 값이 이미 연결되어 있다.
x_train, y_train = next(train_generator)
for idx in range(len(x_train)):  
    print(x_train[idx].shape)
    print(y_train[idx])
    plt.imshow(x_train[idx])
    plt.show()
"""

import tensorflow as tf
import numpy as np
import cv2
 
np.random.seed(15)
 
path = 'example'
 
generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range = 20,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    rescale = 1. / 255
    )
 
batch_size = 4
iterations = 5
images = []


obj = generator.flow_from_directory(
    path,
    target_size = (150, 150),
    batch_size = batch_size,
    class_mode = 'binary'
    )
 
 
for i in enumerate(range(iterations)):
    img, label = obj .next()
    print(label)
    n_img = len(label)

    base = cv2.cvtColor(img[0], cv2.COLOR_RGB2BGR)  # keras는 RGB, openCV는 BGR이라 변경함
    for idx in range(n_img - 1):
        img2 = cv2.cvtColor(img[idx + 1], cv2.COLOR_RGB2BGR)
        base = np.hstack((base, img2))
    images.append(base)
 
img = images[0]
for idx in range(len(images) - 1):
    img = np.vstack((img, images[idx + 1]))
cv2.imshow('result', img)
cv2.waitKey()
