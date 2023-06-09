import cv2
import numpy as np
import os
import csv

x = 0

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/5_Label/HSV/HSV_Testing.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['H', 'S', 'V', 'label'])

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/PreProcessed/5_Label/DataSet_Testing'):

        x = x+1
        # mengambil nama folder terakhir dari root
        label = root.split('\\')[-1]

        # mengambil semua file gambar di dalam folder
        image_files = [f for f in files if f.endswith('.jpg')]

        # melakukan ekstraksi fitur pada setiap gambar
        for image_file in image_files:
            # membaca gambar
            image = cv2.imread(os.path.join(root, image_file))

            # mengubah gambar ke dalam format HSV
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            # mengambil nilai hue (H) dari gambar
            hue = hsv[:, :, 0]

            # mengambil nilai saturation (S) dari gambar
            saturation = hsv[:, :, 1]

            # mengambil nilai value (V) dari gambar
            value = hsv[:, :, 2]

            # membuat list untuk menyimpan hasil ekstraksi fitur
            features = []

            # menambahkan nilai H ke dalam list
            features.append(np.mean(hue))

            # menambahkan nilai S ke dalam list
            features.append(np.mean(saturation))

            # menambahkan nilai V ke dalam list
            features.append(np.mean(value))

            # memasukkan list ke dalam file CSV dengan label tertentu
            writer.writerow([features[0], features[1], features[2], (x-1)])
