from tensorflow.keras.layers import Dense,Conv2D,Input,MaxPool2D,ZeroPadding2D,BatchNormalization,Flatten,Dropout

def models():
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
    
    return Input_layer,Output_layer