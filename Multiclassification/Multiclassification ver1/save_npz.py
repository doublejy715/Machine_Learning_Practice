import os
import cv2
import numpy as np
from sklearn.utils import shuffle

# parameter
path = './'
Images, Labels = [],[]

# bring image list
file_list = os.listdir('./pngs/')

# save i
for name in file_list:
    image = cv2.imread('./pngs/' + name)
    Images.append(np.array(image))
    
    Labels.append([int(name[11])])

Images = np.array(Images)
Labels = np.array(Labels)

# save npz
Save = np.savez('./save_file.npz',images=Images,labels=Labels)

# check npz file
b = np.load('./save_file.npz')
print(b['labels'])