import cv2
import numpy as np
import os
import csv

x = 0

# membuka file CSV untuk menyimpan hasil ekstraksi fitur
with open('../CSV/without_Background/5_label/RGB/RGB_Testing.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['R', 'G', 'B', 'label'])

    # melakukan ekstraksi fitur pada setiap folder
    for root, dirs, files in os.walk('../Dataset/without_Background/5_label/DataSet_Testing'):

        x = x+1
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
            writer.writerow([features[0], features[1], features[2], (x-1)])
