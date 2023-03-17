from skimage.feature import greycomatrix, greycoprops
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Baca gambar
image = cv2.imread('image.jpg')

# Ubah skala warna menjadi HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Split kanal-kanal warna
h, s, v = cv2.split(hsv)

# Hitung histogram untuk setiap kanal
hist_h = cv2.calcHist([h], [0], None, [180], [0, 180])
hist_s = cv2.calcHist([s], [0], None, [256], [0, 256])
hist_v = cv2.calcHist([v], [0], None, [256], [0, 256])

# Buat plot histogram
plt.figure()
plt.title("Histogram HSV")
plt.xlabel("Bin")
plt.ylabel("Jumlah")
plt.plot(hist_h, color='r')
plt.plot(hist_s, color='g')
plt.plot(hist_v, color='b')
plt.show()

# -----------------------------------------------------------------

# import cv2
# import numpy as np

# # Membaca gambar
# image = cv2.imread('image.jpg')

# # Mengubah gambar ke dalam spasi warna HSV
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# lower_color = np.array([40, 30, 0])  # Nilai H, S, dan V untuk batas bawah
# upper_color = np.array([80, 255, 255])  # Nilai H, S, dan V untuk batas atas

# # Membuat mask dengan menggunakan batas warna di atas
# mask = cv2.inRange(hsv, lower_color, upper_color)

# # Melakukan proses masking dengan menggunakan mask yang telah dibuat
# result = cv2.bitwise_and(image, image, mask=mask)

# # Menampilkan hasil proses masking
# cv2.imshow('image', image)
# cv2.imshow('mask', mask)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ----------------------------------------------------------------

# import cv2
# import numpy as np
# from skimage.feature import greycomatrix, greycoprops, hog

# # Baca gambar daun
# image = cv2.imread('image.jpg')

# # Ubah gambar ke skala keabuan
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Ekstraksi fitur tekstur menggunakan glcm
# # Hitung matriks glcm
# glcm = greycomatrix(image_gray, [5], [0],
#                     levels=256, symmetric=True, normed=True)

# # Hitung fitur glcm
# contrast = greycoprops(glcm, 'contrast')
# homogeneity = greycoprops(glcm, 'homogeneity')
# energy = greycoprops(glcm, 'energy')

# # Ekstraksi fitur tekstur menggunakan HOG
# # Hitung histogram orientasi gradient
# fd, hog_image = hog(image_gray, orientations=8, pixels_per_cell=(
#     16, 16), cells_per_block=(1, 1), visualize=True)

# print('Fitur glcm:')
# print('Nilai contrast:', contrast)
# print('Nilai homogenitas:', homogeneity)
# print('Nilai energy:', energy)

# print('Fitur HOG:')
# print(fd)

# # Tampilkan gambar daun dan gambar HOG
# cv2.imshow('Gambar daun', image)
# cv2.imshow('Gambar HOG', hog_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ----------------------------------------------------------------

# import cv2

# Baca gambar daun
# image = cv2.imread('image.jpg')

# # Ubah gambar ke spasi warna RGB
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Hitung nilai rata-rata intensitas merah, hijau, dan biru
# mean_r, mean_g, mean_b = np.mean(image_rgb, axis=(0, 1))

# # Hitung matriks glcm
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# glcm = greycomatrix(image_gray, [5], [0],
#                     levels=256, symmetric=True, normed=True)

# # Hitung fitur glcm
# contrast = greycoprops(glcm, 'contrast')
# dissimilarity = greycoprops(glcm, 'dissimilarity')
# homogeneity = greycoprops(glcm, 'homogeneity')
# energy = greycoprops(glcm, 'energy')
# correlation = greycoprops(glcm, 'correlation')

# # Tambahkan fitur warna ke dalam fitur tekstur
# features = [mean_r, mean_g, mean_b, contrast, homogeneity, energy]

# print('Fitur tekstur dan warna daun:')
# print(features)
