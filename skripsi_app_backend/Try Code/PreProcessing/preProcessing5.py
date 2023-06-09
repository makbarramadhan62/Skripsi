import cv2
import numpy as np

# Load image
img = cv2.imread(
    '../../Code/Dataset/Raw/2_Label/DataSet_Training/Sehat/daun_sehat (10).jpg')

# Konversi gambar ke skala abu-abu
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
contours, _ = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = max(contours, key=cv2.contourArea)

# Dapatkan koordinat bounding box (kotak pembatas) dari kontur
x, y, w, h = cv2.boundingRect(cnt)

# Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
roi = img[y:y+h, x:x+w]

# Menggambar kotak ROI untuk di tampilkan
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 10)

# Resize image
resized_img = cv2.resize(img, (720, 720))

# Tampilkan gambar asli, ROI, dan gambar hasil segmentasi
cv2.imshow('Original', resized_img)

resized_roi = cv2.resize(roi, (720, 720))
cv2.imshow('ROI', resized_roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
