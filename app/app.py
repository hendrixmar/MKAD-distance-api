from flask import Flask
from routes import bp
import os

app = Flask(__name__)
app.register_blueprint(bp)



@app.route('/<name>')
def hello_world(name):
    return "Welcome to MKAD distance API"+ name


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
