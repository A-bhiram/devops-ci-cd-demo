
import logging
from flask import Flask

# Set up logging level
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello():
    app.logger.info("Root / endpoint was accessed")
    return '🔁 One more test: CD pipeline is rock solid!'

@app.route('/health')
def health():
    app.logger.info("/health endpoint was accessed")
    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
