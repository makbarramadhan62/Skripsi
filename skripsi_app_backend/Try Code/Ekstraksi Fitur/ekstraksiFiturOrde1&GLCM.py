import os
import cv2
import csv
import numpy as np
from scipy import stats
from skimage.feature import greycomatrix, greycoprops

# x = 0

# # membuka file CSV untuk menyimpan hasil ekstraksi fitur
# with open('../hasil_ekstraksi_orde1_glcm1.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(
#         ['label', 'Mean', 'Variance', 'Skewness', 'Kurtosis', 'Entropy', 'Contrast', 'Homogeneity', 'Energy'])

#     # melakukan ekstraksi fitur pada setiap folder
#     for root, dirs, files in os.walk('../DataSet_Training'):

#         x = x+1
#         # mengambil nama folder terakhir dari root
#         label = root.split('\\')[-1]

#         # mengambil semua file gambar di dalam folder
#         image_files = [f for f in files if f.endswith('.jpg')]

#         # melakukan ekstraksi fitur pada setiap gambar
#         for image_file in image_files:
#             # membaca gambar
#             image = cv2.imread(os.path.join(root, image_file))

#             # Mengubah gambar ke dalam format HSV
#             hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#             # Menghitung histogram warna HSV
#             hist = cv2.calcHist([hsv], [0, 1, 2], None, [
#                                 180, 256, 256], [0, 180, 0, 256, 0, 256])

#             # Membuat histogram menjadi 1D
#             hist = hist.ravel()

#             # Menghitung mean
#             mean = np.mean(hist)

#             # Menghitung varians
#             variance = np.var(hist)

#             # Menghitung skewness
#             skewness = stats.skew(hist)

#             # Menghitung kurtosis
#             kurtosis = stats.kurtosis(hist)

#             # Menghitung entropy
#             entropy = stats.entropy(hist)

#             # Hitung matriks glcm
#             image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#             glcm = greycomatrix(image_gray, [5], [0],
#                                 levels=256, symmetric=True, normed=True)

#             # Hitung fitur glcm
#             contrast = greycoprops(glcm, 'contrast')[0][0]
#             homogeneity = greycoprops(glcm, 'homogeneity')[0][0]
#             energy = greycoprops(glcm, 'energy')[0][0]

#             # Memasukkan nilai R,G,B, Contrast, Homogeneity dan Energy  ke dalam file CSV dengan label tertentu
#             writer.writerow([(x-1), mean, variance, skewness,
#                             kurtosis, entropy, contrast, homogeneity, energy])

# # Menutup file CSV
# csvfile.close()

# -------------------------------------------------------------------------------------------------------------------

x = 0

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../hasil_ekstraksi_orde1_glcm.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label', 'Mean_h', 'Variance_h', 'Skewness_h', 'Kurtosis_h', 'Entropy_h', 'Mean_s', 'Variance_s', 'Skewness_s', 'Kurtosis_s', 'Entropy_s', 'Mean_v', 'Variance_v', 'Skewness_v', 'Kurtosis_v', 'Entropy_v', 'Contrast', 'Homogeneity', 'Energy'])

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../DataSet_Training'):

        x = x+1
        # mengambil nama folder terakhir dari root
        label = root.split('\\')[-1]

        # mengambil semua file gambar di dalam folder
        image_files = [f for f in files if f.endswith('.jpg')]

        # melakukan ekstraksi fitur pada setiap gambar
        for image_file in image_files:
            # membaca gambar
            image = cv2.imread(os.path.join(root, image_file))

            # Mengubah gambar ke dalam format HSV
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            # Memisahkan kanal warna HSV
            h, s, v = cv2.split(hsv)

            # Menghitung histogram warna H
            hist_h = cv2.calcHist([h], [0], None, [180], [0, 180])

            # Membuat histogram menjadi 1D
            hist_h = hist_h.ravel()

            # Menghitung mean, variance, skewness, kurtosis, dan entropy dari histogram warna H
            mean_h = np.mean(hist_h)
            variance_h = np.var(hist_h)
            skewness_h = stats.skew(hist_h)
            kurtosis_h = stats.kurtosis(hist_h)
            entropy_h = stats.entropy(hist_h)

            # Menghitung histogram warna S
            hist_s = cv2.calcHist([s], [0], None, [256], [0, 256])

            # Membuat histogram menjadi 1D
            hist_s = hist_s.ravel()

            # Menghitung mean, variance, skewness, kurtosis, dan entropy dari histogram warna S
            mean_s = np.mean(hist_s)
            variance_s = np.var(hist_s)
            skewness_s = stats.skew(hist_s)
            kurtosis_s = stats.kurtosis(hist_s)
            entropy_s = stats.entropy(hist_s)

            # Menghitung histogram warna V
            hist_v = cv2.calcHist([v], [0], None, [256], [0, 256])

            # Membuat histogram menjadi 1D
            hist_v = hist_v.ravel()

            # Menghitung mean, variance, skewness, kurtosis, dan entropy dari histogram warna V
            mean_v = np.mean(hist_v)
            variance_v = np.var(hist_v)
            skewness_v = stats.skew(hist_v)
            kurtosis_v = stats.kurtosis(hist_v)
            entropy_v = stats.entropy(hist_v)

            # Hitung matriks glcm
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            glcm = greycomatrix(image_gray, [5], [0],
                                levels=256, symmetric=True, normed=True)

            # Hitung fitur glcm
            contrast = greycoprops(glcm, 'contrast')[0][0]
            homogeneity = greycoprops(glcm, 'homogeneity')[0][0]
            energy = greycoprops(glcm, 'energy')[0][0]

            # Memasukkan nilai R,G,B, Contrast, Homogeneity dan Energy  ke dalam file CSV dengan label tertentu
            writer.writerow([(x-1), mean_h, variance_h, skewness_h,
                            kurtosis_h, entropy_h, mean_s, variance_s, skewness_s,
                            kurtosis_s, entropy_s, mean_v, variance_v, skewness_v,
                            kurtosis_v, entropy_v, contrast, homogeneity, energy])

# Menutup file CSV
csvfile.close()
