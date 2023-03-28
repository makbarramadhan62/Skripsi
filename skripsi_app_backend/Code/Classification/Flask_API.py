from sklearn.metrics import accuracy_score, classification_report
from flask import Flask, request, jsonify
import cv2
import numpy as np
import pandas as pd
import joblib
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# create temporary folder for image uploads
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Load pre-trained model
nb = joblib.load('../Model/NaiveBayes3.pkl')

# Define function for preprocessing and feature extraction


def preprocess_and_extract_features(image):
    # Load image
    # image = cv2.imread(image_path)

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

    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)

    # Compute mean of HSV values for each channel
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
# Define function for prediction
def classify():
    # Get the image file from the request
    image_file = request.files['image']

    # Read the image file into a NumPy array
    image = cv2.imdecode(np.fromstring(
        image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # save image to temporary folder
    filename = secure_filename(image_file.filename)
    image_file.save(os.path.join('uploads', filename))

    # Preprocess image and extract features
    X = preprocess_and_extract_features(image)

    # Reshape feature array
    X_reshaped = X.reshape(1, -1)

    # Create dataframe with feature names
    feature_names = ['H', 'S', 'V']
    X_new = pd.DataFrame(data=X_reshaped, columns=feature_names)

    # Predict label
    y_pred = nb.predict(X_new)

    # result
    result = int(y_pred[0])

    # Print label
    # print(f'Label: {y_pred[0]}')
    return jsonify({'Label': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
