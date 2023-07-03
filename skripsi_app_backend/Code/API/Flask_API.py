import os
import cv2
import joblib
import numpy as np
import pandas as pd
from sklearn import preprocessing
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from skimage.feature import graycomatrix, graycoprops


app = Flask(__name__)

# membuat folder untuk menampung gambar yang di upload dari apps
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Load model
nb = joblib.load(
    '../Model/NB_RGB[Hist-16]_GLCM[S4-D5]_160_ROI_WithoutNormalize.pkl')


def preprocessing_image(image):

    # Crop image to square
    height, width, channels = image.shape
    if height > width:
        crop_size = width
        y = int((height - width) / 2)
        x = 0
    else:
        crop_size = height
        x = int((width - height) / 2)
        y = 0
    cropped_image = image[y:y+crop_size, x:x+crop_size]

    # Konversi gambar ke skala abu-abu
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Thresholding pada gambar untuk memisahkan objek dari latar belakang
    _, thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=cv2.contourArea)

    # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
    x, y, w, h = cv2.boundingRect(cnt)

    # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
    roi = image[y:y+h, x:x+w]

    # Buat mask dengan ukuran yang sama dengan gambar dan inisialisasi dengan nilai 0 (hitam)
    mask = np.zeros(image.shape[:2], np.uint8)

    # Tentukan model latar belakang (background) dan objek (foreground)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # Tentukan persegi panjang (rectangle) yang mencakup objek daun (ROI)
    rect = (x, y, w, h)

    # Algoritma GrabCut untuk menghapus latar belakang
    cv2.grabCut(image, mask, rect, bgdModel,
                fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    # Buat mask dimana piksel non-nol menunjukkan objek (foreground) yang mungkin
    mask2 = np.where((mask == cv2.GC_FGD) | (
        mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

    # Balikkan mask ke negatif (putih menjadi hitam dan sebaliknya)
    mask2_inv = cv2.bitwise_not(mask2)

    # Buat hasil segmentasi dengan latar belakang putih
    result = np.zeros_like(image)
    result[np.where(mask2_inv == 255)] = (255, 255, 255)
    result[np.where(mask2_inv == 0)] = image[np.where(mask2_inv == 0)]

    # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
    roi = result[y:y+h, x:x+w]

    normalized_image = cv2.normalize(
        roi, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # resize ROI hasil segmentasi
    resized_image = cv2.resize(normalized_image, (1080, 1080))

    # cv2.imshow("Image", image)
    # cv2.imshow("Cropped Image", resized_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return resized_image


def extract_features(image):

    # Konversi gambar ke ruang warna rgb
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    r, g, b = cv2.split(rgb_image)  # Pisahkan channel R, G, dan B

    # histogram property
    bins = 16

    # Hitung histogram untuk channel H
    hist_r = cv2.calcHist([r], [0], None, [bins], [0, 256])
    # Mengubah histogram R menjadi array 1 dimensi
    hist_r = np.ravel(hist_r)

    # Hitung histogram untuk channel S
    hist_g = cv2.calcHist([g], [0], None, [bins], [0, 256])
    # Mengubah histogram G menjadi array 1 dimensi
    hist_g = np.ravel(hist_g)

    # Hitung histogram untuk channel V
    hist_b = cv2.calcHist([b], [0], None, [bins], [0, 256])
    # Mengubah histogram B menjadi array 1 dimensi
    hist_b = np.ravel(hist_b)

    # scenario GLCM properties
    glcm_properties = ['dissimilarity',
                       'correlation', 'homogeneity', 'contrast']
    distance = [5]

    # Hitung matriks glcm
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    glcm = graycomatrix(image_gray, distances=distance, angles=[
                        0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)

    # Hitung fitur glcm
    feature_glcm = []
    glcm_props = [
        propery for name in glcm_properties for propery in graycoprops(glcm, name)[0]]
    for item in glcm_props:
        feature_glcm.append(item)

    # menambahkan semua fitur ke list
    features = []
    features.append([*hist_r, *hist_g, *hist_b] + feature_glcm)

    return features


@app.route('/')
def home():
    return 'Welcome to API Grapesense!'


@app.route('/klasifikasi', methods=['POST'])
def classify():
    # Mendapatkan file dari request API
    image_file = request.files['image']

    # Menyimpan gambar ke folder uploads
    filename = secure_filename(image_file.filename)
    image_path = os.path.join('uploads', filename)
    image_file.save(image_path)

    image = cv2.imread(image_path)

    # Melakukan pre processing dan ekstraksi fitur
    preprocessed = preprocessing_image(image)
    X = extract_features(preprocessed)

    # Mengubah bentuk array
    # X_reshaped = X.reshape(1, -1)
    X_reshaped = np.reshape(X, (1, -1))

    # inisialisasi atribut fitur untuk dataframe
    glcm_properties = ['dissimilarity',
                       'correlation', 'homogeneity', 'contrast']
    angles = [0, 45, 90, 135]
    bins = 16

    # Membuat dataframe menggunakan nama fitur
    feature_names = ['hist_r' + str(i+1) for i in range(bins)] + ['hist_g' + str(i+1) for i in range(bins)] + [
        'hist_b' + str(i+1) for i in range(bins)] + [f'{prop} {angle}' for prop in glcm_properties for angle in angles]

    X = pd.DataFrame(data=X_reshaped, columns=feature_names)

    normalization_data = preprocessing.normalize(X, norm="l2")

    # Predict label
    y_pred = nb.predict(normalization_data)

    result = int(y_pred[0])

    # Print label
    print(f'Label: {result}')
    return jsonify({'Label': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
