import skimage.io as io
import glob
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    dpath = '/home/geena/projects/brats/data/BRATS2015_Training/HGG/'
    flair = glob.glob(dpath+'/**/*Flair*/**.mha')
    t1 = glob.glob(dpath+'/**/*T1.*/**.mha')
    t1c = glob.glob(dpath+'/**/*T1c*/**.mha')
    t2 = glob.glob(dpath+'/**/*T2*/**.mha')
    ot = glob.glob(dpath+'/**/*OT*/**.mha')
    # img = io.imread(flair[0],plugin='simpleitk')
    # io.imshow(img[0])
    # plt.show()
    test =[]
    for i in range(len(ot)):
        img = io.imread(ot[i],plugin='simpleitk')
        test.append(img.shape)
    test = np.array(test)
