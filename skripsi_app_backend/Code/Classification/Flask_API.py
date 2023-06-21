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
nb = joblib.load('../Model/NB_Model_HSV_GLCM[all]3_5Label.pkl')


def preprocessing(image):

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

    # Resize image
    resized_image = cv2.resize(cropped_image, (1080, 1080))

    # # Konversi gambar ke skala abu-abu
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # # Thresholding thresholding pada gambar untuk memisahkan objek dari latar belakang
    # _, thresh = cv2.threshold(
    #     gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # # Temukan kontur pada gambar yang telah dithreshold dan dapatkan kontur terbesar yang diasumsikan sebagai objek daun
    # contours, _ = cv2.findContours(
    #     thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnt = max(contours, key=cv2.contourArea)

    # # Dapatkan koordinat bounding box (kotak pembatas) dari kontur
    # x, y, w, h = cv2.boundingRect(cnt)

    # # Dapatkan ROI (Region of Interest) menggunakan koordinat bounding box
    # roi = image[y:y+h, x:x+w]

    # # resize ROI hasil segmentasi
    # resized_image = cv2.resize(roi, (720, 720))

    return resized_image


def extract_features(image):

    # Convert image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # membuat list untuk menyimpan hasil ekstraksi fitur
    features = []

    # Perhitungan rata rata hsv
    mean_h, mean_s, mean_v = np.mean(hsv, axis=(0, 1))
    features.append(np.mean(mean_h))
    features.append(np.mean(mean_s))
    features.append(np.mean(mean_v))

    # Hitung matriks glcm
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    glcm = greycomatrix(image_gray, distances=[5], angles=[
                        0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)

    # Hitung fitur glcm
    glcm_properties = ['dissimilarity', 'homogeneity', 'contrast']
    glcm_props = [
        propery for name in glcm_properties for propery in greycoprops(glcm, name)[0]]
    for item in glcm_props:
        features.append(item)

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
    preprocessed = preprocessing(image)
    X = extract_features(preprocessed)

    # Mengubah bentuk array
    # X_reshaped = X.reshape(1, -1)
    X_reshaped = np.reshape(X, (1, -1))

    # Membuat dataframe menggunakan nama fitur
    glcm_properties = ['dissimilarity', 'homogeneity', 'contrast']
    angles = [0, 45, 90, 135]
    feature_names = ['H', 'S', 'V'] + \
        [f'{prop} {angle}' for prop in glcm_properties for angle in angles]

    X_new = pd.DataFrame(data=X_reshaped, columns=feature_names)

    # Predict label
    y_pred = nb.predict(X_new)

    result = int(y_pred[0])

    # Print label
    print(f'Label: {result}')
    return jsonify({'Label': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
