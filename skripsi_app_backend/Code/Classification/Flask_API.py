from sklearn.metrics import accuracy_score, classification_report
from flask import Flask, request
import cv2
import numpy as np
import pandas as pd
import joblib


def preprocessing(image):

    # inisialisasi ukuran resize
    width, height = 1080, 1920

    # melakukan resize pada file
    image = cv2.resize(image, (width, height),
                       interpolation=cv2.INTER_AREA)
    # melakukan cropping pada file
    image = image[420:1500, 0:1080]

    return image


def extract_features(preprocessed_image):

    # mengubah gambar ke dalam format HSV
    hsv = cv2.cvtColor(preprocessed_image, cv2.COLOR_BGR2HSV)

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

    return features


def classify(image):
    # Load pre-trained model
    nb = joblib.load('../Model/NaiveBayes.pkl')

    image = cv2.imread(image)

    # Preprocess image
    img_array = preprocessing(image)

    # Extract features
    X = extract_features(img_array)

    # Predict label
    y_pred = nb.predict([X])

    # Print label
    print(f'Label: {y_pred[0]}')

    return y_pred

    # # Load true label
    # df = pd.read_csv('../csv/hasil_ekstraksi_rata2_hsv.csv')
    # y_true = df['label']

    # # Print accuracy and precision
    # print(classification_report(y_true, y_pred))
    # print(f'Accuracy: {accuracy_score(y_true, y_pred)}')


app = Flask(__name__)


@app.route('/')
def home():
    return 'API Python sedang berjalan'


@app.route('/klasifikasi', methods=['POST'])
def klasifikasi():
    if request.method == 'POST':
        classify('../hama_tungau (17).jpg')
        return 'Gambar telah diklasifikasikan'
    else:
        return 'Metode permintaan yang diberikan tidak valid'


if __name__ == '__main__':
    app.run(debug=True)
