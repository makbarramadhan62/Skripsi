import cv2
import numpy as np
from os import walk
from os.path import join

# inisialisasi ukuran resize
width, height = 1080, 1920
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

# melakukan perulangan pada folder
for root, dirs, files in walk("../../DataSet_Training/Bercak_Daun/"):
    # validasi apakah terdapat file pada folder
    if files:
        # perulangan pada masing masing file untuk melakukan preprocessing
        for file in files:
            a = a+1
            # membaca file
            img = cv2.imread(join(root, file))
            # melakukan resize pada file
            img = cv2.resize(img, (width, height),
                             interpolation=cv2.INTER_AREA)
            # melakukan cropping pada file
            img = img[420:1500, 0:1080]
            # melakukan penulisan / penyimpanan file yang telah di preprocessing
            cv2.imwrite("../HasilPreProcessing/Bercak_Daun/"+"Data ke-" +
                        str(a)+".jpg", img)

for root, dirs, files in walk("../../DataSet_Training/Bercak_Merah/"):
    if files:
        for file in files:
            c = c+1
            img = cv2.imread(join(root, file))
            img = cv2.resize(img, (width, height),
                             interpolation=cv2.INTER_AREA)
            img = img[420:1500, 0:1080]
            cv2.imwrite("../HasilPreProcessing/Bercak_Merah/"+"Data ke-" +
                        str(c)+".jpg", img)

for root, dirs, files in walk("../../DataSet_Training/Daun_Sehat/"):
    if files:
        for file in files:
            d = d+1
            img = cv2.imread(join(root, file))
            img = cv2.resize(img, (width, height),
                             interpolation=cv2.INTER_AREA)
            img = img[420:1500, 0:1080]
            cv2.imwrite("../HasilPreProcessing/Daun_Sehat/"+"Data ke-" +
                        str(d)+".jpg", img)

for root, dirs, files in walk("../../DataSet_Training/Embun_Bulu/"):
    if files:
        for file in files:
            f = f+1
            img = cv2.imread(join(root, file))
            img = cv2.resize(img, (width, height),
                             interpolation=cv2.INTER_AREA)
            img = img[420:1500, 0:1080]
            cv2.imwrite("../HasilPreProcessing/Embun_Bulu/"+"Data ke-" +
                        str(f)+".jpg", img)

for root, dirs, files in walk("../../../DataSet/DataSet"):
    if files:
        for file in files:
            e = e+1
            img = cv2.imread(join(root, file))
            img = cv2.resize(img, (width, height),
                             interpolation=cv2.INTER_AREA)
            img = img[420:1500, 0:1080]
            cv2.imwrite("../../DataSet_Training/Hama_Tungau"+"Data ke-" +
                        str(e)+".jpg", img)
