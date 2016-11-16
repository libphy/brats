import skimage.io as io
import glob
import os
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def imagefetch(path, pid, modality, s):
    dpath = glob.glob(path+'/*'+pid+'*/*'+modality+'*/**.mha')
    img = io.imread(dpath[0],plugin='simpleitk')
    # io.imshow(img[s])
    # plt.show()
    return img

if __name__ == '__main__':
    hpath = os.getcwd()+'/data/2015/BRATS2015_Training/HGG/'
    lpath = os.getcwd()+'/data/2015/BRATS2015_Training/LGG/'
    tpath = os.getcwd()+'/data/2015/Testing/HGG_LGG/'
    #flair = glob.glob(dpath+'/**/*Flair*/**.mha')
    hlist = sorted(os.listdir(hpath))
    hlist = list(map(lambda x: x.split('_'),hlist))
    llist = sorted(os.listdir(lpath))
    llist = list(map(lambda x: x.split('_'),llist))
    tlist = sorted(os.listdir(tpath))
    tlist = list(map(lambda x: x.split('_'),tlist))
    hdf = pd.DataFrame(hlist, columns=['prefix','tag','pid','num'])
    ldf = pd.DataFrame(llist, columns=['prefix','tag','pid','num'])
    tdf = pd.DataFrame(tlist, columns=['prefix','tag','pid','num'])

    hc = Counter(hdf['pid'])
    hfilter = [(k,v) for k, v in hc.iteritems() if v>1]
    lc = Counter(ldf['pid'])
    lfilter = [(k,v) for k, v in lc.iteritems() if v>1]
    tc = Counter(tdf['pid'])
    tfilter = [(k,v) for k, v in tc.iteritems() if v>1]

    # testing the HGG-LGG overlap patients in training set

    hlc = lc-(lc-hc)
    hlpid = hlc.keys()
    img = imagefetch(hpath, hlpid[0], 'OT', 100)
    img0 = imagefetch(lpath, hlpid[0], 'OT', 100)
    print 'HGG+LGG set:', hlpid[0], 'hgg', set(img[100].flatten()), 'lgg', set(img0[100].flatten())
    hhc = hc-lc
    hhpid = hhc.keys()
    img2 = imagefetch(hpath, hhpid[0], 'OT',100)
    print 'HGG only set:', hhpid[0], set(img2[100].flatten())
    llc = lc-hc
    llpid = llc.keys()
    img3 = imagefetch(lpath, llpid[0], 'OT',100)
    print 'LGG only set:', llpid[0], set(img3[100].flatten())

    # test if there is difference in labels in HGG and LGG
    # => just picked 100th slice
    # => result: seems all kinds of label can occur in both cases
    # => for ten patients with both hgg and lgg, labels for hgg and lgg are different,
    # but basically all kinds of labels can show up in both hgg and lgg. there was no clear pattern.
    honly = list(map(lambda x: set(imagefetch(hpath,x,'OT',100)[100].flatten()),hhpid))
    lonly = list(map(lambda x: set(imagefetch(lpath,x,'OT',100)[100].flatten()),llpid))
    mixed1 = list(map(lambda x: set(imagefetch(hpath,x,'OT',100)[100].flatten()),hlpid))
    mixed2 = list(map(lambda x: set(imagefetch(lpath,x,'OT',100)[100].flatten()),hlpid))
