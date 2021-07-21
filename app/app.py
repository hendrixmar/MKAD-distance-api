from flask import Flask
from cordinate_distance import example_blueprint
import os

app = Flask(__name__)
app.register_blueprint(example_blueprint)


@app.route('/')
def hello_world():
    return os.environ.get('API_YANDEX_KEY', None)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
