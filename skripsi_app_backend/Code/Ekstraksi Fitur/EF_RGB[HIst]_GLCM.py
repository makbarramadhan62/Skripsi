import os
import cv2
import csv
import numpy as np
from skimage.feature import graycomatrix, graycoprops

glcm_properties = ['dissimilarity', 'correlation', 'homogeneity', 'contrast']
angles = [0, 45, 90, 135]
distance = [5]
bins = 16

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/RGB[Hist-16]_GLCM[S4-D5]_160_ROI_Training.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label'] + ['hist_r' + str(i+1) for i in range(bins)] + ['hist_g' + str(i+1) for i in range(bins)] + ['hist_b' + str(i+1) for i in range(bins)] + [f'{prop} {angle}' for prop in glcm_properties for angle in angles])

    # melakukan ekstraksi fitur pada setiap folder
    for a, (root, dirs, files) in enumerate(os.walk('../Dataset/preprocessed_roi_augmentation/5_label/DataSet_Training'), start=0):

        # mengambil nama folder terakhir dari root
        label = root.split('\\')[-1]

        # mengambil semua file gambar di dalam folder
        image_files = [f for f in files if f.endswith('.jpg')]

        # melakukan ekstraksi fitur pada setiap gambar
        for image_file in image_files:
            # membaca gambar
            image = cv2.imread(os.path.join(root, image_file))

            # Konversi gambar ke ruang warna rgb
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            r, g, b = cv2.split(rgb_image)  # Pisahkan channel R, G, dan B

            # Hitung histogram untuk channel H
            hist_r = cv2.calcHist([r], [0], None, [bins], [0, 256])
            # Mengubah histogram R menjadi array 1 dimensi
            hist_r = np.ravel(hist_r)

            # Hitung histogram untuk channel S
            hist_g = cv2.calcHist([g], [0], None, [bins], [0, 256])
            # Mengubah histogram G menjadi array 1 dimensi
            hist_g = np.ravel(hist_g)

            # Hitung histogram untuk channel V
            hist_b = cv2.calcHist([b], [0], None, [bins], [0, 256])
            # Mengubah histogram B menjadi array 1 dimensi
            hist_b = np.ravel(hist_b)

            # Hitung matriks glcm
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            glcm = graycomatrix(image_gray, distances=distance, angles=[
                                0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)

            # Hitung fitur glcm
            feature_glcm = []
            glcm_props = [
                propery for name in glcm_properties for propery in graycoprops(glcm, name)[0]]
            for item in glcm_props:
                feature_glcm.append(item)

            row = [a] + [*hist_r, *hist_g, *hist_b] + feature_glcm
            writer.writerow(row)

# Menutup file CSV
csvfile.close()

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/RGB[Hist-16]_GLCM[S4-D5]_160_ROI_Testing.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label'] + ['hist_r' + str(i+1) for i in range(bins)] + ['hist_g' + str(i+1) for i in range(bins)] + ['hist_b' + str(i+1) for i in range(bins)] + [f'{prop} {angle}' for prop in glcm_properties for angle in angles])

    # melakukan ekstraksi fitur pada setiap folder
    for a, (root, dirs, files) in enumerate(os.walk('../Dataset/preprocessed_roi_augmentation/5_label/DataSet_Testing'), start=0):

        # mengambil nama folder terakhir dari root
        label = root.split('\\')[-1]

        # mengambil semua file gambar di dalam folder
        image_files = [f for f in files if f.endswith('.jpg')]

        # melakukan ekstraksi fitur pada setiap gambar
        for image_file in image_files:
            # membaca gambar
            image = cv2.imread(os.path.join(root, image_file))

            # Konversi gambar ke ruang warna rgb
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            r, g, b = cv2.split(rgb_image)  # Pisahkan channel R, G, dan B

            # Hitung histogram untuk channel H
            hist_r = cv2.calcHist([r], [0], None, [bins], [0, 256])
            # Mengubah histogram R menjadi array 1 dimensi
            hist_r = np.ravel(hist_r)

            # Hitung histogram untuk channel S
            hist_g = cv2.calcHist([g], [0], None, [bins], [0, 256])
            # Mengubah histogram G menjadi array 1 dimensi
            hist_g = np.ravel(hist_g)

            # Hitung histogram untuk channel V
            hist_b = cv2.calcHist([b], [0], None, [bins], [0, 256])
            # Mengubah histogram B menjadi array 1 dimensi
            hist_b = np.ravel(hist_b)

            # Hitung matriks glcm
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            glcm = graycomatrix(image_gray, distances=distance, angles=[
                                0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)

            # Hitung fitur glcm
            feature_glcm = []
            glcm_props = [
                propery for name in glcm_properties for propery in graycoprops(glcm, name)[0]]
            for item in glcm_props:
                feature_glcm.append(item)

            row = [a] + [*hist_r, *hist_g, *hist_b] + feature_glcm
            writer.writerow(row)

# Menutup file CSV
csvfile.close()
