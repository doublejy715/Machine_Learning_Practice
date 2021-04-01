from tensorflow.keras.layers import Dense,Conv2D,Input,MaxPool2D,ZeroPadding2D,BatchNormalization,Flatten,Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import Model
import csv
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image # 이미지 관련

# train file list
path_dir = os.getcwd() +'/data/train/train/'
file_list = os.listdir(path_dir)

# parameter
width,height = 128,128

# reshape image & save as array & save label
x_train,y_train = [],[]

for index in file_list:
    image = Image.open(path_dir + index)
    image = image.resize((width,height))# 먼저 크기를 조정해 주자
    data = np.asarray(image)

    # save label
    if index[:3] == 'cat':
        y_train.append(0)
    else:
        y_train.append(1)

    x_train.append(data)

#np.array() 하면 차수가 없어지고 벡터화 된다.
x_train = np.asarray(x_train)
y_train = to_categorical(y_train) # to_categorical 하면 array가 된다.

# stack Model(AlexNet)
Input_layer = Input(shape=(128,128,3))

    #layer_1
H1_Conv = Conv2D(32,kernel_size=3,strides=1,activation='relu')(Input_layer) 
H1_Max = MaxPool2D(pool_size=(2,2),strides=2)(H1_Conv)
H1_Batch = BatchNormalization()(H1_Max)

    #layer_2
H2_Zero = ZeroPadding2D(padding=(2,2))(H1_Batch)
H2_Conv = Conv2D(64,kernel_size=3,strides=2,activation='relu')(H2_Zero)
H2_Max = MaxPool2D(pool_size=(2,2),strides=2)(H2_Conv)
H2_Batch = BatchNormalization()(H2_Max)

    #layer_3
H3_Zero = ZeroPadding2D(padding=(1,1))(H2_Batch) 
H3_Conv = Conv2D(128,kernel_size=3,strides=2,activation='relu')(H3_Zero)
H3_Max = MaxPool2D(pool_size=(2,2),strides=2)(H3_Conv) 
H3_Batch = BatchNormalization()(H3_Max)

    #layer_4 
H4_Zero = ZeroPadding2D(padding=(1,1))(H3_Batch) 
H4_Conv = Conv2D(256,kernel_size=3,strides=2,activation='relu')(H4_Zero)
H4_Max = MaxPool2D(pool_size=(2,2),strides=2)(H4_Conv) 
H4_Batch = BatchNormalization()(H4_Max) 

    #layer_5
H5_Zero = ZeroPadding2D(padding=(1,1))(H4_Batch) 
H5_Conv = Conv2D(512,kernel_size=3,strides=1,activation='relu')(H5_Zero)
H5_Batch = BatchNormalization()(H5_Conv) 

    #layer_6 flatten 
H6_flat = Flatten()(H5_Batch) 

    #layer_7
H7_FC = Dense(4096,activation='relu')(H6_flat)
H7_Drop = Dropout(0.5)(H7_FC)

    #layer_8
H8_FC = Dense(1000,activation='relu')(H7_Drop)
H8_Drop = Dropout(0.5)(H8_FC)

    #layer_9
Output_layer = Dense(2,activation='softmax')(H8_Drop)

# set Model
model = Model(Input_layer,Output_layer)
model.summary()
model.compile(loss='categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])

# practice
model.fit(x_train,y_train,batch_size=200,epochs=10)

# Function call stack train function 이런 문제가 발생하면 batch_size를 줄이던가 하자!