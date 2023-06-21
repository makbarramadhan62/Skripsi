import cv2
from os import walk
from os.path import join

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

angles = [0, 45, 90, 180, 270]

for root, dirs, files in walk("../Dataset/raw/2_label/dataset_training/sehat"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                a = a+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/2_label/dataset_training/sehat/" +
                            "Data ke-" + str(a)+".jpg", normalized_image)
                print("2_label/dataset_training/sehat/" +
                      "Data ke-" + str(a)+".jpg")

for root, dirs, files in walk("../Dataset/raw/2_label/dataset_training/tidak_sehat"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                b = b+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/2_label/dataset_training/tidak_sehat/" +
                            "Data ke-" + str(b)+".jpg", normalized_image)

                print("dataset_training/tidak_sehat/Data ke-" + str(b)+".jpg")


for root, dirs, files in walk("../Dataset/raw/2_label/dataset_testing/sehat"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                c = c+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/2_label/dataset_testing/sehat/" +
                            "Data ke-" + str(c)+".jpg", normalized_image)

                print("dataset_testing/sehat/Data ke-" + str(c)+".jpg")


for root, dirs, files in walk("../Dataset/raw/2_label/dataset_testing/tidak_sehat"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                d = d+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/2_label/dataset_testing/tidak_sehat/" +
                            "Data ke-" + str(d)+".jpg", normalized_image)

                print("dataset_testing/tidak_sehat/Data ke-" + str(d)+".jpg")


for root, dirs, files in walk("../Dataset/raw/5_label/dataset_training/bercak_daun"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                e = e+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/5_label/dataset_training/bercak_daun/" +
                            "Data ke-" + str(e)+".jpg", normalized_image)

                print("dataset_training/bercak_daun/Data ke-" + str(e)+".jpg")


for root, dirs, files in walk("../Dataset/raw/5_label/dataset_training/bercak_merah"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                f = f+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/5_label/dataset_training/bercak_merah/" +
                            "Data ke-" + str(f)+".jpg", normalized_image)

                print("dataset_training/bercak_merah/Data ke-" +
                      str(f)+".jpg")


for root, dirs, files in walk("../Dataset/raw/5_label/dataset_training/daun_sehat"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                g = g+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/5_label/dataset_training/daun_sehat/" +
                            "Data ke-" + str(g)+".jpg", normalized_image)

                print("dataset_training/daun_sehat/Data ke-" +
                      str(g)+".jpg")


for root, dirs, files in walk("../Dataset/raw/5_label/dataset_training/embun_tepung_palsu"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                p = p+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/5_label/dataset_training/embun_tepung_palsu/" +
                            "Data ke-" + str(p)+".jpg", normalized_image)

                print("dataset_training/embun_tepung_palsu/Data ke-" +
                      str(p)+".jpg")

for root, dirs, files in walk("../Dataset/raw/5_label/dataset_training/hama_tungau_merah"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                i = i+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/5_label/dataset_training/hama_tungau_merah/" +
                            "Data ke-" + str(i)+".jpg", normalized_image)

                print("dataset_training/hama_tungau_merah/Data ke-" +
                      str(i)+".jpg")

for root, dirs, files in walk("../Dataset/raw/5_label/dataset_testing/bercak_daun"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                j = j+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/5_label/dataset_testing/bercak_daun/" +
                            "Data ke-" + str(j)+".jpg", normalized_image)

                print("dataset_testing/bercak_daun/Data ke-" +
                      str(j)+".jpg")

for root, dirs, files in walk("../Dataset/raw/5_label/dataset_testing/bercak_merah"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                k = k+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/5_label/dataset_testing/bercak_merah/" +
                            "Data ke-" + str(k)+".jpg", normalized_image)

                print("dataset_testing/bercak_merah/Data ke-" +
                      str(k)+".jpg")

for root, dirs, files in walk("../Dataset/raw/5_label/dataset_testing/daun_sehat"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                l = l+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/5_label/dataset_testing/daun_sehat/" +
                            "Data ke-" + str(l)+".jpg", normalized_image)

                print("dataset_testing/daun_sehat/Data ke-" +
                      str(l)+".jpg")

for root, dirs, files in walk("../Dataset/raw/5_label/dataset_testing/embun_tepung_palsu"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                m = m+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/5_label/dataset_testing/embun_tepung_palsu/" +
                            "Data ke-" + str(m)+".jpg", normalized_image)

                print("dataset_testing/embun_tepung_palsu/Data ke-" +
                      str(m)+".jpg")

for root, dirs, files in walk("../Dataset/raw/5_label/dataset_testing/hama_tungau_merah"):
    if files:
        for file in files:
            # membaca file
            img = cv2.imread(join(root, file))
            for angle in angles:
                # Membuat matriks transformasi rotasi
                center = (img.shape[1] // 2, img.shape[0] // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

                n = n+1

                # Melakukan rotasi pada gambar menggunakan matriks transformasi
                rotated_image = cv2.warpAffine(
                    img, matrix, (img.shape[1], img.shape[0]))
                normalized_image = cv2.normalize(
                    rotated_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                cv2.imwrite("../Dataset/augmentation_image/5_label/dataset_testing/hama_tungau_merah/" +
                            "Data ke-" + str(n)+".jpg", normalized_image)

                print("dataset_testing/hama_tungau_merah/Data ke-" +
                      str(n)+".jpg")
