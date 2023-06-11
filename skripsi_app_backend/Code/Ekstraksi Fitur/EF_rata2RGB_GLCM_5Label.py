import os
import cv2
import csv
import numpy as np
from skimage.feature import greycomatrix, greycoprops

glcm_properties_1 = ['dissimilarity', 'correlation', 'homogeneity']
angles = [0, 45, 90, 135]

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB_GLCM/RGB_GLCM[all]1_Training.csv', 'w', newline='') as csvfile:
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
with open('../CSV/cropped_ROI/5_Label/RGB_GLCM/RGB_GLCM[all]1_Testing.csv', 'w', newline='') as csvfile:
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


glcm_properties_2 = ['dissimilarity', 'correlation', 'contrast']

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB_GLCM/RGB_GLCM[all]2_Training.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label', 'R', 'G', 'B'] + [f'{prop} {angle}' for prop in glcm_properties_2 for angle in angles])

    c = 0

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/5_Label/DataSet_Training'):

        c = c+1
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
                propery for name in glcm_properties_2 for propery in greycoprops(glcm, name)[0]]
            for item in glcm_props:
                feature.append(item)

            row = [(c-1), mean_r, mean_g, mean_b] + feature[:]
            writer.writerow(row)

# Menutup file CSV
csvfile.close()


# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB_GLCM/RGB_GLCM[all]2_Testing.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label', 'R', 'G', 'B'] + [f'{prop} {angle}' for prop in glcm_properties_2 for angle in angles])

    d = 0

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/5_Label/DataSet_Testing'):

        d = d+1
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
                propery for name in glcm_properties_2 for propery in greycoprops(glcm, name)[0]]
            for item in glcm_props:
                feature.append(item)

            row = [(d-1), mean_r, mean_g, mean_b] + feature[:]
            writer.writerow(row)

# Menutup file CSV
csvfile.close()


glcm_properties_3 = ['dissimilarity', 'homogeneity', 'contrast']

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB_GLCM/RGB_GLCM[all]3_Training.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label', 'R', 'G', 'B'] + [f'{prop} {angle}' for prop in glcm_properties_3 for angle in angles])

    e = 0

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/5_Label/DataSet_Training'):

        e = e+1
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
                propery for name in glcm_properties_3 for propery in greycoprops(glcm, name)[0]]
            for item in glcm_props:
                feature.append(item)

            row = [(e-1), mean_r, mean_g, mean_b] + feature[:]
            writer.writerow(row)

# Menutup file CSV
csvfile.close()


# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB_GLCM/RGB_GLCM[all]3_Testing.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label', 'R', 'G', 'B'] + [f'{prop} {angle}' for prop in glcm_properties_3 for angle in angles])

    f = 0

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/5_Label/DataSet_Testing'):

        f = f+1
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
                propery for name in glcm_properties_3 for propery in greycoprops(glcm, name)[0]]
            for item in glcm_props:
                feature.append(item)

            row = [(f-1), mean_r, mean_g, mean_b] + feature[:]
            writer.writerow(row)

# Menutup file CSV
csvfile.close()


glcm_properties_4 = ['correlation', 'homogeneity', 'contrast']

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB_GLCM/RGB_GLCM[all]4_Training.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label', 'R', 'G', 'B'] + [f'{prop} {angle}' for prop in glcm_properties_4 for angle in angles])

    g = 0

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/5_Label/DataSet_Training'):

        g = g+1
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
                propery for name in glcm_properties_4 for propery in greycoprops(glcm, name)[0]]
            for item in glcm_props:
                feature.append(item)

            row = [(g-1), mean_r, mean_g, mean_b] + feature[:]
            writer.writerow(row)

# Menutup file CSV
csvfile.close()


# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB_GLCM/RGB_GLCM[all]4_Testing.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['label', 'R', 'G', 'B'] + [f'{prop} {angle}' for prop in glcm_properties_4 for angle in angles])

    h = 0

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/5_Label/DataSet_Testing'):

        h = h+1
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
                propery for name in glcm_properties_4 for propery in greycoprops(glcm, name)[0]]
            for item in glcm_props:
                feature.append(item)

            row = [(h-1), mean_r, mean_g, mean_b] + feature[:]
            writer.writerow(row)

# Menutup file CSV
csvfile.close()
