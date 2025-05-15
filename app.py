import logging
logging.basicConfig(level=logging.INFO)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  return '♻️ One more test: CD pipeline is rock solid!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

@app.route('/')
def home():
    app.logger.info("Home page was accessed")
    return "Hello from Flask!"

@app.route('/health')
def health():
    return "OK", 200
