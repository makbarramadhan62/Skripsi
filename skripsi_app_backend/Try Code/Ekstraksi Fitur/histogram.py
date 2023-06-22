import cv2
import numpy as np

def calculate_histogram(image, bins):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # Konversi gambar ke ruang warna HSV
    h, s, v = cv2.split(hsv_image)  # Pisahkan channel H, S, dan V

    hist_h = cv2.calcHist([h], [0], None, [bins], [0, 256])  # Hitung histogram untuk channel H
    hist_s = cv2.calcHist([s], [0], None, [bins], [0, 256])  # Hitung histogram untuk channel S
    hist_v = cv2.calcHist([v], [0], None, [bins], [0, 256])  # Hitung histogram untuk channel V

    return hist_h, hist_s, hist_v

# Baca gambar
image = cv2.imread('../embun_bulu (12).jpg')

# Hitung histogram dengan ukuran bin 4
histogram_4 = calculate_histogram(image, 4)
print("Histogram dengan bin 4:")
print("Channel H:", histogram_4[0])
print("Channel S:", histogram_4[1])
print("Channel V:", histogram_4[2])

# Hitung histogram dengan ukuran bin 8
histogram_8 = calculate_histogram(image, 8)
print("Histogram dengan bin 8:")
print("Channel H:", histogram_8[0])
print("Channel S:", histogram_8[1])
print("Channel V:", histogram_8[2])

# Hitung histogram dengan ukuran bin 16
histogram_16 = calculate_histogram(image, 16)
print("Histogram dengan bin 16:")
print("Channel H:", histogram_16[0])
print("Channel S:", histogram_16[1])
print("Channel V:", histogram_16[2])