from flask import Flask
import logging
from prometheus_client import Counter, generate_latest

# Setup logging
logging.basicConfig(level=logging.INFO)

# Prometheus metric counters
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])

app = Flask(__name__)

@app.route('/')
def hello():
    app.logger.info("Root / endpoint was accessed")
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return '🚀 One more test: CI pipeline is rock solid!'

@app.route('/health')
def health():
    app.logger.info("/health endpoint was accessed")
    REQUEST_COUNT.labels(method='GET', endpoint='/health').inc()
    return "OK", 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
