from flask import Flask
from routes import bp
import os

app = Flask(__name__)
app.register_blueprint(bp)


@app.route('/')
def hello_world():
    return 'Welcome to MKAD distance API. Created by  <a href="https://www.linkedin.com/in/hendrik-martina-54800468/">Hendrik Martina</a>'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
