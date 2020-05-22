from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return send_file('templates/index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8888)


@app.route('/api/init_connection')
def init_connection():
    pass


@app.route('/api/press_button')
def press_button(button):
    pass


@app.route('/api/load_amiibo')
def load_amiibo(amiibo):
    pass
