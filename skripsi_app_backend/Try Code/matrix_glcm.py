import cv2
import numpy as np
from skimage import feature

# Membaca gambar
image = cv2.imread(
    '../Code/Dataset/PreProcessed/5_Label/DataSet_Training/bercak_merah/Data ke-13.jpg', cv2.IMREAD_GRAYSCALE)

# Menghitung matriks GLCM
glcm = feature.greycomatrix(image, distances=[5], angles=[
                            0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256)

# Mereduksi matriks GLCM menjadi ordo 3x3
reduced_glcm = np.sum(glcm, axis=(2, 3))

# Menampilkan matriks GLCM
print(reduced_glcm)