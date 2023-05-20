import cv2
import numpy as np

# Load image
img = cv2.imread('../image.jpg')

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

# Buat mask dengan ukuran yang sama dengan gambar dan inisialisasi dengan nilai 0 (hitam)
mask = np.zeros(img.shape[:2], np.uint8)

# Tentukan model latar belakang (background) dan objek (foreground)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Tentukan persegi panjang (rectangle) yang mencakup objek daun (ROI)
rect = (x, y, w, h)

# algoritma GrabCut untuk menghapus latar belakang
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Buat mask dimana piksel non-nol menunjukkan objek (foreground) yang mungkin
mask2 = np.where((mask == cv2.GC_FGD) | (
    mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

# Terapkan mask pada gambar asli untuk menghapus latar belakang
result = cv2.bitwise_and(img, img, mask=mask2)

# Menggambar kotak ROI untuk di tampilkan
cv2.rectangle(result, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Tampilkan gambar asli, ROI, dan gambar hasil segmentasi
cv2.imshow('Original', img)
# cv2.imshow('ROI', roi)
cv2.imshow('Result', result)

# Crop gambar hasil segmentasi menggunakan ROI
cropped = result[y:y+h, x:x+w]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
