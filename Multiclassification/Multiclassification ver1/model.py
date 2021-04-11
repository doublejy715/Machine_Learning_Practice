from tensorflow.keras.layers import Dense,Conv2D,Input,MaxPool2D,ZeroPadding2D,BatchNormalization,Flatten,Dropout
from tensorflow.keras.models import Model

def models():
        # stack Model(AlexNet)
    Input_layer = Input(shape=(32,32,3))

        #layer_1 32,32,3
    H1_Conv = Conv2D(32,kernel_size=3,strides=1,activation='relu')(Input_layer) 
    H1_Max = MaxPool2D(pool_size=(2,2),strides=2)(H1_Conv)

        #layer_2 16,16
    H2_Zero = ZeroPadding2D(padding=(2,2))(H1_Max)
    H2_Conv = Conv2D(64,kernel_size=3,strides=2,activation='relu')(H2_Zero)
    H2_Max = MaxPool2D(pool_size=(2,2),strides=2)(H2_Conv)

        #layer_3 8,8
    H3_Zero = ZeroPadding2D(padding=(1,1))(H2_Max) 
    H3_Conv = Conv2D(128,kernel_size=3,strides=2,activation='relu')(H3_Zero)
    H3_Max = MaxPool2D(pool_size=(2,2),strides=2)(H3_Conv) 

        #layer_4 flatten 
    H4_flat = Flatten()(H3_Max) 

        #layer_6
    H5_FC = Dense(1000,activation='relu')(H4_flat)
    H5_Drop = Dropout(0.5)(H5_FC)

        #layer_7
    H6_FC = Dense(500,activation='relu')(H5_Drop)
    H6_Drop = Dropout(0.5)(H6_FC)

        #layer_8
    Output_layer = Dense(10,activation='softmax')(H6_Drop)
    
    return Input_layer,Output_layer
