import cv2
import numpy as np
import os
import csv


# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB/RGB_Training.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['R', 'G', 'B', 'label'])

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

            # # mengubah gambar ke dalam format RGB
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # # mengambil nilai red (R) dari gambar
            red = rgb[:, :, 0]

            # # mengambil nilai green (G) dari gambar
            green = rgb[:, :, 1]

            # # mengambil nilai blue (B) dari gambar
            blue = rgb[:, :, 2]

            # # membuat list untuk menyimpan hasil ekstraksi fitur
            features = []

            # # menambahkan nilai R ke dalam list
            features.append(np.mean(red))

            # # menambahkan nilai G ke dalam list
            features.append(np.mean(green))

            # # menambahkan nilai B ke dalam list
            features.append(np.mean(blue))

            # memasukkan list ke dalam file CSV dengan label tertentu
            writer.writerow([features[0], features[1], features[2], (a-1)])

# Menutup file CSV
csvfile.close()


# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/5_Label/RGB/RGB_Testing.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['R', 'G', 'B', 'label'])

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

            # # mengubah gambar ke dalam format RGB
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # # mengambil nilai red (R) dari gambar
            red = rgb[:, :, 0]

            # # mengambil nilai green (G) dari gambar
            green = rgb[:, :, 1]

            # # mengambil nilai blue (B) dari gambar
            blue = rgb[:, :, 2]

            # # membuat list untuk menyimpan hasil ekstraksi fitur
            features = []

            # # menambahkan nilai R ke dalam list
            features.append(np.mean(red))

            # # menambahkan nilai G ke dalam list
            features.append(np.mean(green))

            # # menambahkan nilai B ke dalam list
            features.append(np.mean(blue))

            # memasukkan list ke dalam file CSV dengan label tertentu
            writer.writerow([features[0], features[1], features[2], (b-1)])

# Menutup file CSV
csvfile.close()


# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/2_Label/RGB/RGB_Training.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['R', 'G', 'B', 'label'])

    c = 0

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/2_Label/DataSet_Training'):

        c = c+1
        # mengambil nama folder terakhir dari root
        label = root.split('\\')[-1]

        # mengambil semua file gambar di dalam folder
        image_files = [f for f in files if f.endswith('.jpg')]

        # melakukan ekstraksi fitur pada setiap gambar
        for image_file in image_files:
            # membaca gambar
            image = cv2.imread(os.path.join(root, image_file))

            # # mengubah gambar ke dalam format RGB
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # # mengambil nilai red (R) dari gambar
            red = rgb[:, :, 0]

            # # mengambil nilai green (G) dari gambar
            green = rgb[:, :, 1]

            # # mengambil nilai blue (B) dari gambar
            blue = rgb[:, :, 2]

            # # membuat list untuk menyimpan hasil ekstraksi fitur
            features = []

            # # menambahkan nilai R ke dalam list
            features.append(np.mean(red))

            # # menambahkan nilai G ke dalam list
            features.append(np.mean(green))

            # # menambahkan nilai B ke dalam list
            features.append(np.mean(blue))

            # memasukkan list ke dalam file CSV dengan label tertentu
            writer.writerow([features[0], features[1], features[2], (c-1)])

# Menutup file CSV
csvfile.close()


# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/cropped_ROI/2_Label/RGB/RGB_Testing.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['R', 'G', 'B', 'label'])

    d = 0

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/2_Label/DataSet_Testing'):

        d = d+1
        # mengambil nama folder terakhir dari root
        label = root.split('\\')[-1]

        # mengambil semua file gambar di dalam folder
        image_files = [f for f in files if f.endswith('.jpg')]

        # melakukan ekstraksi fitur pada setiap gambar
        for image_file in image_files:
            # membaca gambar
            image = cv2.imread(os.path.join(root, image_file))

            # # mengubah gambar ke dalam format RGB
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # # mengambil nilai red (R) dari gambar
            red = rgb[:, :, 0]

            # # mengambil nilai green (G) dari gambar
            green = rgb[:, :, 1]

            # # mengambil nilai blue (B) dari gambar
            blue = rgb[:, :, 2]

            # # membuat list untuk menyimpan hasil ekstraksi fitur
            features = []

            # # menambahkan nilai R ke dalam list
            features.append(np.mean(red))

            # # menambahkan nilai G ke dalam list
            features.append(np.mean(green))

            # # menambahkan nilai B ke dalam list
            features.append(np.mean(blue))

            # memasukkan list ke dalam file CSV dengan label tertentu
            writer.writerow([features[0], features[1], features[2], (d-1)])

# Menutup file CSV
csvfile.close()
