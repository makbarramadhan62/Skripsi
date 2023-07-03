import cv2
import numpy as np

# Load image
img = cv2.imread('../../Code/API/uploads/image_2023_06_26_18_06_54.jpg')

# Konversi gambar ke skala abu-abu
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding pada gambar untuk memisahkan objek dari latar belakang
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
contours, _ = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = max(contours, key=cv2.contourArea)

# Dapatkan koordinat bounding box (kotak pembatas) dari kontur
x, y, w, h = cv2.boundingRect(cnt)

# Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
roi = img[y:y+h, x:x+w]

# Buat mask dengan ukuran yang sama dengan gambar dan inisialisasi dengan nilai 0 (hitam)
mask = np.zeros(img.shape[:2], np.uint8)

# Tentukan model latar belakang (background) dan objek (foreground)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Tentukan persegi panjang (rectangle) yang mencakup objek daun (ROI)
rect = (x, y, w, h)

# Algoritma GrabCut untuk menghapus latar belakang
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Buat mask dimana piksel non-nol menunjukkan objek (foreground) yang mungkin
mask2 = np.where((mask == cv2.GC_FGD) | (
    mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

# Balikkan mask ke negatif (putih menjadi hitam dan sebaliknya)
mask2_inv = cv2.bitwise_not(mask2)

# Buat hasil segmentasi dengan latar belakang putih
result = np.zeros_like(img)
result[np.where(mask2_inv == 255)] = (255, 255, 255)
result[np.where(mask2_inv == 0)] = img[np.where(mask2_inv == 0)]

# Menggambar kotak ROI pada hasil segmentasi
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Resize image
resized_img = cv2.resize(img, (576, 1024))
resized_result = cv2.resize(result, (512, 512))

# Tampilkan gambar asli, ROI, dan gambar hasil segmentasi
cv2.imshow('Original', resized_img)
# cv2.imshow('ROI', roi)
cv2.imshow('Result', resized_result)

# Crop gambar hasil segmentasi menggunakan ROI
cropped = result[y:y+h, x:x+w]
resized_cropped = cv2.resize(cropped, (512, 512))

cv2.imshow('Cropped', resized_cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()