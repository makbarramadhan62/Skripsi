from flask import Flask, request, jsonify
import cv2
import numpy as np
import pandas as pd
import joblib
import os
from werkzeug.utils import secure_filename
from skimage.feature import greycomatrix, greycoprops


app = Flask(__name__)

# membuat folder untuk menampung gambar yang di upload dari apps
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Load model
nb = joblib.load('../Model/NB_Model_HSV_GLCM[0]4_5Label.pkl')


def preprocessing_extract_features(image):

    # Konversi gambar ke skala abu-abu
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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
    roi = image[y:y+h, x:x+w]

    # resize ROI hasil segmentasi
    resized_image = cv2.resize(roi, (720, 720))

    # Convert image to HSV
    hsv = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)

    # Perhitungan rata rata hsv
    mean_h, mean_s, mean_v = np.mean(hsv, axis=(0, 1))

    # Hitung matriks glcm
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    glcm = greycomatrix(image_gray, [5], [0],
                        levels=256, symmetric=True, normed=True)

    # Hitung fitur glcm
    correlation = greycoprops(glcm, 'correlation')[0][0]
    homogeneity = greycoprops(glcm, 'homogeneity')[0][0]
    contrast = greycoprops(glcm, 'contrast')[0][0]

    # Create feature array
    X = np.array([mean_h, mean_s, mean_v, correlation, homogeneity, contrast])

    return X


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

    # Membaca gambar dari file ke numpy array
    # image = cv2.imdecode(np.fromstring(
    #     image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    image = cv2.imread(image_path)

    # Melakukan pre processing dan ekstraksi fitur
    X = preprocessing_extract_features(image)

    # Mengubah bentuk array
    X_reshaped = X.reshape(1, -1)

    # Membuat dataframe menggunakan nama fitur
    feature_names = ['H', 'S', 'V', 'correlation', 'homogeneity', 'contrast']

    X_new = pd.DataFrame(data=X_reshaped, columns=feature_names)

    # Predict label
    y_pred = nb.predict(X_new)

    # Print label
    print(f'Label: {y_pred[0]}')

    # Hasil
    result = int(y_pred[0])

    # Print label
    # print(f'Label: {y_pred[0]}')
    return jsonify({'Label': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
