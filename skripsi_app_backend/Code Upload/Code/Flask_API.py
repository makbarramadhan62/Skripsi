from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'API Python sedang berjalan'


@app.route('/klasifikasi', methods=['POST'])
def klasifikasi():
    if request.method == 'POST':
        # Lakukan klasifikasi gambar di sini
        return 'Gambar telah diklasifikasikan'
    else:
        return 'Metode permintaan yang diberikan tidak valid'


if __name__ == '__main__':
    app.run(debug=True)
