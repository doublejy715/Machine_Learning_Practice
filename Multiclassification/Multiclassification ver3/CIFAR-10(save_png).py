# 참조 : https://gist.github.com/jo7ueb/2ac148463ce17a3cf69786ac05e74096
from chainer.datasets import get_cifar10
import cv2

# 이건 CIFAR-10 데이터 셋을 저장하는 방법
def get_dataset():
    return get_cifar10()

def save_png(img, name):
    # swap axis: chainer(C x H x W) -> opencv(H x W x C)
    nimg = img.transpose(1, 2, 0)
    nimg *= 255
    cimg = cv2.cvtColor(nimg, cv2.COLOR_RGB2BGR)
    cv2.imwrite(name, cimg)
    print(name + ' saved!')

def main():
    train, test = get_dataset()
    print('type of test {}'.format(type(test)))
    print('length of test  {}'.format(len(test)))
    print('length of train {}'.format(len(train)))

    t0 = train[0]
    print('type of t0 {}'.format(type(t0)))
    print('length of t0 {}'.format(len(t0)))
    print('t0[0] {}'.format(t0[0]))
    print('t0[1] {}'.format(t0[1]))
    print('type of t0[0] {}'.format(type(t0[0])))
    print('type of t0[1] {}'.format(type(t0[1])))

    img = t0[0]
    print('shape of img {}'.format(img.shape))

    for i, d in enumerate(train):
        img = d[0]
        label = d[1]
        name = 'C:/workspace/ML/practice/multi classification ver1/pngs/train_label%d_%05d.png' % (label, i)
        save_png(img, name)
        print('{} saved!'.format(name))

if __name__ == '__main__':
    main()
"""
# 이건 각 label을 파일별로 저장하기 위한 방법이다.
import shutil
import os

path = 'C:/workspace/ML/practice/multi classification ver1/'

def make_directory(dir_path,label):
    if not os.path.exists(dir_path + 'datasets/' + label):
        os.mkdir(dir_path + 'datasets/' + label)

file_list = os.listdir(path + 'pngs/')
for name in file_list:
    make_directory(path,name[11])
    src = path + 'pngs/'
    dire = path + 'datasets/' + name[11] + '/'
    shutil.move(src + name, dire + name)"""