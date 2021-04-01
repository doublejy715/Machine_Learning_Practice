import os
import cv2
import numpy as np

def Save_npz():
    # 현재 경로 불러오기
    directory = os.getcwd()

    # 이미지 목록 가져오기
    file_list = os.listdir('./data/train/train/')

    # 이미지 열기(1개)
    img = cv2.imread('./data/train/train/cat.0.jpg')

    # 이미지 데이터 저장 해보기 
    Images,Labels = [],[]
    # enumerate(x1)는 기본적으로 index,x1의 원소를 반환해 준다.
    for name in file_list: 
        image = cv2.imread('./data/train/train/'+ name) # load image
        image = cv2.resize(image,(128,128)) # resize image
        Images.append(np.array(image)) # save image to array

        # save label
        if name[:3] == 'cat':
            Labels.append([0])
        else:
            Labels.append([1])

    Images = np.array(Images)
    Labels = np.array(Labels)

    # save npz
    file_names = 'save_file'
    Save = np.savez('./save/'+file_names+'.npz',images=Images,labels=Labels) # 따로따로 어떤 항목으로 저장할지 지정합니다.