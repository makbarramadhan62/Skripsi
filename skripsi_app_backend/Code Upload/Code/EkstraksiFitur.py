import cv2
import numpy as np

# membaca gambar
image = cv2.imread()

# mengubah gambar ke dalam format HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# mengambil nilai hue (H) dari gambar
hue = hsv[:, :, 0]

# mengambil nilai saturation (S) dari gambar
saturation = hsv[:, :, 1]

# mengambil nilai value (V) dari gambar
value = hsv[:, :, 2]

# membuat list untuk menyimpan hasil ekstraksi fitur
features = []

# menambahkan nilai H ke dalam list
features.append(np.mean(hue))

# menambahkan nilai S ke dalam list
features.append(np.mean(saturation))

# menambahkan nilai V ke dalam list
features.append(np.mean(value))
