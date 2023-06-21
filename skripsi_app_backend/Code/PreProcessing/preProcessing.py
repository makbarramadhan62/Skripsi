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
g = 0
p = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0

# melakukan perulangan pada folder
for root, dirs, files in walk("../Dataset/augmentation_image/2_Label/DataSet_Training/Sehat"):
    # validasi apakah terdapat file pada folder
    if files:
        # perulangan pada masing masing file untuk melakukan preprocessing
        for file in files:
            a = a+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/2_Label/DataSet_Training/Sehat/" +
                        "Data ke-" + str(a)+".jpg", resized_roi)

            print("DataSet_Training/Sehat/Data ke-" + str(a)+".jpg")

for root, dirs, files in walk("../Dataset/augmentation_image/2_Label/DataSet_Training/Tidak_Sehat"):
    if files:
        for file in files:
            b = b+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/2_Label/DataSet_Training/Tidak_Sehat/" +
                        "Data ke-" + str(b)+".jpg", resized_roi)

            print("DataSet_Training/Tidak_Sehat/Data ke-" + str(b)+".jpg")


for root, dirs, files in walk("../Dataset/augmentation_image/2_Label/DataSet_Testing/Sehat"):
    if files:
        for file in files:
            c = c+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/2_Label/DataSet_Testing/Sehat/" +
                        "Data ke-" + str(c)+".jpg", resized_roi)

            print("DataSet_Testing/Sehat/Data ke-" + str(c)+".jpg")


for root, dirs, files in walk("../Dataset/augmentation_image/2_Label/DataSet_Testing/Tidak_Sehat"):
    if files:
        for file in files:
            d = d+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/2_Label/DataSet_Testing/Tidak_Sehat/" +
                        "Data ke-" + str(d)+".jpg", resized_roi)

            print("DataSet_Testing/Tidak_Sehat/Data ke-" + str(d)+".jpg")


for root, dirs, files in walk("../Dataset/augmentation_image/5_Label/DataSet_Training/bercak_daun"):
    if files:
        for file in files:
            e = e+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/5_Label/DataSet_Training/bercak_daun/" +
                        "Data ke-" + str(e)+".jpg", resized_roi)

            print("DataSet_Training/bercak_daun/Data ke-" + str(e)+".jpg")


for root, dirs, files in walk("../Dataset/augmentation_image/5_Label/DataSet_Training/bercak_merah"):
    if files:
        for file in files:
            f = f+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/5_Label/DataSet_Training/bercak_merah/" +
                        "Data ke-" + str(f)+".jpg", resized_roi)

            print("DataSet_Training/bercak_merah/Data ke-" +
                  str(f)+".jpg")


for root, dirs, files in walk("../Dataset/augmentation_image/5_Label/DataSet_Training/daun_sehat"):
    if files:
        for file in files:
            g = g+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/5_Label/DataSet_Training/daun_sehat/" +
                        "Data ke-" + str(g)+".jpg", resized_roi)

            print("DataSet_Training/daun_sehat/Data ke-" +
                  str(g)+".jpg")


for root, dirs, files in walk("../Dataset/augmentation_image/5_Label/DataSet_Training/embun_tepung_palsu"):
    if files:
        for file in files:
            p = p+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/5_Label/DataSet_Training/embun_tepung_palsu/" +
                        "Data ke-" + str(p)+".jpg", resized_roi)

            print("DataSet_Training/embun_tepung_palsu/Data ke-" +
                  str(p)+".jpg")

for root, dirs, files in walk("../Dataset/augmentation_image/5_Label/DataSet_Training/hama_tungau_merah"):
    if files:
        for file in files:
            i = i+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/5_Label/DataSet_Training/hama_tungau_merah/" +
                        "Data ke-" + str(i)+".jpg", resized_roi)

            print("DataSet_Training/hama_tungau_merah/Data ke-" +
                  str(i)+".jpg")

for root, dirs, files in walk("../Dataset/augmentation_image/5_Label/Dataset_Testing/bercak_daun"):
    if files:
        for file in files:
            j = j+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/5_Label/Dataset_Testing/bercak_daun/" +
                        "Data ke-" + str(j)+".jpg", resized_roi)

            print("Dataset_Testing/bercak_daun/Data ke-" +
                  str(j)+".jpg")

for root, dirs, files in walk("../Dataset/augmentation_image/5_Label/Dataset_Testing/bercak_merah"):
    if files:
        for file in files:
            k = k+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/5_Label/Dataset_Testing/bercak_merah/" +
                        "Data ke-" + str(k)+".jpg", resized_roi)

            print("Dataset_Testing/bercak_merah/Data ke-" +
                  str(k)+".jpg")

for root, dirs, files in walk("../Dataset/augmentation_image/5_Label/Dataset_Testing/daun_sehat"):
    if files:
        for file in files:
            l = l+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/5_Label/Dataset_Testing/daun_sehat/" +
                        "Data ke-" + str(l)+".jpg", resized_roi)

            print("Dataset_Testing/daun_sehat/Data ke-" +
                  str(l)+".jpg")

for root, dirs, files in walk("../Dataset/augmentation_image/5_Label/Dataset_Testing/embun_tepung_palsu"):
    if files:
        for file in files:
            m = m+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/5_Label/Dataset_Testing/embun_tepung_palsu/" +
                        "Data ke-" + str(m)+".jpg", resized_roi)

            print("Dataset_Testing/embun_tepung_palsu/Data ke-" +
                  str(m)+".jpg")

for root, dirs, files in walk("../Dataset/augmentation_image/5_Label/Dataset_Testing/hama_tungau_merah"):
    if files:
        for file in files:
            n = n+1

            # membaca file
            img = cv2.imread(join(root, file))

            # Konversi gambar ke skala abu-abu
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
            x, y, w, h = cv2.boundingRect(cnt)

            # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
            roi = img[y:y+h, x:x+w]

            resized_roi = cv2.resize(roi, (1080, 1080))

            cv2.imwrite("../Dataset/preprocessed_roi_augmentation/5_Label/Dataset_Testing/hama_tungau_merah/" +
                        "Data ke-" + str(n)+".jpg", resized_roi)

            print("Dataset_Testing/hama_tungau_merah/Data ke-" +
                  str(n)+".jpg")
