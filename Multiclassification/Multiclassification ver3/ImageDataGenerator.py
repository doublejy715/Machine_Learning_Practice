from tensorflow.keras.preprocessing.image import ImageDataGenerator

def Image_Data_Generator():
    # Augmentation : 이미지의 augmentation을 어떻게 할지 설정하는 식
    datagen = ImageDataGenerator(
            rotation_range=20,          # 이미지 회전 범위
            width_shift_range=0.2,      # 이미지 평행 이동
            height_shift_range=0.2,
            rescale=1./255,             # Nomalization
            shear_range=0.2,            # 임의 전단 변환 범위
            zoom_range=0.2,             # 임의 확대/축소 범위
            horizontal_flip=True        # 50% 확률로 이미지 뒤집기
            )        

    # 데이터를 전처리 하는 함수인 flow_from_directory
    # 폴더를 기준으로 하여 to_categorical을 실시한다.
    # train_generator에 기존 이미지, 변환 이미지, label(to_categorical) 한 녀석이 다들어있다.
    train_generator = datagen.flow_from_directory(
            './datasets/',  # this is the target directory (폴더로 나뉘어진 부분으로 이동한다. )
            target_size=(32, 32),  # 모든 이미지의 크기가 32x32로 조정됩니다.
            batch_size=500,
            class_mode='categorical')  # binary_crossentropy 손실 함수를 사용하므로 binary 형태로 라벨을 불러와야 합니다.

    return train_generator