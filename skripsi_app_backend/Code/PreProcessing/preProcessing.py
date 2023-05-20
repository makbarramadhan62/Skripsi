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
for root, dirs, files in walk("../Dataset/with_Background/2_Label/DataSet_Training/Sehat"):
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

            # Buat mask dengan ukuran yang sama dengan gambar dan inisialisasi dengan nilai 0 (hitam)
            mask = np.zeros(img.shape[:2], np.uint8)

            # Tentukan model latar belakang (background) dan objek (foreground)
            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            # Tentukan persegi panjang (rectangle) yang mencakup objek daun (ROI)
            rect = (x, y, w, h)

            # algoritma GrabCut untuk menghapus latar belakang
            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            # Buat mask dimana piksel non-nol menunjukkan objek (foreground) yang mungkin
            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            # Terapkan mask pada gambar asli untuk menghapus latar belakang
            result = cv2.bitwise_and(img, img, mask=mask2)

            # Crop gambar hasil segmentasi menggunakan ROI
            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/2_Label/DataSet_Training/Sehat/" +
                        "Data ke-" + str(a)+".jpg", cropped)

            print("DataSet_Training/Sehat/Data ke-" + str(a)+".jpg")

for root, dirs, files in walk("../Dataset/with_Background/2_Label/DataSet_Training/Tidak_Sehat"):
    if files:
        for file in files:
            b = b+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/2_Label/DataSet_Training/Tidak_Sehat/" +
                        "Data ke-" + str(b)+".jpg", cropped)

            print("DataSet_Training/Tidak_Sehat/Data ke-" + str(b)+".jpg")


for root, dirs, files in walk("../Dataset/with_Background/2_Label/DataSet_Testing/Sehat"):
    if files:
        for file in files:
            c = c+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/2_Label/DataSet_Testing/Sehat/" +
                        "Data ke-" + str(c)+".jpg", cropped)

            print("DataSet_Testing/Sehat/Data ke-" + str(c)+".jpg")


for root, dirs, files in walk("../Dataset/with_Background/2_Label/DataSet_Testing/Tidak_Sehat"):
    if files:
        for file in files:
            d = d+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/2_Label/DataSet_Testing/Tidak_Sehat/" +
                        "Data ke-" + str(d)+".jpg", cropped)

            print("DataSet_Testing/Tidak_Sehat/Data ke-" + str(d)+".jpg")


for root, dirs, files in walk("../Dataset/with_Background/5_Label/DataSet_Training/bercak_daun"):
    if files:
        for file in files:
            e = e+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/5_Label/DataSet_Training/bercak_daun/" +
                        "Data ke-" + str(e)+".jpg", cropped)

            print("DataSet_Training/bercak_daun/Data ke-" + str(e)+".jpg")


for root, dirs, files in walk("../Dataset/with_Background/5_Label/DataSet_Training/bercak_merah"):
    if files:
        for file in files:
            f = f+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/5_Label/DataSet_Training/bercak_merah/" +
                        "Data ke-" + str(f)+".jpg", cropped)

            print("DataSet_Training/bercak_merah/Data ke-" +
                  str(f)+".jpg")


for root, dirs, files in walk("../Dataset/with_Background/5_Label/DataSet_Training/daun_sehat"):
    if files:
        for file in files:
            g = g+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/5_Label/DataSet_Training/daun_sehat/" +
                        "Data ke-" + str(g)+".jpg", cropped)

            print("DataSet_Training/daun_sehat/Data ke-" +
                  str(g)+".jpg")


for root, dirs, files in walk("../Dataset/with_Background/5_Label/DataSet_Training/embun_bulu"):
    if files:
        for file in files:
            p = p+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/5_Label/DataSet_Training/Embun_Bulu/" +
                        "Data ke-" + str(p)+".jpg", cropped)

            print("DataSet_Training/embun_bulu/Data ke-" +
                  str(p)+".jpg")

for root, dirs, files in walk("../Dataset/with_Background/5_Label/DataSet_Training/hama_tungau"):
    if files:
        for file in files:
            i = i+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/5_Label/DataSet_Training/hama_tungau/" +
                        "Data ke-" + str(i)+".jpg", cropped)

            print("DataSet_Training/hama_tungau/Data ke-" +
                  str(i)+".jpg")

for root, dirs, files in walk("../Dataset/with_Background/5_Label/Dataset_Testing/bercak_daun"):
    if files:
        for file in files:
            j = j+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/5_Label/Dataset_Testing/bercak_daun/" +
                        "Data ke-" + str(j)+".jpg", cropped)

            print("Dataset_Testing/bercak_daun/Data ke-" +
                  str(j)+".jpg")

for root, dirs, files in walk("../Dataset/with_Background/5_Label/Dataset_Testing/bercak_merah"):
    if files:
        for file in files:
            k = k+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/5_Label/Dataset_Testing/bercak_merah/" +
                        "Data ke-" + str(k)+".jpg", cropped)

            print("Dataset_Testing/bercak_merah/Data ke-" +
                  str(k)+".jpg")

for root, dirs, files in walk("../Dataset/with_Background/5_Label/Dataset_Testing/daun_sehat"):
    if files:
        for file in files:
            l = l+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/5_Label/Dataset_Testing/daun_sehat/" +
                        "Data ke-" + str(l)+".jpg", cropped)

            print("Dataset_Testing/daun_sehat/Data ke-" +
                  str(l)+".jpg")

for root, dirs, files in walk("../Dataset/with_Background/5_Label/Dataset_Testing/embun_bulu"):
    if files:
        for file in files:
            m = m+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/5_Label/Dataset_Testing/embun_bulu/" +
                        "Data ke-" + str(m)+".jpg", cropped)

            print("Dataset_Testing/embun_bulu/Data ke-" +
                  str(m)+".jpg")

for root, dirs, files in walk("../Dataset/with_Background/5_Label/Dataset_Testing/hama_tungau"):
    if files:
        for file in files:
            n = n+1

            img = cv2.imread(join(root, file))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(cnt)

            roi = img[y:y+h, x:x+w]

            mask = np.zeros(img.shape[:2], np.uint8)

            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)

            rect = (x, y, w, h)

            cv2.grabCut(img, mask, rect, bgdModel,
                        fgdModel, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == cv2.GC_FGD) | (
                mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

            result = cv2.bitwise_and(img, img, mask=mask2)

            cropped = result[y:y+h, x:x+w]

            cv2.imwrite("../Dataset/without_Background/5_Label/Dataset_Testing/hama_tungau/" +
                        "Data ke-" + str(n)+".jpg", cropped)

            print("Dataset_Testing/hama_tungau/Data ke-" +
                  str(n)+".jpg")
