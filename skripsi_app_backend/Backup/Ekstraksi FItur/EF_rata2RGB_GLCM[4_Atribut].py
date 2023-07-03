import os
import cv2
import csv
import numpy as np
from skimage.feature import greycomatrix, greycoprops

glcm_properties_1 = ['dissimilarity', 'correlation', 'homogeneity', 'contrast']
angles = [0, 45, 90, 135]

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB_GLCM/RGB_GLCM[4_atribut]_Training.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label', 'R', 'G', 'B'] + [f'{prop} {angle}' for prop in glcm_properties_1 for angle in angles])

    a = 0

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/5_Label/DataSet_Training'):

        a = a+1
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
            glcm = greycomatrix(image_gray, distances=[5], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4],
                                levels=256, symmetric=True, normed=True)

            # Hitung fitur glcm
            feature = []
            glcm_props = [
                propery for name in glcm_properties_1 for propery in greycoprops(glcm, name)[0]]
            for item in glcm_props:
                feature.append(item)

            row = [(a-1), mean_r, mean_g, mean_b] + feature[:]
            writer.writerow(row)

# Menutup file CSV
csvfile.close()


# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB_GLCM/RGB_GLCM[4_Atribut]_Testing.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label', 'R', 'G', 'B'] + [f'{prop} {angle}' for prop in glcm_properties_1 for angle in angles])

    b = 0

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/5_Label/DataSet_Testing'):

        b = b+1
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
            glcm = greycomatrix(image_gray, distances=[5], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4],
                                levels=256, symmetric=True, normed=True)

            # Hitung fitur glcm
            feature = []
            glcm_props = [
                propery for name in glcm_properties_1 for propery in greycoprops(glcm, name)[0]]
            for item in glcm_props:
                feature.append(item)

            row = [(b-1), mean_r, mean_g, mean_b] + feature[:]
            writer.writerow(row)

# Menutup file CSV
csvfile.close()
