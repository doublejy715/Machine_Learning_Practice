from PIL import Image
import numpy as np

with open("./tower.jpg","rb") as file:
    img = Image.open(file)
    img = img.convert("RGB")
    img = img.resize((64,64)) # RGB 값이 64*64의 List형식으로 저장되어 있다.
    data = np.asarray(img)
    '''
    img.save("test.png") # 저장하기
    '''

    