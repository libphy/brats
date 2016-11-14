# BRATS2016
## 11-13-16
#### Data directory structure:  
Downloaded data from [smir repository brats2016 version](https://www.smir.ch/BRATS/Start2016)- the size is about 2 GB, the folder name is BRATS2015_Training. It has only training set- it is divided to HGG and LGG. Then each folder, it has bunch of patients folders brats_2013_xxx and brats_tcia_xxx, then each has 5 folders with different modality, and each folder has a .mha file.

#### File format:
.mha file format is a special image format widely used in medical imaging. It seems that there are several python packages to read this format such as MedPy, ITK. Some people suggest to use scikit-image with a plugin for simplicity ([more](http://stackoverflow.com/questions/29738822/how-to-convert-mha-file-to-nii-file-in-python-without-using-medpy-or-c)). Nikki used this as well.

#### The image:
When reading using skimage.io.imread, it loads the image to numpy array with a size of (155,240,240). It is possible that the image size and number of stacks might vary depending on the equipment. Anyway, the stacks have sometimes completely dark (all zeros) images.

#### Using glob:
glob can get multiple file paths from various subfolders at once.  
(ex: getting the file path for all Flair images)
```python
import glob as glob
dpath = '/home/geena/projects/brats/data/BRATS2015_Training/HGG/'
flist = glob.glob(dpath+'/**/*Flair*/**.mha')
```
