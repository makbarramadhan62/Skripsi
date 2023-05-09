from sklearn.metrics import accuracy_score, classification_report
from flask import Flask, request, jsonify
import cv2
import numpy as np
import pandas as pd
import joblib
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# membuat folder untuk menampung gambar yang di upload dari apps
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Load model
nb = joblib.load('../Model/NB_HSV.pkl')


def preprocess_and_extract_features(image):
    # Load image
    # image = cv2.imread(image_path)

    # Crop image menjadi kotak (1:1)
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

    # Convert image ke HSV
    hsv_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)

    # Perhitungan rata rata hsv
    h_mean = np.mean(hsv_image[:, :, 0])
    s_mean = np.mean(hsv_image[:, :, 1])
    v_mean = np.mean(hsv_image[:, :, 2])

    # Create feature array
    X = np.array([h_mean, s_mean, v_mean])

    return X


@app.route('/')
def home():
    return 'Welcome to API Grapesense!'


@app.route('/klasifikasi', methods=['POST'])
def classify():
    # Mendapatkan file dari request API
    image_file = request.files['image']

    # Membaca gambar dari file ke numpy array
    image = cv2.imdecode(np.fromstring(
        image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # Menyimpan gambar ke folder uploads
    filename = secure_filename(image_file.filename)
    image_file.save(os.path.join('uploads', filename))

    # Melakukan pre processing dan ekstraksi fitur
    X = preprocess_and_extract_features(image)

    # Mengubah bentuk array
    X_reshaped = X.reshape(1, -1)

    # Membuat dataframe menggunakan nama fitur
    feature_names = ['H', 'S', 'V']
    X_new = pd.DataFrame(data=X_reshaped, columns=feature_names)

    # Predict label
    y_pred = nb.predict(X_new)

    # Hasil
    result = int(y_pred[0])

    # Print label
    # print(f'Label: {y_pred[0]}')
    return jsonify({'Label': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
