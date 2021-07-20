from flask import Flask
from cordinate_distance import example_blueprint
app = Flask(__name__)
app.register_blueprint(example_blueprint)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
