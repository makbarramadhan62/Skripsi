import cv2
from os import walk
from os.path import join

# a = 0

# for root, dirs, files in walk("../Bercak_Merah"):
#     if files:
#         for file in files:
#             a = a+1

#             # membaca file
#             img = cv2.imread(join(root, file))

#             # # Konversi gambar ke skala abu-abu
#             # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#             # # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
#             # _, thresh = cv2.threshold(
#             #     gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#             # # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
#             # contours, _ = cv2.findContours(
#             #     thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#             # cnt = max(contours, key=cv2.contourArea)

#             # # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
#             # x, y, w, h = cv2.boundingRect(cnt)

#             # # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
#             # roi = img[y:y+h, x:x+w]

#             # resized_roi = cv2.resize(roi, (1080, 1080))

#             # Normalisasi citra
#             normalized_image = cv2.normalize(
#                 img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

#             cv2.imwrite("../Bercak_Merah/" +
#                         "bercak_merah_" + str(a)+".jpg", normalized_image)

#             print("DataSet_Training/bercak_merah/Data ke-" +
#                   str(a)+".jpg")


img = cv2.imread("../Bercak_Merah/bercak_merah (30).jpg")
img2 = cv2.imread("../Bercak_Merah/bercak_merah (31).jpg")
normalized_image = cv2.normalize(
    img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
normalized_image2 = cv2.normalize(
    img2, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

resized_img = cv2.resize(img, (512, 512))
resized_img2 = cv2.resize(img2, (512, 512))
resized_normalisasi = cv2.resize(normalized_image, (512, 512))
resized_normalisasi2 = cv2.resize(normalized_image2, (512, 512))

cv2.imshow('img', resized_img)
cv2.imshow('img2', resized_img2)
cv2.imshow('normalisasi', resized_normalisasi)
cv2.imshow('normalisasi2', resized_normalisasi2)

cv2.waitKey(0)
cv2.destroyAllWindows()
