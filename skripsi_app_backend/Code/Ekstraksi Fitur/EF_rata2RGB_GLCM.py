import os
import cv2
import csv
import numpy as np
from skimage.feature import greycomatrix, greycoprops

x = 0

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/5_Label/RGB_GLCM/RGB_GLCM[0]4_Training.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label', 'R', 'G', 'B', 'correlation', 'homogeneity', 'contrast'])

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/5_Label/DataSet_Training'):

        x = x+1
        # mengambil nama folder terakhir dari root
        label = root.split('\\')[-1]

        # mengambil semua file gambar di dalam folder
        image_files = [f for f in files if f.endswith('.jpg')]

        # melakukan ekstraksi fitur pada setiap gambar
        for image_file in image_files:
            # membaca gambar
            image = cv2.imread(os.path.join(root, image_file))

            # mengubah gambar ke dalam format RGB
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Hitung nilai rata-rata intensitas merah, hijau, dan biru
            mean_r, mean_g, mean_b = np.mean(rgb, axis=(0, 1))

            # Hitung matriks glcm
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            glcm = greycomatrix(image_gray, [5], [0],
                                levels=256, symmetric=True, normed=True)

            # Hitung fitur glcm
            contrast = greycoprops(glcm, 'correlation')[0][0]
            homogeneity = greycoprops(glcm, 'homogeneity')[0][0]
            energy = greycoprops(glcm, 'contrast')[0][0]

            # Memasukkan nilai R,G,B, Contrast, Homogeneity dan Energy  ke dalam file CSV dengan label tertentu
            writer.writerow([(x-1), mean_r, mean_g, mean_b,
                            contrast, homogeneity, energy])

# Menutup file CSV
csvfile.close()
