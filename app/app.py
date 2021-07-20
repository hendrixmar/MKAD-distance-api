from flask import Flask
from cordinate_distance import example_blueprint
app = Flask(__name__)
app.register_blueprint(example_blueprint)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
