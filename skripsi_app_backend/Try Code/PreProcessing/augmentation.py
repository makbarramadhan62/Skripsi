import cv2
import numpy as np
from os import walk
from os.path import join

angles = [0, 45, 90, 135, 180, 225, 270, 315]

# membaca file
img = cv2.imread(
    "../../Code/Dataset/raw/2_label/dataset_training/sehat/daun_sehat (1).jpg")

# Membuat matriks transformasi rotasi
center = (img.shape[1] // 2, img.shape[0] // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

# Melakukan rotasi pada gambar menggunakan matriks transformasi
rotated_image = cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))

# Buat gambar putih dengan ukuran yang sama
white_image = np.ones_like(rotated_image) * 255

# Buat maska warna berdasarkan area hitam pada gambar yang dirotasi
gray_rotated = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(
    gray_rotated, 1, 255, cv2.THRESH_BINARY)

# Inversi maska warna
mask_inv = cv2.bitwise_not(mask)

# Ubah gambar putih menjadi gambar asli menggunakan maska
result = cv2.bitwise_and(white_image, rotated_image, mask=mask_inv)

# Gabungkan gambar asli dan gambar yang dirotasi menggunakan maska warna
result = cv2.bitwise_or(result, rotated_image, mask=mask)

normalized_image = cv2.normalize(
    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

resized_img = cv2.resize(img, (512, 512))
resized_rotasi = cv2.resize(normalized_image, (512, 512))

cv2.imshow("img", resized_img)
cv2.imshow("rotasi img", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
